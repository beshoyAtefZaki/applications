import frappe







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
