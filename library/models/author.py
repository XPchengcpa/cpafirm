from odoo import models, fields

class Author(models.Model):
    _name = 'library.author'
    _description = 'Library Author'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    bio = fields.Text(string='Bio')
    book_ids = fields.One2many(
        'library.book',
        'author_id',
        string='Books'
    )
    #author 的文件中，book_ids 是 一个 1对多 的 关系，一个作者可以有多个书，一个书只能有一个作者；
    #作者里面有个字段是book-ids，这个字段是 一个 1对多 的 关系，一个作者可以有多个书，一个书只能有一个作者； 
    #关联的是书，通过author_id 关联到书； 


   