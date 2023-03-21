from odoo import fields,models,api

class Subject(models.Model):
    _name="school.subject"
    _description="List of Subjects"

    name=fields.Char(string="Sujeto")
    credits=fields.Integer(string="Creditos")
    max_students=fields.Integer(string="Cantidad Maxima")
    active=fields.Boolean(string="Estado",default=True)
    subject_ids=fields.Many2many(string="Estudiantes",comodel_name="school.student")
    teacher_id=fields.Many2one(string="Maestro",comodel_name="school.teacher")