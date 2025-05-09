# -*- coding: utf-8 -*-
# from odoo import http


# class PetManagement(http.Controller):
#     @http.route('/pet_management/pet_management', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/pet_management/pet_management/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('pet_management.listing', {
#             'root': '/pet_management/pet_management',
#             'objects': http.request.env['pet_management.pet_management'].search([]),
#         })

#     @http.route('/pet_management/pet_management/objects/<model("pet_management.pet_management"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('pet_management.object', {
#             'object': obj
#         })

