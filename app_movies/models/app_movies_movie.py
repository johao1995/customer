
from odoo import models,fields,api
from odoo.exceptions import ValidationError
from datetime import datetime

class Movies(models.Model):
    _name="app_movies.movie"
    description="Movies for our customers"

    name=fields.Char(string="Pelicula",size=50)
    description=fields.Text(string="Descripcion")
    director_id=fields.Many2one(string="Director",comodel_name="app_movies.director",ondelete="cascade")
    category_ids=fields.Many2many(string="Categoria",comodel_name="app_movies.category",ondelete="cascade",default=lambda self:self.env['app_movies.category'].search([]))
    date_public=fields.Datetime(string="Fecha",default=datetime.now())
    idioma_movie=fields.Selection(string="Idioma",selection=[
        ("spanish","Español"),
        ("english","Ingles")
    ],default="spanish")
    disponible_movie=fields.Selection(string="Disponible",selection=[
        ("disponible","Disponible"),
        ("agotado","No Disponible")
    ])
    image=fields.Binary(string="Imagen",help="Imagen de la Pelicula")
    detalle_ids=fields.One2many(string="Detalle Pelicula",comodel_name="app_movies.detalle",inverse_name="name")

    @api.constrains("image","description","name")
    def _get_image_description(self):
        if not(self.image and self.description and self.name):
            raise ValidationError("Error Debe registrar el archivo imagen,descripcion y nombre de la pelicula")

    @api.model
    def create(self,data):
        get_name=data['name']
        object_name=self.env["app_movies.movie"].search_read([],['id','name'])
        for names in object_name:
            if names['name']==get_name:
                raise ValidationError("Error la pelicula debe ser diferente......")
        return super(Movies,self).create(data)
    

    def write(self,data):
        return super(Movies,self).write(data)

    def unlink(self):
        return super(Movies,self).unlink()


  