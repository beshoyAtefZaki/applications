from __future__ import unicode_literals
import frappe

def get_notification_config():
    notifications =  { "for_doctype":
        {"Employee applications": {'ap_status':'Waiting'},
        "Manager applications":{"manager_approved":"Waiting"}}



    }
    # doctype = [d for d in notifications.get('for_doctype')]
    # for doc in frappe.get_all('DocType',fields= ["name"], filters = {"name": ("not in", doctype), 'is_submittable': 1}):
	# 	     notifications["for_doctype"][doc.name] = {"docstatus": 0}
    #
    #
    #
    return notifications
