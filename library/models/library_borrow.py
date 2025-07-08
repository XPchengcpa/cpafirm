from odoo import models, fields, api
import logging

_logger = logging.getLogger(__name__)


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
    due_date = fields.Datetime(string='Due Date', tracking=True)
    # TODO: 把due_date字段改为Float类型，并且自动计算：归还时间 - 借阅时间 的天数
    due_days = fields.Float(string='Due Days', compute='_compute_due_days', store=True)
    #compute 是计算逻辑，store 是存储逻辑。compute 是一个函数，需要另外定义。
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
    
    @api.depends('return_date', 'borrow_date')
    def _compute_due_days(self):
        for record in self:
            if record.return_date and record.borrow_date:
                record.due_days = (record.return_date - record.borrow_date).days
            else:
                record.due_days = 0
    #函数定义不要和字段定义放在一起，要归类。
    #函数与函数之间要空行，保持一定的代码规范。
    #self 就是class 的实例。
    #return-date 是日期类型，borrow-date 是日期类型。.days 是日期类型。为什么要加.days?因为.days 是日期类型。取两个日期的时间段的天数
    
    # 创建方法
    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('name', 'New') == 'New':
                vals['name'] = self.env['ir.sequence'].next_by_code('library.borrow') or 'New'
            vals['borrower_id'] = 7
        result = super(LibraryBorrow, self).create(vals_list)
        result.write({
            'borrower_id': 8,
            'notes': "你好"
        })
        # result.borrower_id = 8
        # result.notes = "你好呀"
        return result
    
    # 修改方法
    def write(self, vals):
        _logger.info(vals)
        result = super().write(vals)
        return result

    # 删除方法
    def unlink(self):
        result = super().unlink()
        return result

    def search(self, domain, offset=0, limit=None, order=None):
        return super().search(domain, offset, limit, order)

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