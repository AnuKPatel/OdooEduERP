# -*- encoding: UTF-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2012-Today Serpent Consulting Services PVT. LTD.
#    (<http://www.serpentcs.com>)
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>
#
##############################################################################

{
    'name': 'Timetable Management',
    'version': '3.0',
    'author': 'Serpent Consulting Services PVT. LTD.',
    'website': 'http://www.serpentcs.com',
    'category': 'School Management',
    'complexity': 'easy',
    'summary': 'A Module For Timetable Management In School',
    'description': 'A module to School Timetable Management.',
    'depends': ['school'],
    'data': [
        'security/ir.model.access.csv',
        'views/timetable_view.xml',
        'views/report_view.xml',
        'views/timetable.xml',
    ],
    'demo': ['demo/timetable_demo.xml'],
    'test': [
        'test/timetable.yml'
    ],
    'installable': True,
    'application': True,
}
