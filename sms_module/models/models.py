# -*- coding: utf-8 -*-

from odoo import models, fields, api

from odoo.exceptions import ValidationError

class Student(models.Model):
    _name = 'sms_module.student'
    _description = 'Student'
    _rec_name = 'name'
    _sql_constraints = [
        ('unique_student_id', 'unique(student_id)', 'Student ID must be unique!')
    ]

    name = fields.Char(string='Name', required=True)
    description = fields.Html(string='Description')
    date_of_birth = fields.Date(string='Date of Birth')
    contact_details = fields.Text(string='Contact Details')
    address = fields.Text(string='Address')
    guardian_details = fields.Text(string='Guardian Details')
    student_id = fields.Char(string='Student ID', required=True)
    national_doc = fields.Binary(string='National Document')
    image = fields.Binary(string='Image')

class Course(models.Model):
    _name = 'sms_module.course'
    _description = 'Course'

    name = fields.Char(string='Name', required=True)
    description = fields.Text(string='Description')
    syllabus = fields.Text(string='Syllabus')
    duration = fields.Integer(string='Duration (in hours)')
    prerequisites = fields.Text(string='Prerequisites')


class Enrollment(models.Model):
    _name = 'sms_module.enrollment'
    _description = 'Enrollment'
    _sql_constraints = [
        ('unique_enrollment', 'unique(student_id, course_id)', 'Enrollment must be unique per student and course!')
    ]

    enrollment_date = fields.Date(string='Enrollment Date', required=True)
    student_id = fields.Many2one('sms_module.student', string='Student', required=True)
    course_id = fields.Many2one('sms_module.course', string='Course', required=True)


class Grade(models.Model):
    _name = 'sms_module.grade'
    _description = 'Grade'

    grade = fields.Char(string='Grade', required=True)
    date = fields.Date(string='Date', required=True)
    student_id = fields.Many2one('sms_module.student', string='Student', required=True)
    course_id = fields.Many2one('sms_module.course', string='Course', required=True)

class Attendance(models.Model):
    _name = 'sms_module.attendance'
    _description = 'Attendance'
    _sql_constraints = [
        ('unique_attendance', 'unique(attendance_date, student_id)', 'Attendance must be unique per student per day!')
    ]

    attendance_date = fields.Date(string='Attendance Date', required=True)
    status = fields.Selection([('present', 'Present'), ('absent', 'Absent')], string='Status', required=True)
    student_id = fields.Many2one('sms_module.student', string='Student', required=True)
    course_id = fields.Many2one('sms_module.course', string='Course', required=True)

