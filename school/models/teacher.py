from odoo import fields,models,api

class Teacher(models.Model):
    _name="school.teacher"
    _description="Register of Teachers"

    name=fields.Char(string="Maestro")
    profile=fields.Text(string="Perfil")
    subject_ids=fields.One2many(string="Sujeto",comodel_name="school.subject",inverse_name="teacher_id")