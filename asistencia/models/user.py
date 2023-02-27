from odoo import models,fields,api
from odoo.exceptions import ValidationError
import logging
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
    _inherit="asistencia.information"
    _name="asistencia.user"
    _description="Informacio Usuario"

    date_inicio=fields.Datetime(string="Fecha Salida")
    date_regreso=fields.Datetime(string="Fecha Retorno")
    image_sustent=fields.Binary(string="Archivo")

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
