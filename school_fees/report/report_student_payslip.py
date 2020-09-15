# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

import time
from datetime import datetime
from openerp.osv import osv
from openerp.report import report_sxw


class StudentPayslip(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context):
        super(StudentPayslip, self).__init__(cr, uid, name, context)

        self.localcontext.update({
            'time': time,
            'get_month': self.get_month,
            'get_no': self.get_no,
        })
        self.no = 0

    def get_no(self):
        self.no += 1
        return self.no

    def get_month(self, indate):
        new_date = datetime.strptime(indate, '%Y-%m-%d')
        out_date = new_date.strftime('%B') + '-' + new_date.strftime('%Y')
        return out_date


class ReportStudentPayslip(osv.AbstractModel):
    _name = 'report.school_fees.student_payslip'
    _inherit = 'report.abstract_report'
    _template = 'school_fees.student_payslip'
    _wrapped_report_class = StudentPayslip
