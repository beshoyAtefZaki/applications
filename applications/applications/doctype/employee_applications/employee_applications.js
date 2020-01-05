// Copyright (c) 2019, Beshoy Atef and contributors
// For license information, please see license.txt

frappe.ui.form.on('Employee applications', {
	application_type:function(frm){
		var type = frm.doc.application_type
		if (type == "Accounting Application"){

				frm.set_value("ap_status" ,"Processing To Accounting")
		}		else {
				frm.set_value("ap_status" , "Processing To HR")
		}

	},
	employee :  function(frm) {
    var employee = frm.doc.employee ;
    frappe.call({
    method:'applications.applications.doctype.employee_applications.employee_applications.get_employee',
    args: {
      'usr'  : employee
    } ,
    callback: function(r){
				frm.set_value("employee_name" ,r.message[0].employee_name)
			}



})
	}
});
