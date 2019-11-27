import frappe







def create_manager_app(docname, application, employee , em_name , status , applications,attachment):
    doc               = frappe.new_doc(docname)
    doc.employee      =  employee
    doc.employee_applications = application
    doc.employee_name = em_name
    doc.ap_status        = status
    doc.applications = applications
    doc.attachment    = attachment
    doc.insert(ignore_permissions=True)
    doc.save()
    frappe.db.commit()




def update_status(approved , application):

	res = frappe.db.sql('''
		UPDATE `tabEmployee applications`
		SET ap_status='%s' WHERE name = '%s'
		'''%(approved,application))
