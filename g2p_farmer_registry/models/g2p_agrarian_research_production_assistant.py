from odoo import api, fields, models, tools, _


class AgrarianResearchProductionAssistant(models.Model):
    _name = 'g2p.agrarian.research.production.assistant'
    _description = 'Agrarian Research & Production Assistant'
    _rec_name = 'arpa_name'

    asc_id = fields.Many2one( 'g2p.agrarian.service.center', string='ASC', required=True, ondelete='cascade')
    arpa_code = fields.Char(string='Code', size=10, required=True)
    arpa_name = fields.Char(string='Name', size=100)
    arpa_sname = fields.Char(string='Sinhala Name', size=100)
    arpa_tname = fields.Char(string='Tamil Name', size=100)

    # Need clarification because in odoo itself there are fields to set these values
    # arpa_status = fields.Selection(
    #     [('A', 'Active'), ('I', 'Inactive')],string='Status',default='A')
    created_at = fields.Datetime( string='Created At', default=fields.Datetime.now, readonly=True)
    updated_at = fields.Datetime(string='Updated At',readonly=True)
    active = fields.Boolean(default=True)

    def write(self, vals):
        vals['updated_at'] = fields.Datetime.now()
        return super().write(vals)
