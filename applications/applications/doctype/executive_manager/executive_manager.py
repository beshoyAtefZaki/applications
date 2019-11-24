# -*- coding: utf-8 -*-
# Copyright (c) 2019, Beshoy Atef and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
# import frappe
from frappe.model.document import Document

from employee_applications.employee_applications import employee_applications.create_manager_app
class Executivemanager(Document):
	def on_submit(self):
		create_manager_app("Financial manager",self.employee , self.employee_name , self.status ,
							self.applications , self.attachment)


def create_manager_app(employee , em_name , status , applications,attachment):
	doc               = frappe.new_doc("Manager applications")
	doc.employee      = employee
	doc.employee_name = em_name
	doc.status        = status
	doc.applications = applications
	doc.attachment    = attachment
	doc.insert(ignore_permissions=True)
	doc.save()
	frappe.db.commit()
