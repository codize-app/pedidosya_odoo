# -*- coding: utf-8 -*-
from odoo import http

# class AndreaniOdoo(http.Controller):
#     @http.route('/andreani_odoo/andreani_odoo/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/andreani_odoo/andreani_odoo/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('andreani_odoo.listing', {
#             'root': '/andreani_odoo/andreani_odoo',
#             'objects': http.request.env['andreani_odoo.andreani_odoo'].search([]),
#         })

#     @http.route('/andreani_odoo/andreani_odoo/objects/<model("andreani_odoo.andreani_odoo"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('andreani_odoo.object', {
#             'object': obj
#         })