# -*- coding: utf-8 -*-
import random
from odoo import models, fields, api


class Libreria(models.Model):
    _name = 'libreria.libreria'
    _description = 'Libreria'

    name = fields.Char(string="Nombre", required=True)
    autor = fields.Char(string="Autor", required=True)
    editorial = fields.Char(string="Editorial", required=True)
    fecha = fields.Date(string="Fecha de publicación", required=True)
    precio = fields.Float(string="Precio", required=True)
    cantidad = fields.Integer(string="Cantidad", required=True)
    codigo = fields.Char(string="Código", required=True)
    estado = fields.Selection([('disponible', 'Disponible'), ('no disponible', 'No disponible')], string="Estado", default='disponible')
    categoria = fields.Many2one('libreria.categoria', string="Categoría", required=True)
    descripcion = fields.Text(string="Descripción")

    @api.model
    def create(self, vals):
        vals['codigo'] = self.env['ir.sequence'].next_by_code('libreria.libreria')
        return super(Libreria, self).create(vals)

    def action_disponible(self):
        self.estado = 'disponible'

    def action_no_disponible(self):
        self.estado = 'no disponible'

    def action_random(self):
        self.cantidad = random.randint(1, 100)

    def action_random2(self):
        self.precio = random.randint(1, 100)

    def action_random3(self):
        self.fecha = random.randint(1, 100)

    def action_random4(self):
        self.autor = random.randint(1, 100)

    def action_random5(self):
        self.editorial = random.randint(1, 100)

    def action_random6(self):
        self.descripcion = random.randint(1, 100)

    def action_random7(self):
        self.categoria = random.randint(1, 100)

    def action_random8(self):
        self.name = random.randint(1, 100)

    def action_random9(self):
        self.estado = random.randint(1, 100)

    def action_random10(self):
        self.codigo = random.randint(1, 100)
