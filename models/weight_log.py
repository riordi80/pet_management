# -*- coding: utf-8 -*-

from odoo import models, fields, api

class WeightLog(models.Model):
    _name = 'pet_management.weight_log'
    _description = 'Registro de peso de la mascota'

    pet_id = fields.Many2one('pet_management.pet', string="Mascota", required=True, ondelete="cascade")
    date = fields.Date(string="Fecha", required=True)
    weight = fields.Float(string="Peso (kg)", required=True)

    day_string = fields.Char(string="Día", compute="_compute_day_string", store=True)

    @api.depends('date')
    def _compute_day_string(self):
        for record in self:
            if record.date:
                record.day_string = record.date.strftime("%d-%m-%Y")
