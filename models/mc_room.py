# -*- coding: utf-8 -*-


from flectra import api, fields, models, _


class McRoom(models.Model):
    _name = "mc.room"
    _description = "Medical Centre Room"

    name = fields.Many2one(comodel_name='mc.rmcategory', string='Category Name', required=True)
    room_no = fields.Integer(string='Room Number', required=True)
    seq_rmcode = fields.Char(string='Room Code',
        required=True, copy=False, readonly=True,
        default=lambda self: _('New'))
    floor_no = fields.Integer(string='Floor Number', required=True)
    
    
    @api.model
    def create(self,vals):
        if vals.get('seq_rmcode', _('New')) == _('New'):
            vals['seq_rmcode'] = self.env['ir.sequence'].next_by_code('mc.rmcategory') or _('New')
        line = super(McRoom, self).create(vals)
        return line
    