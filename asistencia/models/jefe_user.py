from odoo import fields,models,api
from odoo.exceptions import ValidationError
import logging

class JefeUser(models.Model):
    _name="asistencia.jefe_usuer"
    _inherit="asistencia.information"

    @api.constrains("dni")
    def constrains_dni(self):
        if not(self.dni):
            raise ValidationError("Error el campo Nombre es Obligatorio")


    @api.model
    def create(self,data):
        logging.info(data)
        user=self.env["asistencia.jefe_usuer"].search([('name','=',data['name'])])
        logging.info(user)
        if user.name==data["name"]:
            raise ValidationError(f"Error El usuario {user.name} existe")
        
        return super(JefeUser,self).create(data)