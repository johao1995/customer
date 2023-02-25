from odoo import models,fields,api
from odoo.exceptions import ValidationError
from datetime import datetime

import logging
# Model Abstract
class Information(models.AbstractModel):
    _name="asistencia.information"

    name=fields.Char(string="Nombre")
    lastname=fields.Char(string="APellido")
    dni=fields.Char(string="Documento",size=8)
    sexo=fields.Selection(string="Sexo",selection=[
        ('H','Masculino'),
        ('F','Femenino')
    ])
    sede=fields.Selection(string="Sede",selection=[
        ('001','Chorrillos'),
        ('002','Surco'),
        ('003','Lima'),
    ],default='001')
    
    

class User(models.Model):
    _name="asistencia.user"
    _inherit="asistencia.information"
    _description="Informacio Usuario"

    date_inicio=fields.Date(string="Fecha Salida")
    date_regreso=fields.Date(string="Fecha Retorno")
    image_sustent=fields.Binary(string="Archivo")
    date_today=fields.Date(string="Fecha Actual",default=datetime.now())
    jefe_id=fields.Many2one(string="Jefe",comodel_name="asistencia.jefe_user")
    area_user=fields.Char(string="Area",related="jefe_id.area_id.name")
    image_user=fields.Binary(string="Imagen")

    @api.constrains("dni")
    def constrains_dni(self):
        if not(self.dni):
            raise ValidationError("Error el campo Nombre es Obligatorio")


    @api.model
    def create(self,data):
        logging.info(data)
        user=self.env["asistencia.user"].search([('name','=',data['name'])])
        logging.info(user)
        if user.name==data["name"]:
            raise ValidationError(f"Error El usuario {user.name} existe")
        
        return super(User,self).create(data)
