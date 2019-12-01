# -*- coding: utf-8 -*-
# Copyright (c) 2019, Beshoy Atef and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from applications.utilites import update_status



class GMApplications(Document):
	def on_submit(self):
		update_status(self.manager_approved ,self.employee_applications)
