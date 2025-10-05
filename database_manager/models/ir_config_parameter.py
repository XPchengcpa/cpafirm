# -*- coding: utf-8 -*-
from odoo import models


class IrConfigParameter(models.Model):
    _inherit = 'ir.config_parameter'

    def _register_hook(self):
        super()._register_hook()
        record = self.search([('key', '=', 'database.expiration_date')])
        if record:
            record.write({
                "value": "2099-01-01 00:00:00"
            })
