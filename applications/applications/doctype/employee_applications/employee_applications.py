# -*- coding: utf-8 -*-
# Copyright (c) 2019, Beshoy Atef and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from applications.utilites import create_manager_app , send_mail


class Employeeapplications(Document):
	
	

	def comments_view (self):
		
		sql = frappe.db.sql("""SELECT  creation ,modified_by,content   FROM `tabComment` WHERE reference_name='%s'  AND comment_type = 'Workflow' """%self.name)
		
		table = '<table class="table table-bordered"> <tr> <th>User</th> <th>time</th><th>Action</th></tr>'
		cels = ''
		self.set('action_table', [])
		for i in sql :
			te =str(i[2])
			trans = frappe.db.sql("""SELECT  target_name FROM `tabTranslation` WHERE source_name = '%s' """%te)
			if trans :
				te = trans[0][0]
			if str(i[1]) =='Administrator' :

				cels += '<tr> <td> '+str(i[1])+'</td> <td>'+str(i[0]) +'</td> <td>'+te +'</td> </tr>'
			
			else :
				user_l = frappe.db.sql("SELECT full_name FROM `tabUser` WHERE email='%s' "% str(i[1]))
				
				cels += '<tr> <td> '+str(user_l[0][0])+'</td> <td>'+str(i[0]) +'</td> <td>' +te +'</td> </tr>'
			


		html_table = table + cels +'</table>'
		

		return (html_table)
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
