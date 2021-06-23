# -*- coding: utf-8 -*-


from flectra import api, fields, models, _


class McCategory(models.Model):
    _name = "mc.category"
    _description = "Doctors Category"

    name = fields.Char(string='Category Name', required=True)
    doctors_category_code = fields.Char(string="Code", required=True)
    seq_code = fields.Char(string='Category Code',
        required=True, copy=False, readonly=True,
        default=lambda self: _('New'))
    
    @api.model
    def create(self,vals):
        if vals.get('seq_code', _('New')) == _('New'):
            vals['seq_code'] = self.env['ir.sequence'].next_by_code('mc.category') or _('New')
        line = super(McCategory, self).create(vals)
        return line
    
    