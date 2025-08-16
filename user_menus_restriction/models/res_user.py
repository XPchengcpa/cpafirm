# -*- coding: utf-8 -*-

from odoo import models, fields, api


class HideMenuUser(models.Model):
    _inherit = 'res.users'

    is_admin = fields.Boolean(compute='_compute_is_admin', string="Admin")
    hide_menu_ids = fields.Many2many('ir.ui.menu', 'res_user_hide_menus_rel', string="Hide Menus")

    def _compute_is_admin(self):
        for rec in self:
            rec.is_admin = False
            if rec.id == self.env.ref('base.user_admin').id:
                rec.is_admin = True

    @api.model_create_multi
    def create(self, vals_list):
        self.clear_caches()
        return super(HideMenuUser, self).create(vals_list)

    def write(self, vals):
        res = super(HideMenuUser, self).write(vals)
        for record in self:
            for menu in record.hide_menu_ids:
                menu.write({
                    'restrict_user_ids': [(4, record.id)]
                })
        self.clear_caches()
        return res


class UserRestrictMenu(models.Model):
    _inherit = 'ir.ui.menu'

    restrict_user_ids = fields.Many2many('res.users', 'res_user_hide_menus_rel', string="User")
