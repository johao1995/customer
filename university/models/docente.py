from odoo import fields,models,api

class Docente(models.Model):
    _name="university.docente"
    
    code=fields.Char(string="Codigo")
    name=fields.Char(string="Nombre")
    # document=fields.Char(string="Documento")
    # #speciality=fields.Many2one(string="Especialidad")

