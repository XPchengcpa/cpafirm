from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Title', required=True)
    #author = fields.Char(string='Author')  # 这个字段被注释掉了，因为作者现在是一个关联字段，而不是一个简单的字符串
    published_date = fields.Date(string='Published Date')

    author_id = fields.Many2one(
        'library.author',
        string='Author'
    )
    #many2one 在author里面不写 one2many 也可以
    #但是写了 one2many 就必须在对应的模型中写many2one ，否则会报错； 

