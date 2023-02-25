
from odoo import models,fields,api
from odoo.exceptions import ValidationError
from datetime import datetime

class AppMoviesCategory(models.Model):
    _name="app_movies.category"
    description="Category of Movie"

    name=fields.Char(string="Categoria",size=50,help="Categoria de la pelicula")
    