# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions

from typing import Dict, Text, List, Optional, Any
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.forms import FormValidationAction
from rasa_sdk.events import SlotSet
from rasa_sdk.types import DomainDict

from actions.sql_aux import *
from actions.validaciones import * 

class ActionEdad(Action):
    """Acción que según la edad deja entrar o no"""
    def name(self) -> Text:
        return "action_edad"
        
    def run(self, dispatcher, tracker, domain):
        edad_slot = tracker.get_slot('edad') 
        response = ""
        for e in edad_slot:  
            edad = int(e)  
            if edad >= 18:				
                response = """¡Genial! Pregúntame lo que quieras saber."""						
            else:
                response = """Lo siento, eres menor de edad y no puedo contestarte. ¡Hasta luego!"""    			
        dispatcher.utter_message(response)
        return []


class ActionResetSlots(Action):
	"""Acción para resetear los slots"""
	def name(self) -> Text:
		return "action_resetear"
	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
# Devuelve a None todos los slots
		return [
			SlotSet("pais", None), 
			SlotSet("tipo", None),
			SlotSet("edad", None)
           ]  


class ActionMostrarCervezas(Action):
    """Mostramos los edificios disponibles"""

    def name(self) -> Text:
        return "action_cervezas"

    def run(
        self,
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]
    ) -> List[Dict[Text, Any]]:
        
        cervezas = consultar_cervezas(tipo=None, pais=None)

        dispatcher.utter_message("Las cervezas de las que disponemos son las siguientes:")
        for cerveza in cervezas:
            return(cerveza)

        return []

