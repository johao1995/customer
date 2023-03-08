from odoo import fields,models,api


class Product(models.Model):
    _name="movies.product"
    _description="Producto"

    name=fields.Char(string="Producto")
    description=fields.Char(string="Descripcion")
    price_uni=fields.Float(string="Precio")


class DetailPresupuesto(models.Model):
    _name="movies.detail.presupuesto"
    _description="Detalle Presupuesto"

    name=fields.Char(string="Nombre",related="product_id.name")
    description=fields.Char(string="Descripción",related="product_id.description")
    quanty=fields.Integer(string="Cantidad")
    price_uni=fields.Float(string="Precio Unitario",related="product_id.price_uni")
    importe=fields.Float(string="Importe")
    presupuesto_id=fields.Many2one(string="Detalle",comodel_name="movies.presupuesto")
    product_id=fields.Many2one(string="Producto",comodel_name="movies.product")

    @api.onchange('quanty')
    def onchange_importe(self):
        self.importe=self.quanty*self.price_uni
