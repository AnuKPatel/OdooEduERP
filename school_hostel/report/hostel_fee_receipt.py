# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
#
from openerp.report import report_sxw
from openerp import models


class HostelFeeReceipt(report_sxw.rml_parse):

    def __init__(self, cr, uid, name, context):
        super(HostelFeeReceipt, self).__init__(cr, uid, name,
                                               context=context)


class ReportAddExamResult(models.AbstractModel):

    _name = 'report.school_hostel.hostel_fee_reciept'
    _inherit = 'report.abstract_report'
    _template = 'school_hostel.hostel_fee_reciept'
    _wrapped_report_class = HostelFeeReceipt
