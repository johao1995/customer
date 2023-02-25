from odoo import fields,models,api

class AppMoviesDetalle(models.Model):
    _name="app_movies.detalle"

    name=fields.Many2one(string="Pelicula",comodel_name="app_movies.movie")
    description=fields.Char(string="Descripcion",related="name.name")
    date=fields.Datetime(string="Fecha")
    quanty=fields.Integer(string="Entradas")
    price=fields.Float(string="Precio",default=15)
    importe=fields.Float(string="Importe")

    @api.onchange("quanty")
    def _importe(self):
        if self.quanty:
            self.importe=self.quanty*self.price
        else:
            self.importe=0


