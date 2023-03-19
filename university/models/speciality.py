from odoo import fields,models,api

class Speciality(models.Model):
    _name="university.speciality"

    name=fields.Char(string="Especialidad")
    code=fields.Selection(string="Codigo",selection=[
        ('FIIS','Ing.Sistemas'),
        ('FIGAE','Ing.Civil'),
        ('FIEI','Ing.Informatica')
    ])
    
    
    # document=fields.Char(string="Documento")
    # #speciality=fields.Many2one(string="Especialidad")

