from odoo import models,api
from datetime import date

class ReportWizardAsistenciaUser(models.AbstractModel):
    _name="report.asistencia.report_wizard_asistencia_user"

    @api.model
    def _get_report_values(self,docids,data=None):
        
        #query
        obj_asis_user=self.env["asistencia.user"].search_read(
            [('jefe_id.area_id.code','=',data['code_area']),
            ('date_inicio','=',data['date_inicio']),
            ('date_regreso','=',data['date_regreso'])],['id','name','dni','date_inicio','date_regreso','jefe_id','date_today']
        )
        print(obj_asis_user)
        return {
            "docs":obj_asis_user,
            "date":date.today()
        }