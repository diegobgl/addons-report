# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2018-BroadTech IT Solutions (<http://www.broadtech-innovations.com/>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

from odoo import api, fields, models

class BtAccountBalanceCheck(models.TransientModel):
    _name = 'bt.account.balance.check'
    _description = 'Wizard for checking account balance'

    account_id = fields.Many2one('account.account', 'Account', required=True)
    date  = fields.Date('Date', required=True)
    check_bal = fields.Boolean('Check Balance', default=False)
    balance = fields.Float('Balance')
     
    @api.multi  
    def check_balance(self):
        for wiz in self:
            domain = [('account_id','=',wiz.account_id.id),('date','<=',wiz.date)]
            move_lines = self.env['account.move.line'].search(domain)
            balance = 0
            for line in move_lines:
                balance += line.debit - line.credit
            wiz.balance = balance
            wiz.check_bal = True
            return {
                    'view_mode': 'form',
                    'res_id': wiz.id,
                    'res_model': 'bt.account.balance.check',
                    'view_type': 'form',
                    'type': 'ir.actions.act_window',
                    'name':'Account Balance Check',
                    'context': self.env.context,
                    'target': 'new',
                       } 
            
    
    
             
