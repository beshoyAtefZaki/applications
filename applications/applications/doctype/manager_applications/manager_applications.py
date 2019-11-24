# -*- coding: utf-8 -*-
# Copyright (c) 2019, Beshoy Atef and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document
from employee_applications import create_manager_app
class Managerapplications(Document):

	def on_submit(self):
		create_manager_app("Financial manager",self.employee , self.employee_name , self.status ,
							self.applications , self.attachment)
