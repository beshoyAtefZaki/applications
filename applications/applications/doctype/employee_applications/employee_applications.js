// Copyright (c) 2019, Beshoy Atef and contributors
// For license information, please see license.txt

frappe.ui.form.on('Employee applications', {
	onload: function(frm) {
    var employee = frappe.session.user ;
    frappe.call({
    method:'applications.applications.doctype.employee_applications.employee_applications.get_employee',
    args: {
      'usr'  : employee
    } ,
    callback: function(r){

			frm.set_value("employee" ,r.message.name)
			frm.set_value("employee_name" ,r.message.employee_name)
				// frm.set_value("employee" ,r.message)

      // frm.set_value("contratc_end_date" ,r.message)
    }


})
},
	employee :  function(frm) {
    var employee = frm.doc.employee ;
		// var empl = frappe.session.user
		// var em = frappe.get_doc("Employee" ,employee)
    frappe.call({
    method:'applications.applications.doctype.employee_applications.employee_applications.get_employee',
    args: {
      'usr'  : employee
    } ,
    callback: function(r){
			if (r.messgae){
				frm.set_value("employee" ,r.message.name)
				frm.set_value("employee_name" ,r.message.employee_name)
			}
    }


})
	}
});
