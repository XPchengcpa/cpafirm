from odoo import models, fields, api
from datetime import datetime

class LibraryBookTags(models.Model):
    _name = 'library.book.tag'
    _description = 'Library Book Tag'

    name = fields.Char(string="名称")
    sequence = fields.Integer(default=10)
    color = fields.Char(string="Color", default='#3C3C3C')
