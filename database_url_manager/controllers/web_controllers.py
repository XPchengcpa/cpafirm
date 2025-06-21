from odoo import http
from odoo.addons.web.controllers.home import Home as WebHome
from odoo.addons.web.controllers.utils import ensure_db
from odoo.http import request


class MyWebHome(WebHome):

    @http.route(['/web', '/odoo', '/odoo/<path:subpath>', '/scoped_app/<path:subpath>'], type='http', auth="none", readonly=WebHome._web_client_readonly)
    def web_client(self, s_action=None, **kw):
        ensure_db()
        if kw.get('debug') and ("assets" in kw.get('debug')or "1" in kw.get('debug')):
            if not request.env.user.browse(request.session.uid)._is_admin():
                return request.redirect('/')

        return super().web_client(s_action=s_action, **kw)
