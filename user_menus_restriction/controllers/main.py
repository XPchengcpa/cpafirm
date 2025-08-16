# -*- coding: utf-8 -*-
from odoo import _
from odoo.exceptions import AccessError
from odoo.http import request, route
from odoo.addons.web.controllers import action


class UrlAction(action.Action):

    @route('/web/action/load', type='json', auth="user")
    def load(self, action_id, additional_context=None):
        Actions = request.env['ir.actions.actions']
        try:
            action_id = int(action_id)
        except ValueError:
            try:
                action = request.env.ref(action_id)
                assert action._name.startswith('ir.actions.')
                action_id = action.id
            except Exception:
                action_id = 0

        base_action = Actions.browse([action_id]).sudo().read(['type'])
        if base_action:
            user = request.env['res.users'].sudo().browse(request.session.uid)
            if not user or len(user.hide_menu_ids) == 0:
                return super().load(action_id, additional_context=additional_context)
            menu = False
            menu_ids = request.env['ir.ui.menu'].sudo().with_context({'ir.ui.menu.full_list': True}).search([])
            for menu in menu_ids:
                if menu.action and menu.action.id == action_id and menu.id in user.hide_menu_ids.ids:
                    raise AccessError(_("No permission to access this action"))

        return super().load(action_id, additional_context=additional_context)
