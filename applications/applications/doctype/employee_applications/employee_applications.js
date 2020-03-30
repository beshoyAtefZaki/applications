// Copyright (c) 2019, Beshoy Atef and contributors
// For license information, please see license.txt

frappe.ui.form.on('Employee applications', {
	onload:function(frm){
		if(frm.doc.attachment){
			var f = frm.doc.attachment;
			var text = '<a href=" ' +f.toString() + ' " target="_blank">Perview File </a>' 
			frm.set_df_property('code', 'options', [text])
		 	frm.refresh_field("code")

		}
		if (frm.doc.__islocal){
		frm.set_value("to" ,"G M manager" ) }
	},
		refresh:function(frm){
		return frappe.call({
				doc: frm.doc,
				method : 'check_if_rejected',
				callback:function(r){
					if (r.message == 1 && frm.doc.rejected == 0) {

						frappe.prompt([
   				 {'fieldname': 'rejected', 'fieldtype': 'Small Text', 'label': 'Rejected Reason', 'reqd': 1}  
					],
							function(values){
							  // frm.set_value("rejected_for" ,values.rejected)
							  // frm.set_value("rejected" , 1)
							  // frm.update()
							 frappe.call({
							 	doc: frm.doc,
							 	method : 'add_rejected',
							 	args :{
							 		"rejected":values.rejected
							 	},
							 	callback:function(r){
							 		frm.refresh_field("rejected_for")
							 		frm.set_value("rejected" , 1)
							 		frm.refresh()
							 	
							 	}

							 }) 

  									
							},
							'Rejected Reason',
							'Save'
					)




					}
					}
					
				})
		} ,
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
	},
	attachment:function(frm){
		var f = frm.doc.attachment;
		console.log(f.toString())
		var text = '<a href=" ' +f.toString() + ' ">Perview File </a>' ;
		console.log(text)
		frm.set_value("code" , text);
		 frm.set_df_property('code', 'options', [text])
		 frm.refresh_field("code")

	}

});
