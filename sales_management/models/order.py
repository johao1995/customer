from odoo import models,fields,api
import logging
_logger=logging.getLogger(__name__)

class Order(models.Model):
    _name="sales_management.order"
    _description="Cliente"

    name=fields.Char(string="Nombre",size=100)
    quanty=fields.Float(string="Cantidad")
    date=fields.Date(string="Fecha")
    customer_id=fields.Many2one(string="Cliente",comodel_name="sales_management.customer")
    commercial_id=fields.Many2one(string="Comercial",comodel_name="sales_management.commercial")
    image_order=fields.Binary(string="Imagen")
    price=fields.Float(string="Precio")
    import_total=fields.Float(string="Importe")
    # igv=fields.Float(string="IGV")
    # total=fields.Float(string="Total")


    @api.onchange('quanty','price')
    def onchange_import_total(self):
        self.import_total=self.quanty*self.price
  



    @api.model
    def create(self,data):
        return super(Order,self).create(data)

    def write(self,data):
        return super(Order,self).write(data)
    
    def unlink(self):
        return super(Order,self).write()