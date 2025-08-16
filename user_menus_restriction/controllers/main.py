# -*- coding: utf-8 -*-
from odoo import _
from odoo.exceptions import AccessError
from odoo.http import request, route
from odoo.addons.web.controllers import action


class UrlAction(action.Action):

    @route('/web/action/load', type='json', auth='user', readonly=True)
    def load(self, action_id, context=None):
        result = super().load(action_id=action_id, context=context)
        access_error = False
        try:
            Actions = request.env['ir.actions.actions']
            base_action = Actions.browse([result.get('id')])
            if base_action:
                user = request.env['res.users'].sudo().browse(request.session.uid)
                if not user or len(user.hide_ui_menu_ids) == 0 or user.is_admin:
                    return result
                menu_recs = request.env['ir.ui.menu'].sudo().with_context({'ir.ui.menu.full_list': True}).search([
                    ('id', 'in', user.hide_ui_menu_ids.ids),
                    ('action', '!=', False)
                ])
                for menu in menu_recs:
                    if menu.action.id == base_action.id:
                        access_error = True
        except Exception as e:
            pass
        if access_error:
            raise AccessError(_("No permission to access this action"))
        return result
