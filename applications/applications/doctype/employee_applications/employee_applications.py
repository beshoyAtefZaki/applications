# -*- coding: utf-8 -*-
# Copyright (c) 2019, Beshoy Atef and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from applications.utilites import create_manager_app , send_mail


class Employeeapplications(Document):
	
	def check_if_rejected(self):
		status_r = frappe.db.sql("""SELECT  is_rejected FROM `tabWorkflow State` WHERE workflow_state_name='%s' """ %self.workflow_state)
		return status_r[0][0]

	def add_rejected(self,rejected):
		sql = frappe.db.sql(""" UPDATE `tabEmployee applications` SET rejected_for = '%s' ,
						 rejected = 1 WHERE name = '%s' """ %(rejected,self.name))
		frappe.db.commit()
		return True



@frappe.whitelist()
def get_employee(usr):
	res = frappe.db.sql('''
		SELECT employee_name FROM `tabEmployee` WHERE employee = '%s'
		'''%usr, as_dict=1)

	return res
