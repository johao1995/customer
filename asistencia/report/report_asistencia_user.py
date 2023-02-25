from odoo import fields,models,api

from datetime import date

class ReportAsistenciaUser(models.AbstractModel):
    _name="report.asistencia.report_asistencia_user"

    @api.model
    def _get_report_values(self,docids,data=None):
        obj_asist_user=self.env["asistencia.user"].browse(docids)
        
        return {
            'docs':obj_asist_user,
            'date':date.today()
        }