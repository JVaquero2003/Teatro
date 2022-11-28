# -*- coding: utf-8 -*-
import random
from odoo import models, fields, api

class obra_teatro(models.Model):
    _name = 'teatro.obra_teatro'

    id = fields.Integer(string="ID", required=True)
    titulo = fields.Char(string="Titulo", required=True)
    idioma = fields.Char(string="Idioma", required=True)
    duracion = fields.Float(string="Duracion", required=True)
    genero = fields.Selection([('drama', 'Drama'), ('comedia', 'Comedia'), ('tragedia', 'Tragedia')], string="Genero", required=True)
    fecha_estreno = fields.Date(string="Fecha de estreno", required=True)
    resumen = fields.Text(string="Resumen", required=True)
    director = fields.Many2one('teatro.directores', string="Directores")
    opiniones = fields.One2many('teatro.opinion', 'obra_teatro', string="Opiniones")
    salas = fields.Many2one('teatro.sala', string="Salas")
    promociones = fields.Many2many('teatro.promociones', string="Promociones")

class personas(models.Model):
    _name = 'teatro.personas'

    id = fields.Integer(string="ID", required=True)
    nombre = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    fecha_nacimiento = fields.Date(string="Fecha de nacimiento", required=True)
    nacionalidad = fields.Char(string="Nacionalidad", required=True)
    direccion = fields.Char(string="Direccion", required=True)
    telefono = fields.Char(string="Telefono", required=True)

class directores(models.Model):
    _inherit = 'teatro.personas'

    _name= 'teatro.directores'

    destreza = fields.Selection([('baja', 'Baja'), ('media', 'Media'), ('alta', 'Alta')], string="Destreza", required=True)
    experiencia = fields.Selection([('baja', 'Baja'), ('media', 'Media'), ('alta', 'Alta')], string="Experiencia", required=True)
    conocimientos = fields.Char(string="Conocimientos", required=True)
    obra_teatro = fields.One2many('teatro.obra_teatro','director', string="Obras de teatro")

class actores(models.Model):
    _inherit = 'teatro.personas'

    _name = 'teatro.actores'

    fecha_inicio = fields.Date(string="Fecha de inicio", required=True)
    personaje = fields.Char(string="Personaje", required=True)
    obra_teatro = fields.Many2many('teatro.obra_teatro', string="Obras de teatro")

class opinion(models.Model):
    _name = 'teatro.opinion'

    id = fields.Integer(string="ID", required=True)
    nombre = fields.Char(string="Nombre", required=True)
    apellidos = fields.Char(string="Apellidos", required=True)
    edad = fields.Integer(string="Edad", required=True)
    fecha_publicacion = fields.Date(string="Fecha de publicacion", required=True)
    valoracion = fields.Selection([('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')], string="Valoracion", required=True)
    texto = fields.Text(string="Texto", required=True)
    obra_teatro = fields.Many2one('teatro.obra_teatro', string="Obra de teatro", required=True)

class salas(models.Model):
    _name = 'teatro.salas'

    id = fields.Integer(string="ID", required=True)
    nombre = fields.Char(string="Nombre", required=True)
    capacidad = fields.Integer(string="Capacidad", required=True)
    obra_teatro = fields.One2many('teatro.obra_teatro','salas', string="Obras de teatro")

class promociones(models.Model):
    _name = 'teatro.promociones'

    id = fields.Integer(string="ID", required=True)
    descripcion = fields.Text(string="Descripcion", required=True)
    descuento = fields.Float(string="Descuento", required=True)
    obra_teatro = fields.Many2many('teatro.obra_teatro', string="Obras de teatro")