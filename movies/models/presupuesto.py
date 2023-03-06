from odoo import models,api,fields

class Presupuesto(models.Model):
    _name='movies.presupuesto'
    _description='Presupuesto de Peliculas'

    name=fields.Char(string="Nombre",size=100)
    clasification=fields.Selection(string="Clasificacion",selection=[
        ('G','G'),#Publico General
        ('PG','PG'),#Se recomienda compañia de un adulto
        ('PG-13','PG-13'),#Mayores de 13
        ('R','R'),#En compañia de un adulto obligatorio
        ('NC-17','NC-17'),#Mayores de 18

    ],default="G")
    date_streno=fields.Date(string="Fecha Estreno")
    puntuacion=fields.Integer(string="Puntuacion",related="puntuacion2")
    puntuacion2=fields.Integer(string="Puntuacion2")
    active=fields.Boolean(string="Estado")
    director_id=fields.Many2one(string="Director",comodel_name="res.partner")
    genero_ids=fields.Many2many(string="Genero",comodel_name="movies.genero")
    description=fields.Text(string="Description")
    image=fields.Binary(string="Imagen")
    link_trailer=fields.Char(string="Link")
    is_book=fields.Boolean(string="Version Libro")
    book_pdf=fields.Binary(string="Libro")
    state=fields.Selection(string="Estado Presupuesto",selection=[
        ('aprobado','Aprobado'),
        ('borrador','Borrador')
    ],default="borrador")

    def Aprobado(self):
        self.state="aprobado"

    def Borrador(self):
        self.state="borrador"