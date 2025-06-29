from odoo import models, fields, api

class LibraryBorrow(models.Model):
    _name = 'library.borrow'
    _description = 'Library Borrow Record'
    _inherit = ['mail.thread']
    _order = 'borrow_date desc'
    #类的继承，继承mail.thread，mail.thread是odoo自带的模块，用于记录邮件的跟踪。
    #Line 8 都是属性，_name 代表一个模型的名字。


    name = fields.Char(string='Reference', required=True, copy=False, readonly=True, 
                      default=lambda self: 'New')
    book_id = fields.Many2one('library.book', string='Book', required=True, 
                             tracking=True, ondelete='restrict')
    borrower_id = fields.Many2one('res.partner', string='Borrower', required=True, 
                                 tracking=True, ondelete='restrict')
    author_id = fields.Many2one('library.author', string='Author', readonly=True, 
                               compute='_compute_author', store=True)
    #计算逻辑写到_compute_author函数中。
    borrow_date = fields.Datetime(string='Borrow Date', required=True, 
                                default=fields.Datetime.now, tracking=True)
    return_date = fields.Datetime(string='Return Date', tracking=True)
    due_date = fields.Datetime(string='Due Date', required=True, tracking=True)
    state = fields.Selection([
        ('borrowed', 'Borrowed'),
        #前面的是字段，后面的是字段名。
        ('returned', 'Returned'),
        ('overdue', 'Overdue'),
        ('cancelled', 'Cancelled'),
    ], string='Status', default='borrowed', required=True, tracking=True)
    
    notes = fields.Text(string='Notes')
    
    @api.depends('book_id')
    #装饰器，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，装饰器是用来装饰函数，
    def _compute_author(self):
        #self 代表当前的记录集，当前模型
        for record in self:
            #record 也是当前的记录集，当前模型
            record.author_id = record.book_id.author_id if record.book_id else False
    
    @api.model
    def create(self, vals):
        if vals.get('name', 'New') == 'New':
            vals['name'] = self.env['ir.sequence'].next_by_code('library.borrow') or 'New'
        return super(LibraryBorrow, self).create(vals)
    
    def action_return(self):
        self.ensure_one()
        self.write({
            'state': 'returned',
            'return_date': fields.Datetime.now()
        })
    
    def action_cancel(self):
        self.ensure_one()
        self.write({'state': 'cancelled'})
    
    @api.model
    def _check_overdue_books(self):
        """检查逾期图书的定时任务"""
        overdue_records = self.search([
            ('state', '=', 'borrowed'),
            ('due_date', '<', fields.Datetime.now())
        ])
        overdue_records.write({'state': 'overdue'}) 