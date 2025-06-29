from odoo import models, fields

class Publisher(models.Model):
    _name = 'library.publisher'
    #_name 代表一个模型的名字。
    _description = 'Library Publisher'

    name = fields.Char(string='Name', required=True)
    address = fields.Text(string='Address')
    phone = fields.Char(string='Phone')
    email = fields.Char(string='Email')
    website = fields.Char(string='Website')
    
    # 关联的图书
    book_ids = fields.One2many(
        'library.book',
        'publisher_id',
        string='Books'
    ) 