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
	   {
         "type": "doctype",
         "name": "Manager applications",
         "description": _("Employee applications."),
 		"onboard": 1,
       },
	    {
		  "type": "doctype",
		  "name": "Executive manager",
		  "description": _("Employee applications."),
	   "onboard": 1,
		},
	    {
          "type": "doctype",
          "name": "Financial manager",
          "description": _("Employee applications."),
  		"onboard": 1,
        },

		 {
           "type": "doctype",
           "name": "G M Applications",
           "description": _("Employee applications."),
   			"onboard": 1,
         },
      ],



    	},
	]
