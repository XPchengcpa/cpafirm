import logging
from odoo import models, fields, api
_logger = logging.getLogger(__name__)


class Author(models.Model):
    _name = 'library.author'
    _description = 'Library Author'

    name = fields.Char(string='Name', required=True)
    email = fields.Char(string='Email')
    bio = fields.Text(string='Bio')
    birth_date = fields.Date(string='Birth Date', help='Author birth date')
    book_ids = fields.One2many(
        'library.book',
        'author_id',
        string='Books'
    )
    #author 的文件中，book_ids 是 一个 1对多 的 关系，一个作者可以有多个书，一个书只能有一个作者；
    #作者里面有个字段是book-ids，这个字段是 一个 1对多 的 关系，一个作者可以有多个书，一个书只能有一个作者； 
    #关联的是书，通过author_id 关联到书； 


    @api.depends_context('author_from_book', 'author_from_borrow')
    def _compute_display_name(self):
        _logger.info(self._context)
        if not self._context.get('author_from_book') and not self._context.get('author_from_borrow'):
            return super()._compute_display_name()
        for author in self:
            if self._context.get('author_from_book'):
                author.display_name = f'{author.name} - {author.email}'
            else:
                author.display_name = f'{author.name}'
# {
#     'lang': 'zh_CN', 
#     'tz': 'Asia/Shanghai', 
#     'uid': 2, 
#     'allowed_company_ids': [1], 
#     'bin_size': True, 
#     'params': {
#         'resId': 1, 
#         'action': 567, 
#         'actionStack': [{'action': 567}, {'resId': 1, 'action': 567}]
#     }, 
#     'author_from_book': '1'
# }
