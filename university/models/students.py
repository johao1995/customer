from odoo import fields,models,api

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
    speciality_id=fields.Many2one(string="Especialidad",comodel_name="university.speciality")
    docente_ids=fields.Many2many(string="Docente",comodel_name="university.docente")

    def Aprobar(self):
        self.state="aprobar"

    def Borrador(self):
        self.state="borrador"
    
    def Anulado(self):
        self.state="anulado"

    @api.model
    def create(self,values):
        return super(Students,self).create(values)

    def write(self,values):
        return super(Students,self).write(values)

    def unlink(self):
        return super(Students,self).unlink()


  

