# -*- coding: utf-8 -*-
from flectra import api, fields, models, _


class McRmCategory(models.Model):
    _name = "mc.rmcategory"
    _description = "Rooms Category"

    name = fields.Char(string='Category Name', required=True)
    description = fields.Text(string="Description")
    seq_rmcode = fields.Char(string='Category Code',
        required=True, copy=False, readonly=True,
        default=lambda self: _('New'))
    
    @api.model
    def create(self,vals):
        if vals.get('seq_rmcode', _('New')) == _('New'):
            vals['seq_rmcode'] = self.env['ir.sequence'].next_by_code('mc.rmcategory') or _('New')
        line = super(McRmCategory, self).create(vals)
        return line
    
    