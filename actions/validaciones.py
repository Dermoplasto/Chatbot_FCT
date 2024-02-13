'''# This files contains your custom actions which can be used to run
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

from actions.sql_auxiliar import *
from actions.validaciones import *
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
