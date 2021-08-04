# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

import logging
_logger = logging.getLogger(__name__)

import requests
import json

class ResCompany(models.Model):
    _inherit = 'res.company'

    def action_py_login(self):
        url = 'https://auth-api.pedidosya.com/v1/token'
        headers = {'Content-type': 'application/json', 'Accept': 'text/plain'}
        obj = {
            "client_id": self.py_client_id,
            "client_secret": self.py_client_secret,
            "grant_type": "password",
            "password": self.py_password,
            "username": self.py_username
        }
        x = requests.post(url, data=json.dumps(obj), headers=headers)
        self.py_token = x.json()['access_token']


    py_client_id = fields.Char(string='PedidosYa Client Id', help='PedidosYa Client Id')
    py_client_secret = fields.Char(string='PedidosYa Client Secret', help='PedidosYa Client Secret')
    py_username = fields.Char(string='PedidosYa Username', help='PedidosYa Username')
    py_password = fields.Char(string='PedidosYa Password', help='PedidosYa Password')
    py_reference_id = fields.Char(string='PedidosYa Reference ID', help='Client Reference ID. The cadet requests it to withdraw the package.')

    py_token = fields.Char(string='PedidosYa Token', help='PedidosYa Token', readonly="True")

class DeliveryCarrier(models.Model):
    _inherit = 'delivery.carrier'

    urlPYRateShipment = 'https://courier-api.pedidosya.com/v1/estimates/shippings'

    delivery_type = fields.Selection(selection_add=[('pedidosya', 'Pedidos Ya')])

    def pedidosya_rate_shipment(self, order):
        headers = {
            "Accept": "application/json",
            "Content-Type": "application/json",
            "Authorization": self.company_id.py_token
        }

        payload = {
            "referenceId": "Client Internal Reference",
            "isTest": true,
            "deliveryTime": "2020-06-24T19:00:00Z",
            "notificationMail": "email@email.com",
            "volume": 20.02,
            "weight": 0.8,
            "items": [
                {
                "categoryId": 123,
                "value": 1250.6,
                "description": "Unos libros de Kotlin y una notebook.",
                "quantity": 1,
                "volume": 10.01,
                "weight": 0.5
                },
                {
                "categoryId": 124,
                "value": 250,
                "description": "Una remera",
                "quantity": 1,
                "volume": 10.01,
                "weight": 0.3
                }
            ],
            "waypoints": [
                {
                "type": "PICK_UP",
                "addressStreet": "Plaza Independencia 755",
                "addressAdditional": "Piso 6 Recepción",
                "city": "Montevideo",
                "latitude": -34.905988,
                "longitude": -56.199592,
                "phone": "+59898765432",
                "name": "Oficina Ciudad Vieja",
                "instructions": "El ascensor esta roto.",
                "order": 1
                },
                {
                "type": "DROP_OFF",
                "latitude": -34.9138414,
                "longitude": -56.1837661,
                "addressStreet": "La Cumparsita 1475",
                "addressAdditional": "Piso 1, Oficina Delivery",
                "city": "Montevideo",
                "phone": "+59812345678",
                "name": "Agustin",
                "instructions": "Entregar en mano",
                "order": 2
                }
            ]
        }

        response = requests.request("POST", urlPYRateShipment, json=payload, headers=headers)

        print(response.text)
