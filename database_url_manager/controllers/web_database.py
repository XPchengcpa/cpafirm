# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request
from odoo.addons.web.controllers.database import Database


class DatabaseAccessController(http.Controller):

    @http.route('/web/database/selector', type='http', auth="user")
    def selector(self, **kw):
        if request.env.user.has_group('database_url_manager.group_database_url_manager'):
            if request.db:
                request.env.cr.close()
            return Database._render_template(self, manage=False)
        return request.redirect('/web')


    @http.route('/web/database/manager', type='http', auth="user")
    def manager(self, **kw):
        if request.env.user.has_group('database_url_manager.group_database_url_manager'):
            if request.db:
                request.env.cr.close()
            return Database._render_template(self)
        return request.redirect('/web')

Database.selector = DatabaseAccessController.selector
Database.manager = DatabaseAccessController.manager