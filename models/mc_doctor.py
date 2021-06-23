# -*- coding: utf-8 -*-


from flectra import api, fields, models, _


class McDoctor(models.Model):
    _name = "mc.doctor"
    _description = "Medical Centre Doctor"

    name = fields.Char(string='First Name', required=True)
    last_name = fields.Char(string='Last Name', required=True)
    doctor_code = fields.Char(string='Doctor Code',
        required=True, copy=False, readonly=True,
        default=lambda self: _('New'))
    category_id = fields.Many2one(comodel_name='mc.category', string="Category", required=True)
    contact = fields.Char(string='Contact Number', required=True)
    hosp_name = fields.Char(string='Hospital Name', required=True)
    hosp_address = fields.Text(string='Hospital Address')
    hosp_contact = fields.Char(string='Hospital Contact Number', required=True)
    
    @api.model
    def create(self,vals):
        if vals.get('doctor_code', _('New')) == _('New'):
            vals['doctor_code'] = self.env['ir.sequence'].next_by_code('mc.doctor') or _('New')
        line = super(McDoctor, self).create(vals)
        return line
    