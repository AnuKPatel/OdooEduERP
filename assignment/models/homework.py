# -*- coding: utf-8 -*-
# See LICENSE file for full copyright and licensing details.

from odoo import models, fields, api
from odoo.exceptions import ValidationError


class SchoolTeacherAssignment(models.Model):
    _name = 'school.teacher.assignment'
    _description = 'Teacher Assignment Information'

    @api.constrains('assign_date', 'due_date')
    def check_date(self):
        if self.due_date < self.assign_date:
            raise ValidationError('Due date of homework should be greater than assign date')

    name = fields.Char('Assignment Name')
    subject_id = fields.Many2one('subject.subject', 'Subject', required=True)
    standard_id = fields.Many2one('school.standard', 'Standard')
    teacher_id = fields.Many2one('hr.employee', 'Teacher', required=True)
    assign_date = fields.Date('Assign Date', required=True)
    due_date = fields.Date('Due Date', required=True)
    attached_homework = fields.Binary('Attached Home work')
    state = fields.Selection([('draft', 'Draft'), ('active', 'Active')],
                             'Status', readonly=True, default='draft')
    school_id = fields.Many2one('school.school', 'School Name',
                                related='standard_id.school_id')
    cmp_id = fields.Many2one('res.company', 'Company Name',
                             related='school_id.company_id')

    @api.multi
    def active_assignment(self):
        ''' This method change state as active state
            and create assignment line
            @return : True
        '''
        assignment_obj = self.env['school.student.assignment']
        std_ids = []
        self._cr.execute('''select id from student_student\
                            where standard_id=%s''', (self.standard_id.id,))
        student = self._cr.fetchall()
        if student:
            for stu in student:
                std_ids.append(stu[0])
        if std_ids:
            for std in std_ids:
                ass_dict = {'name': self.name,
                            'subject_id': self.subject_id.id,
                            'standard_id': self.standard_id.id,
                            'assign_date': self.assign_date,
                            'due_date': self.due_date,
                            'state': 'active',
                            'attached_homework': self.attached_homework,
                            'teacher_id': self.teacher_id.id,
                            'student_id': std}
                assignment_id = assignment_obj.create(ass_dict)
                if self.attached_homework:
                    attach = {'name': 'test',
                              'datas': str(self.attached_homework),
                              'description': 'Assignment attachment',
                              'res_model': 'school.student.assignment',
                              'res_id': assignment_id.id}
                    self.env['ir.attachment'].create(attach)
                self.write({'state': 'active'})
            return True


class SchoolStudentAssignment(models.Model):
    _name = 'school.student.assignment'
    _description = 'Student Assignment Information'

    @api.constrains('assign_date', 'due_date')
    def check_date(self):
        if self.due_date < self.assign_date:
            raise ValidationError('Due date of homework should be greater than Assign date')

    name = fields.Char('Assignment Name')
    subject_id = fields.Many2one('subject.subject', 'Subject', required=True)
    standard_id = fields.Many2one('school.standard', 'Standard', required=True)
    teacher_id = fields.Many2one('hr.employee', 'Teacher', required=True)
    assign_date = fields.Date('Assign Date', required=True)
    due_date = fields.Date('Due Date', required=True)
    state = fields.Selection([('draft', 'Draft'), ('active', 'Active'),
                              ('done', 'done')], 'Status', readonly=True)
    student_id = fields.Many2one('student.student', 'Student', required=True)
    attached_homework = fields.Binary('Attached Home work')

    @api.multi
    def done_assignment(self):
        ''' This method change state as done
            for school student assignment
            @return : True
        '''
        self.state = 'done'
        return True
