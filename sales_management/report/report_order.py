from odoo import fields,models,api
from datetime import date

class ReportOrder(models.AbstractModel):
    _name="report.sales_management.report_order"
    description="Informe de Pedidos"

    @api.model
    def _get_report_values(self,docids,data):
        obj_order=self.env['sales_management.order'].browse(docids)
        return {
            'docs':obj_order,
            'date':date.today()
        }