




frappe.listview_settings['Employee applications'] = {
	add_fields: ["ap_status"],
	get_indicator: function(doc) {
		if(  doc.ap_status == "Rejected") {
			return [__(("Rejected")), "red", "ap_status,=,Rejected"];
		}else if(doc.ap_status == "Processing") {
      	return [__(("Processing")), "orange", "ap_status,=,Processing"];
    }
    else if(doc.ap_status == "Waiting") {
      	return [__(("Waiting")), "darkgrey", "ap_status,=,Waiting"];
    }
    else if(doc.ap_status == "Approved") {
        return [__(("Approved")), "green", "ap_status,=,Approved"];
    }
	}
};
