from odoo import fields, models, _



class G2PSeason(models.Model):
    _name = 'g2p.season'
    _rec_name = 'name'

    name = fields.Char(string=_("Season"))
