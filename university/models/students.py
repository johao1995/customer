from odoo import fields,models,api
from datetime import datetime
from odoo.exceptions import ValidationError

class Students(models.Model):
    _name="university.students"
    
    name=fields.Char(string="Estudiante")
    code=fields.Char(string="Codigo",size=10)
    document=fields.Char(string="Documento",size=8)
    image=fields.Binary(string="Imagen")
    state=fields.Selection(selection=[
        ('borrador','Borrador'),
        ('aprobar','Aprobado'),
        ('anulado','Anulado')
    ],default="borrador")
    active=fields.Boolean(string="Estado",default=True)
    date_ini=fields.Date(string="Fecha Inscripción")
    date_cul=fields.Date(string="Fecha Anulacion")
    speciality_id=fields.Many2one(string="Especialidad",comodel_name="university.speciality")
    docente_ids=fields.Many2many(string="Docente",comodel_name="university.docente")

    # @api.constrains('code')
    # def code_constrains(self):
    #     name=self.env['']

    def Aprobar(self):
        self.state="aprobar"
        self.date_ini=datetime.now()

    def Borrador(self):
        self.state="borrador"
    
    def Anulado(self):
        self.state="anulado"
        self.date_cul=datetime.now()

    @api.model
    def create(self,values):
        obj_university_students=self.env['university.students'].search_read([],['document','code'])
        # print("***oBJETO***")
        # print(obj_university_students)
        print(values)
        for o in obj_university_students:
            if values['code']==o['code']:
                raise ValidationError("Error el codigo {} existe ingrese otro ....!".format(values['code']))
            elif values['document']==o['document']:
                raise ValidationError("Error el documento {} existe ingrese otro ....!".format(values['document']))
        
        return super(Students,self).create(values)

    def write(self,values):
        return super(Students,self).write(values)

    def unlink(self):
        return super(Students,self).unlink()


  

