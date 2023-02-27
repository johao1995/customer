from odoo import models,fields,api

class Homework(models.Model):
    _name='apps.tareas.homework'
    _description='LIsta de tareas'

    name=fields.Char(string="Nombre",track_visibility="onchange")
    description=fields.Text(string="Descripcion")
    state_materia=fields.Selection(string="Estado",selection=[
        ('iniciado','Iniciado'),
        ('pendiente','Pendiente'),
        ('finalizado','Finalizado')
    ],default='iniciado')