# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2018-BroadTech IT Solutions (<http://www.broadtech-innovations.com/>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
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

{
    'name': 'Account Balance Check by Date',
    'version': '0.1',
    'category': 'Accounting',
    'license':'LGPL-3',
    'summary': '"Check Account Balance Date Wise"',
    'description': """
    This module helps users to check the balance in an Odoo account on any selected date from the past.
    """,
    'author': 'BroadTech IT Solutions Pvt Ltd',
    'website': 'http://www.broadtech-innovations.com/',
    'depends': ['account','account_accountant'],
    'data': [
        'wizard/bt_accnt_balance_check.xml'
    ],
    'images': ['static/description/banner.jpg'],
    'installable': True,
    'application': True,
    'auto_install': False,
    'qweb': [
    ],
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
