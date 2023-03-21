from odoo import fields,models,api
from datetime import date
from dateutil.relativedelta import relativedelta


class Students(models.Model):
    _name='school.student'
    _description="Register of Students"

    name=fields.Char(string="Estudiante")
    birth_date=fields.Date(string="Fecha Cumpleaños")
    age=fields.Integer(string="Edad",compute="compute_age")
    final_exam_grade=fields.Float(string="Examen Final")
    subject_ids=fields.Many2many(string="Sujeto",comodel_name="school.subject")

    @api.depends('birth_date')
    def compute_age(self):
        for record in self:
            record.age=relativedelta(date.today(),record.birth_date).years