from odoo import models,fields,api
import logging
_logger=logging.getLogger(__name__)

class Commercial(models.Model):
    _name="sales_management.commercial"
    _description="Comercial"

    name=fields.Char(string="Nombre",size=100)
    apellido1=fields.Char(string="Apellido1",size=100)
    apellido2=fields.Char(string="Apellido2",size=100)
    city=fields.Char(string="Ciudad",size=50)
    commission=fields.Float(string="Comision")


    @api.model
    def create(self,data):
        return super(Commercial,self).create(data)

    def write(self,data):
        return super(Commercial,self).write(data)
    
    def unlink(self):
        return super(Commercial,self).write()