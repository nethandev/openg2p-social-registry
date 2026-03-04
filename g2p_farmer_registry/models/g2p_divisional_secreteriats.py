from odoo import api, fields, models


class DivisionalSecretariat(models.Model):
    _name = 'g2p.divisional.secretariat'
    _description = 'Divisional Secretariat'
    _order = 'name asc'

    name = fields.Char(string='Name', required=True, index=True)
    # ds_id = fields.Char(string='ID', required=True, size=11, index=True)
    district_id = fields.Many2one('g2p.district', string='District', required=True, index=True)
    active = fields.Boolean(string='Active', default=True)

    # _sql_constraints = [
    #     ('ds_id_unique', 'unique(ds_id)', 'DS ID must be unique!'),
    # ]

    @api.model
    def _name_search(self, name, args=None, operator='ilike', limit=100, name_get_uid=None):
        """ Allow search by name or ds_id """
        args = args or []
        domain = []
        if name:
            domain = [('name', operator, name)]
        return self._search(domain + args, limit=limit, access_rights_uid=name_get_uid)