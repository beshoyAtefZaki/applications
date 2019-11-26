from __future__ import unicode_literals
from frappe import _
from frappe.desk.moduleview import add_setup_section

def get_data():
	data =[
		{
		"label": _("Settings"),
	    "icon": "fa fa-wrench",
	    "items": [
	      {
	        "type": "doctype",
	        "name": "Employee applications",
	        "label": _("Employee applications"),
	        "description": _("Employee applications."),
	        "hide_count": True,
	        "settings": 1,
			}
			]
			}
			]

	return data
