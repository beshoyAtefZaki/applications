import frappe







def create_manager_app(docname,applications, employee , em_name , status , applications,attachment):
	doc               = frappe.new_doc(docname)
	doc.employee      = employee
    self.employee_applications = applications
	doc.employee_name = em_name
	doc.status        = status
	doc.applications = applications
	doc.attachment    = attachment
	doc.insert(ignore_permissions=True)
	doc.save()
	frappe.db.commit()
