
from odoo import models,fields,api
from odoo.exceptions import ValidationError
from datetime import datetime

class AppMoviesDirector(models.Model):
    _name="app_movies.director"
    description="director of movie"

    name=fields.Char(string="Director",size=50,help="Director de la pelicula")
    