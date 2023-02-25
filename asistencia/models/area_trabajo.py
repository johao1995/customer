from odoo import fields,models,api


class AreaTrabajo(models.Model):
    _name="asistencia.area_trabajo"
    
    name=fields.Char(string="Area")
    code=fields.Selection(string="Codigo",selection=[
        ('001S','Area Sistemas'),
        ('001T','Area T.I'),
        ('001A','Area Analista')
    ])