'''     

# Accion por la que el usuario consulta una cerveza
class ActionConsultaCerveza(Action):
	"""Mostramos la cerveza que el usuario ha consultado"""

	def name(self) -> Text:
		return "action_consulta_cerveza"

def run(self, dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		# Obtenemos la cerveza que el usuario ha consultado
		cerveza = tracker.get_slot("cerveza")
		# Obtenemos la informacion de la cerveza
		cerveza_info = consultar_cerveza(cerveza)
		# Si la cerveza no existe, informamos al usuario
		if not cerveza_info:
			dispatcher.utter_message("Lo siento, no tengo información sobre esa cerveza.")
			return []
		# Si la cerveza existe, la informamos al usuario
		dispatcher.utter_message("La cerveza que has consultado es la siguiente: ")
		dispatcher.utter_message("Nombre: {}".format(cerveza_info[0][1]))
		dispatcher.utter_message("País de origen: {}".format(cerveza_info[0][2]))
		dispatcher.utter_message("Categoría: {}".format(cerveza_info[0][3]))
		dispatcher.utter_message("Graduación: {}".format(cerveza_info[0][4]))
		dispatcher.utter_message("Precio: {}".format(cerveza_info[0][5]))
		return []


# Accion por la que el usuario consulta las cervezas de un país

class ActionConsultaPaisCerveza(Action):

	"""Mostramos las cervezas de un país que el usuario ha consultado"""
def name(self) -> Text:
	return "action_consulta_pais_cerveza"

def run(self, dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		# Obtenemos el país que el usuario ha consultado
		pais = tracker.get_slot("pais_origen")
		# Obtenemos la informacion de las cervezas del país
		cervezas_info = consultar_paiscerves(pais)
		# Si no hay cervezas de ese país, informamos al usuario
		if not cervezas_info:
			dispatcher.utter_message("Lo siento, no tengo información sobre cervezas de ese país.")
			return []
		# Si hay cervezas de ese país, las informamos al usuario
		dispatcher.utter_message("Las cervezas de {} son las siguientes: ".format(pais))
		for cerveza in cervezas_info:
			dispatcher.utter_message("Nombre: {}".format(cerveza[1]))
			dispatcher.utter_message("País de origen: {}".format(cerveza[2]))
			dispatcher.utter_message("Categoría: {}".format(cerveza[3]))
			dispatcher.utter_message("Graduación: {}".format(cerveza[4]))
			dispatcher.utter_message("Precio: {}".format(cerveza[5]))
		return []

# Accion por la que el usuario consulta las cervezas de una categoria

class ActionConsultaCategoriaCerveza(Action):

	"""Mostramos las cervezas de una categoria que el usuario ha consultado"""

def name(self) -> Text:
	return "action_consulta_categoria_cerveza"

def run(self, dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		# Obtenemos la categoria que el usuario ha consultado
		categoria = tracker.get_slot("categoria")
		# Obtenemos la informacion de las cervezas de la categoria
		cervezas_info = consultar_categoria(categoria)
		# Si no hay cervezas de esa categoria, informamos al usuario
		if not cervezas_info:
			dispatcher.utter_message("Lo siento, no tengo información sobre cervezas de esa categoría.")
			return []
		# Si hay cervezas de esa categoria, las informamos al usuario
		dispatcher.utter_message("Las cervezas de la categoría {} son las siguientes: ".format(categoria))
		for cerveza in cervezas_info:
			dispatcher.utter_message("Nombre: {}".format(cerveza[1]))
			dispatcher.utter_message("País de origen: {}".format(cerveza[2]))
			dispatcher.utter_message("Categoría: {}".format(cerveza[3]))
			dispatcher.utter_message("Graduación: {}".format(cerveza[4]))
			dispatcher.utter_message("Precio: {}".format(cerveza[5]))
		return []

# Accion por la que el usuario consulta las cervezas de una graduacion

class ActionConsultaGraduacionCerveza(Action):

	"""Mostramos las cervezas de una graduacion que el usuario ha consultado"""

def name(self) -> Text:
	return "action_consulta_graduacion_cerveza"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		# Obtenemos la graduacion que el usuario ha consultado
		graduacion = tracker.get_slot("graduacion")
		# Obtenemos la informacion de las cervezas de la graduacion
		cervezas_info = consultar_graduacion(graduacion)
		# Si no hay cervezas de esa graduacion, informamos al usuario
		if not cervezas_info:
			dispatcher.utter_message("Lo siento, no tengo información sobre cervezas de esa graduación.")
			return []
		# Si hay cervezas de esa graduacion, las informamos al usuario
		dispatcher.utter_message("Las cervezas de graduación {} son las siguientes: ".format(graduacion))
		for cerveza in cervezas_info:
			dispatcher.utter_message("Nombre: {}".format(cerveza[1]))
			dispatcher.utter_message("País de origen: {}".format(cerveza[2]))
			dispatcher.utter_message("Categoría: {}".format(cerveza[3]))
			dispatcher.utter_message("Graduación: {}".format(cerveza[4]))
			dispatcher.utter_message("Precio: {}".format(cerveza[5]))
		return [] 

# Accion por la que el usuario consulta las cervezas de un precio

class ActionConsultaPrecioCerveza(Action):
	
	"""Mostramos las cervezas de un precio que el usuario ha consultado"""

def name(self) -> Text:
	return "action_consulta_precio_cerveza"

	def run(self, dispatcher: CollectingDispatcher,
			tracker: Tracker,
			domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
		# Obtenemos el precio que el usuario ha consultado
		precio = tracker.get_slot("precio")
		# Obtenemos la informacion de las cervezas de la graduacion
		cervezas_info = consultar_precio(precio)
		# Si no hay cervezas de ese precio, informamos al usuario
		if not cervezas_info:
			dispatcher.utter_message("Lo siento, no tengo información sobre cervezas de ese precio.")
			return []
		# Si hay cervezas de ese precio, las informamos al usuario
		dispatcher.utter_message("Las cervezas de precio {} son las siguientes: ".format(precio))
		for cerveza in cervezas_info:
			dispatcher.utter_message("Nombre: {}".format(cerveza[1]))
			dispatcher.utter_message("País de origen: {}".format(cerveza[2]))
			dispatcher.utter_message("Categoría: {}".format(cerveza[3]))
			dispatcher.utter_message("Graduación: {}".format(cerveza[4]))
			dispatcher.utter_message("Precio: {}".format(cerveza[5]))
		return []

# validaciones

class ValidateConsultaCervezaForm(FormValidationAction):

	def name(self) -> Text:
		return "validate_consulta_cerveza_form"

	def validate_cerveza(
		self,
		slot_value: Any,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: DomainDict,
		) -> Optional[Text]:
		"""Validamos que la cerveza que el usuario ha introducido existe"""
		cerveza = slot_value
		cerveza_info = consultar_cerveza(cerveza)
		if not cerveza_info:
			dispatcher.utter_message("Lo siento, no tengo información sobre esa cerveza.")
			return {"cerveza": None}
		return {"cerveza": cerveza}

class ValidateConsultaPaisCervezaForm(FormValidationAction):

	def name(self) -> Text:
		return "validate_consulta_pais_cerveza_form"

	def validate_pais_origen(
		self,
		slot_value: Any,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: DomainDict,
		) -> Optional[Text]:
		"""Validamos que el país que el usuario ha introducido existe"""
		pais = slot_value
		cervezas_info = consultar_paiscerves(pais)
		if not cervezas_info:
			dispatcher.utter_message("Lo siento, no tengo información sobre cervezas de ese país.")
			return {"pais_origen": None}
		return {"pais_origen": pais}

class ValidateConsultaCategoriaCervezaForm(FormValidationAction):

	def name(self) -> Text:
		return "validate_consulta_categoria_cerveza_form"

	def validate_categoria(
		self,
		slot_value: Any,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: DomainDict,
		) -> Optional[Text]:
		"""Validamos que la categoria que el usuario ha introducido existe"""
		categoria = slot_value
		cervezas_info = consultar_categoria(categoria)
		if not cervezas_info:
			dispatcher.utter_message("Lo siento, no tengo información sobre cervezas de esa categoría.")
			return {"categoria": None}
		return {"categoria": categoria}

class ValidateConsultaGraduacionCervezaForm(FormValidationAction):

	def name(self) -> Text:
		return "validate_consulta_graduacion_cerveza_form"

	def validate_graduacion(
		self,
		slot_value: Any,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: DomainDict,
		) -> Optional[Text]:
		"""Validamos que la graduacion que el usuario ha introducido existe"""
		graduacion = slot_value
		cervezas_info = consultar_graduacion(graduacion)
		if not cervezas_info:
			dispatcher.utter_message("Lo siento, no tengo información sobre cervezas de esa graduación.")
			return {"graduacion": None}
		return {"graduacion": graduacion}

class ValidateConsultaPrecioCervezaForm(FormValidationAction):

	def name(self) -> Text:
		return "validate_consulta_precio_cerveza_form"

	def validate_precio(
		self,
		slot_value: Any,
		dispatcher: CollectingDispatcher,
		tracker: Tracker,
		domain: DomainDict,
		) -> Optional[Text]:
		"""Validamos que el precio que el usuario ha introducido existe"""
		precio = slot_value
		cervezas_info = consultar_precio(precio)
		if not cervezas_info:
			dispatcher.utter_message("Lo siento, no tengo información sobre cervezas de ese precio.")
			return {"precio": None}
		return {"precio": precio}

		
'''



