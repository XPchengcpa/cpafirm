# Copyright 2018 Simone Orsi - Camptocamp SA
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).
{
    "name": "隐藏odoo特性",
    "version": "18.0.0.0.1",
    "author": "Mo Li",
    "category": "Extra Tools",
    "license": "LGPL-3",
    "depends": ["auth_totp"],
    "application": False,
    "installable": True,
    "auto_install": False,
    "data": [
        'views/res_users_profile_views.xml'
      ],
}
