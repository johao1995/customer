from odoo import models,fields,api
import logging

class WizardAsistenciaUser(models.TransientModel):
    _name="asistencia.wizard.asistencia.user"

    code_area=fields.Selection(string="Area",selection=[
        ('001S','Area Sistemas'),
        ('001T','Area T.I'),
        ('001A','Area Analista')
    ])
    date_inicio=fields.Date(string="Fecha Salida")
    date_regreso=fields.Date(string="Fecha Retorno")

    def check_report(self):
        data={
            'code_area':self.code_area,
            'date_inicio':self.date_inicio,
            'date_regreso':self.date_regreso
        }
        return self.env.ref("asistencia.report_action_wizard_asistencia_user").report_action(
            self,data=data
        )
        