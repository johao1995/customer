from odoo import fields,models,api
from datetime import date

class ReportCustomer(models.AbstractModel):
    _name="report.sales_management.report_customer"
    description="Informe de Clientes"

    @api.model
    def _get_report_values(self,docids,data=None):
        obj_customer=self.env['sales_management.customer'].search([])
        print(obj_customer)

        return {
            'docs':obj_customer,
            'date':date.today()
        }