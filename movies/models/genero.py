from odoo import models,fields,api

class Genero(models.Model):
    _name="movies.genero"
    _description="Genero de peliculas"

    name=fields.Char(string="Nombre")