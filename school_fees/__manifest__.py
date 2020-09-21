# See LICENSE file for full copyright and licensing details.

{
    'name': 'Fees Management',
    'version': "14.0.1.0.0",
    'author': 'Serpent Consulting Services Pvt. Ltd.',
    'website': 'http://www.serpentcs.com',
    'category': 'School Management',
    'license': "AGPL-3",
    'complexity': 'easy',
    'summary': 'A Module For Fees Management In School',
    'depends': ['account', 'school'],
    'images': ['static/description/SchoolFees.png'],
    'data': ['security/ir.model.access.csv',
             'security/security_fees.xml',
             'views/school_fees_view.xml',
             'data/school_fees_sequence.xml',
             'report/student_payslip.xml',
             'report/student_fees_register.xml',
             'report/report_view.xml'],
    'demo': ['demo/school_fees_demo.xml'],
    'installable': True,
    'application': True
}
