from odoo import fields, models


class StatusCultivation(models.Model):
    _name = 'status.cultivation'
    _description = 'Status Cultivation'
    _rec_name = 'name'

    name = fields.Char(string='Status Name', required=True)
    code = fields.Char(string='Code', required=True)
    active = fields.Boolean(default=True)



class StatusLandDetails(models.Model):
    _name = 'status.land.details'
    _description = 'Status Land Details'
    _rec_name = 'name'

    name = fields.Char(string='Status Name', required=True)
    code = fields.Char(string='Code', required=True)
    active = fields.Boolean(default=True)


class StatusSubsidy(models.Model):
    _name = 'status.subsidy'
    _description = 'Status Subsidy'
    _rec_name = 'name'

    name = fields.Char(string='Status Name', required=True)
    code = fields.Char(string='Code', required=True)
    active = fields.Boolean(default=True)


class StatusGrant(models.Model):
    _name = 'status.grant'
    _description = 'Status Subsidy'
    _rec_name = 'name'

    name = fields.Char(string='Status Name', required=True)
    code = fields.Char(string='Code', required=True)
    active = fields.Boolean(default=True)


class StatusFlood(models.Model):
    _name = 'status.flood'
    _description = 'Status Flood'
    _rec_name = 'name'

    name = fields.Char(string='Status Name', required=True)
    code = fields.Char(string='Code', required=True)
    active = fields.Boolean(default=True)
