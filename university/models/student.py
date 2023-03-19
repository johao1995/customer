from odoo import fields,models,api

class Student(models.Model):
    _name="university.student"
    
    name=fields.Char(string="Estudiante")
    code=fields.Char(string="Codigo",size=10)
    document=fields.Char(string="Documento",size=8)
    image=fields.Binary(string="Imagen")
    state=fields.Selection(selection=[
        ('borrador','Borrador'),
        ('aprobar','Aprobar'),
    ])
    active=fields.Boolean(string="Estado")
    speciality_id=fields.Many2one(string="Especialidad",comodel_name="university.speciality",ondelete="cascade")
    docente_ids=fields.Many2many(string="Docente",comodel_name="university.docente",ondelete="cascade")


  

