# -*- coding: utf-8 -*-
# Copyright (c) 2019, Beshoy Atef and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Employeeapplications(Document):
		def on_submit(self):
			create_manager_app("Manager applications" ,self.employee , self.employee_name , self.status ,
								self.applications , self.attachment)



def create_manager_app(docname, employee , em_name , status , applications,attachment):
	doc               = frappe.new_doc(docname)
	doc.employee      = employee
	doc.employee_name = em_name
	doc.status        = status
	doc.applications = applications
	doc.attachment    = attachment
	doc.insert(ignore_permissions=True)
	doc.save()
	frappe.db.commit()
@frappe.whitelist()
def get_employee(usr):
	res = frappe.db.sql('''
		SELECT name, employee_name FROM `tabEmployee` WHERE user_id = '%s'
		'''%usr, as_dict=1)
	for i in res :
		return (i)
	return None
