# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

class BookBorrowWizard(models.TransientModel):
    _name = 'library.borrow.wizard'
    _description = 'Book Borrow Wizard'

    book_id = fields.Many2one(
        'library.book',
        string='Book',
        required=True,
        default=lambda self: self._default_book_id()
    )
    borrower_id = fields.Many2one(
        'res.partner',
        string='Borrower',
        required=True
    )
    borrow_date = fields.Date(
        string='Borrow Date',
        default=fields.Date.context_today,
        required=True
    )
    return_date = fields.Date(
        string='Due Return Date',
        required=True
    )

    @api.model
    def _default_book_id(self):
        # 获取上下文中的图书ID
        return self.env.context.get('active_id')

    def action_confirm_borrow(self):
        self.ensure_one()
        # 创建借阅记录
        borrow = self.env['library.borrow'].create({
            'book_id': self.book_id.id,
            'borrower_id': self.borrower_id.id,
            'borrow_date': self.borrow_date,
            'return_date': self.return_date,
            'state': 'borrowed'
        })
        
        # 返回借阅记录视图
        return {
            'name': _('Borrow Record'),
            'view_mode': 'form',
            'res_model': 'library.borrow',
            'res_id': borrow.id,
            'type': 'ir.actions.act_window',
            'target': 'current',
        }