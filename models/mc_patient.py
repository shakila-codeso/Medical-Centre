# -*- coding: utf-8 -*-
from flectra import api, fields, models, _


class McPatient(models.Model):
    _name = "mc.patient"
    _description = "Medical Centre Patient"
    _rec_name = 'patient_code'

    name = fields.Char(string='Full Name', required=True,
        track_visibility='onchange')
    name_with_initials = fields.Char(string='Name With Initials',
        required=True)
    patient_code = fields.Char(string='Patient Code',
        required=True, copy=False, readonly=True,
        default=lambda self: _('New'))
    age = fields.Integer(string='Age', track_visibility='onchange', required=True)
    gender = fields.Selection([
        ('female', 'Female'),
        ('male', 'Male'),
        ('other', 'other'),
    ], required=True, default='male', track_visibility='onchange')
    contact = fields.Char(string='Contact Number', track_visibility='always', required=True)
    address = fields.Text(string='Address', track_visibility='always')
    emg_name = fields.Char(string='Name', required=True,
        track_visibility='onchange')
    emg_relation = fields.Char(string='Relationship', required=True,
        track_visibility='onchange')
    emg_contact = fields.Char(string='Contact Number', track_visibility='always', required=True)
    
    
    @api.model
    def create(self,vals):
        if vals.get('patient_code', _('New')) == _('New'):
            vals['patient_code'] = self.env['ir.sequence'].next_by_code('mc.patient') or _('New')
        line = super(McPatient, self).create(vals)
        return line