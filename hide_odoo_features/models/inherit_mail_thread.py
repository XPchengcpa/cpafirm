# -*- coding: utf-8 -*-

from odoo import api, fields, models

class CpaMailThread(models.AbstractModel):
    _inherit = 'mail.thread'

    def _notify_by_email_prepare_rendering_context(self, message, msg_vals=False,
                                                   model_description=False,
                                                   force_email_company=False,
                                                   force_email_lang=False,
                                                   force_record_name=False):
        result = super()._notify_by_email_prepare_rendering_context(message=message,
                                                           msg_vals=msg_vals,
                                                           model_description=model_description,
                                                           force_email_company=force_email_company,
                                                           force_email_lang=force_email_lang,
                                                           force_record_name=force_record_name)
        is_force_footer = int(self.env['ir.config_parameter'].sudo().get_param('is_email_notification_force_footer'))
        is_allow_footer = int(self.env['ir.config_parameter'].sudo().get_param('is_email_notification_allow_footer'))
        result['email_notification_force_footer'] = result['email_notification_force_footer'] if is_force_footer else False
        result['email_notification_allow_footer'] = result['email_notification_allow_footer'] if is_allow_footer else False
        return result
