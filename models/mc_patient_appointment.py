# -*- coding: utf-8 -*-
from flectra import api, fields, models, _


class McAppointment(models.Model):
    _name = "mc.appointment"
    _description = "Medical Centre Patient Appointment"

    name = fields.Many2one(comodel_name='mc.patient', string='Patient Name', required=True,
        track_visibility='onchange')
    reference_no = fields.Char(string='Reference No.',
        required=True, copy=False, readonly=True,
        default=lambda self: _('New'))
    doc_name = fields.Many2one(comodel_name='mc.docvisit', string='Doctors Name',
        required=True)
    app_category = fields.Many2one(comodel_name='mc.category', related='doc_name.doctors_category_code', string='Category',
        required=True)
    resp_nurse = fields.Char(string='Responsible nurse name', related='doc_name.resp_nurse', required=True)
    date = fields.Date(string='Date',related='doc_name.date', required=True)
    start_time = fields.Datetime(string='From', related='doc_name.start_time', required=True)
    end_time = fields.Datetime(string='To', related='doc_name.end_time', required=True)
    room_no = fields.Many2one(comodel_name='mc.room', related='doc_name.room_no',string='Venue', required=True)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
        ], string='Status', default='draft', track_visibility='onchange')
    
    def action_confirm(self):
        self.state = 'confirm'
    def action_done(self):
        self.state = 'done'
    def action_draft(self):
        self.state = 'draft'
    def action_cancel(self):
        self.state = 'cancel'

    @api.model
    def create(self,vals):
        if vals.get('reference_no', _('New')) == _('New'):
            vals['reference_no'] = self.env['ir.sequence'].next_by_code('mc.appointment') or _('New')
        line = super(McAppointment, self).create(vals)
        return line