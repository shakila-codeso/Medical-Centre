# -*- coding: utf-8 -*-
from flectra import api, fields, models, _


class McDocVisit(models.Model):
    _name = "mc.docvisit"
    _description = "Doctors Visits Details"

    name = fields.Many2one(comodel_name='mc.doctor', string='Doctor Name', required=True)
    date = fields.Date(string='Date', required=True)
    start_time = fields.Datetime(string='From', required=True)
    end_time = fields.Datetime(string='To', required=True)
    room_no = fields.Many2one(comodel_name='mc.room', string='Venue', required=True)
    maximum_patients = fields.Integer(string='Maximum number of Patients', required=True)
    resp_nurse = fields.Char(string='Responsible nurse name', required=True)
    doctors_category_code = fields.Many2one(comodel_name='mc.category', string="Category", required=True)
    seq_doc_visit_code = fields.Char(string='Doctor Visit Code',
        required=True, copy=False, readonly=True,
        default=lambda self: _('New'))
    state = fields.Selection([
        ('draft', 'Draft'),
        ('confirm', 'Confirmed'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
        ], string='Status', default='draft', track_visibility='onchange')
    appointment_count = fields.Integer(string='Appointments', compute="_compute_appointment")

    def _compute_appointment(self):
        for rec in self:
            appointment_count = self.env['mc.appointment'].search_count([('doc_name','=',rec.id)])
            rec.appointment_count = appointment_count
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
        if vals.get('seq_doc_visit_code', _('New')) == _('New'):
            vals['seq_doc_visit_code'] = self.env['ir.sequence'].next_by_code('mc.docvisit') or _('New')
        line = super(McDocVisit, self).create(vals)
        return line

    



    
    