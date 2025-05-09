# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Vaccination(models.Model):
    _name = 'pet_management.vaccination'
    _description = 'Vaccionation'

    name = fields.Char(string="Nombre")
    vaccine_date = fields.Date(string="Fecha")
    veterinarian = fields.Char(string="Veterinario/a")
    pet_id = fields.Many2one('pet_management.pet', string="Mascota", required=True)

#     value2 = fields.Float(compute="_value_pc", store=True)
#     description = fields.Text()
#
#     @api.depends('value')
#     def _value_pc(self):
#         for record in self:
#             record.value2 = float(record.value) / 100

