# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Species(models.Model):
    _name = 'pet_management.species'
    _description = 'Especie de mascota'

    name = fields.Char(string="Nombre", required=True, translate=True)

