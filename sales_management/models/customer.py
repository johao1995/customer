from odoo import models,fields,api
import logging
_logger=logging.getLogger(__name__)

class Customer(models.Model):
    _name="sales_management.customer"
    _description="Cliente"

    name=fields.Char(string="Nombre",size=100)
    apellido1=fields.Char(string="Apellido1",size=100)
    apellido2=fields.Char(string="Apellido2",size=100)
    city=fields.Char(string="Ciudad",size=50)
    category=fields.Integer(string="Categoria")
    state_order=fields.Boolean(string="Ver Pedido")
    order_ids=fields.One2many(string="Pedidos",comodel_name="sales_management.order",inverse_name="customer_id")


    @api.model
    def create(self,data):
        return super(Customer,self).create(data)

    def write(self,data):
        return super(Customer,self).write(data)
    
    def unlink(self):
        return super(Customer,self).write()