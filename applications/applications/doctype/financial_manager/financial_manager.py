# -*- coding: utf-8 -*-
# Copyright (c) 2019, Beshoy Atef and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from applications.utilites import create_gm_app ,update_status


class Financialmanager(Document):
	def on_submit(self):
		if self.manager_approved == "Approved":
			if self.g_m_approved == 1:
				create_gm_app("G M Applications",self.employee_applications ,
									self.employee , self.employee_name , "Approved" ,
									self.refrence ,self.refrence_type ,
									self.applications , self.attachment)

			if self.g_m_approved == 0:
				status ="Approved"
				update_status(status ,self.employee_applications)
		if self.manager_approved == "Rejected":
			status ="Rejected"
			update_status(status ,self.employee_applications)
