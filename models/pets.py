# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Pet(models.Model):
    _name = 'pet_management.pet'
    _description = 'Pet'

    name = fields.Char(string="Nombre")
    species_id = fields.Many2one(
    'pet_management.species',
    string="Especie",
    required=False
)
    birthday = fields.Date(string="Fecha de nacimiento")
    sex = fields.Selection([
    ('male', 'Macho'),
    ('female', 'Hembra')
], string="Sexo")
    owner_id = fields.Many2one('res.partner', string="Propietario")
    vaccination_ids = fields.One2many('pet_management.vaccination', 'pet_id', string="Vacunas")
    weight_log_ids = fields.One2many('pet_management.weight_log', 'pet_id', string="Historial de peso")