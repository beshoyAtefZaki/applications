from __future__ import unicode_literals
from frappe import _
import frappe


def get_data():
	return  [
		{
    "label": _("Applications"),
    "items": [
      {
        "type": "doctype",
        "name": "Employee applications",
        "description": _("Employee applications."),
		"onboard": 1,
      },
	 
      ],



    	},
	]
