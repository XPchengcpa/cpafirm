from odoo import models, fields, api


class LibraryBook(models.Model):
    _name = 'library.book'
    _inherit = ['mail.thread']
    _description = 'Library Book'
    _check_company_auto = True

    name = fields.Char(string='Name', required=True)
    publisher = fields.Char(string="Publisher")
    published_date = fields.Date(string='Published Date')
    currency_id = fields.Many2one('res.currency', help='The currency used to sale', string="Currency")
    company_id = fields.Many2one('res.company', string='Company', required=True, readonly=True, index=True, default=lambda self: self.env.company,
        help="Company")
    original_price = fields.Monetary(string="Original Amount", currency_field='currency_id')
    discount_amount = fields.Monetary(string="Discount Amount", currency_field='currency_id')
    final_price = fields.Monetary(string="Discounted Amount", currency_field='currency_id',
                                 compute='_compute_final_price', store=True)
    # buyer_id = fields.Many2one('res.partner', string="Buyer")
    tag_ids = fields.Many2many('library.book.tag', 'library_book_tag_rel', string="Tags")
    author_id = fields.Many2one(
        'library.author',
        string='Author'
    )
    image = fields.Image(string="Image")
    state = fields.Selection(
        selection=[
            ('draft', 'Draft'),
            ('published', 'Published'),
            ('cancel', 'Cancelled'),
        ],
        string='Status',
        required=True,
        readonly=True,
        copy=False,
        tracking=True,
        default='draft',
    )
    #many2one 在author里面不写 one2many 也可以
    #但是写了 one2many 就必须在对应的模型中写many2one ，否则会报错； 

    @api.depends('original_price', 'discount_amount')
    def _compute_final_price(self):
        for book in self:
            book.final_price = book.original_price - book.discount_amount
