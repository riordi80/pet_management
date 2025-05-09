# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Species(models.Model):
    _name = 'pet_management.species'
    _description = 'Especie de mascota'

    name = fields.Char(string="Nombre", required=True, translate=True)

#    value2 = fields.Float(compute="_value_pc", store=True)
#    description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

