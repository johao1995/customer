from odoo import fields,models,api

class CategoryOperario(models.Model):
    _name='movies.category.operarios'
    _description='Categoria de Operarios'

    name=fields.Char(string="Nombre")