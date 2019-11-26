# -*- coding: utf-8 -*-
# Copyright (c) 2019, Beshoy Atef and contributors
# For license information, please see license.txt
#use
from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from applications.utilites import create_manager_app

class Managerapplications(Document):
	# def validate(self):
	# 	update_status(self.ap_status ,self.employee_applications  )
	def on_submit(self):

		if self.manager_approved =='Approved' :
			self.ap_status = "Processing"
			update_status(self.ap_status, self.employee_applications)
			create_manager_app("Executive manager",self.employee_applications ,self.employee , self.employee_name , self.ap_status ,
								self.applications , self.attachment)

			# create_manager_app("Executive manager", self.name , self.employee , self.employee_name ,self.ap_status  ,
			# 				self.applications , self.attachment)







def update_status(approved , application):

	res = frappe.db.sql('''
		UPDATE `tabEmployee applications`
		SET ap_status='%s' WHERE name = '%s'
		'''%approved,application)
