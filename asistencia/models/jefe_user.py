from odoo import fields,models,api
from odoo.exceptions import ValidationError
import logging

class JefeUser(models.Model):
    _name="asistencia.jefe_user"
    _inherit="asistencia.information"

    area_id=fields.Many2one(string="Area",comodel_name="asistencia.area_trabajo")

    @api.constrains("dni")
    def constrains_dni(self):
        if not(self.dni):
            raise ValidationError("Error el campo Nombre es Obligatorio")


    @api.model
    def create(self,data):
        
        user=self.env["asistencia.jefe_user"].search([('name','=',data['name'])])
        
        if user.name==data["name"]:
            raise ValidationError(f"Error El usuario {user.name} existe")
        
        return super(JefeUser,self).create(data)