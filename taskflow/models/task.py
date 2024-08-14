# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError
import logging


_logger = logging.getLogger(__name__)

class Task(models.Model):
    _name="taskflow.task"
    _description = "Task"

# ---------------------------------------------------------------------------------
# FIELDS
# ---------------------------------------------------------------------------------


    name = fields.Char(
        string="Task Name",
    )
    description = fields.Text(
        string="Description"
    )
    start_date = fields.Date(
        string="Start Date", 
        required=True
    )
    end_date = fields.Date(
        string="End Date", 
        required=True
    )
    duration = fields.Integer(
        string="Duration", 
        compute="_compute_duration", 
        store=True
    )
    state = fields.Selection([
        ('draft', 'Draft'),
        ('progress', 'In Progress'),
        ('completed', 'Completed'),
        ('cancel', 'Cancelled')
    ], string='State', default='draft', readonly=True)

# ---------------------------------------------------------------------------------
# METHODS
# ---------------------------------------------------------------------------------

    # Duration is calculated based on start_date and end_date
    @api.depends('start_date', 'end_date')
    def _compute_duration(self):
        for task in self:
            if task.start_date and task.end_date: 
                if task.end_date >= task.start_date:
                    task.duration = (task.end_date - task.start_date).days
                else:
                    raise ValidationError(_("End date must be greater than start date"))
    
    # Method to change the state of the task to 'In Progress'
    @api.model
    def create(self, vals):
        vals['state'] = 'progress'
        vals['name'] = self.env['ir.sequence'].next_by_code('taskflow.task')
        task = super(Task, self).create(vals)
        return task

    # Method to change the state of the task to 'Completed'
    def action_complete(self):
        self.state = 'completed'
    
    # Method to change the state of the task to 'Cancelled'
    def action_cancel(self):
        self.state = 'cancel'


