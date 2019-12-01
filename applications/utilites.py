# -*- encoding: utf-8 -*-
import frappe
import smtplib






def create_manager_app(docname, application, employee , em_name , status , applications,attachment):
    doc               = frappe.new_doc(docname)
    doc.employee      =  employee
    doc.employee_applications = application
    doc.employee_name = em_name
    doc.ap_status        = status
    doc.applications = applications
    doc.attachment    = attachment
    doc.insert(ignore_permissions=True)
    doc.save()
    frappe.db.commit()


def create_gm_app(docname, application, employee , em_name , status , refrence ,refrence_type,applications,attachment):
    doc                       = frappe.new_doc(docname)
    doc.employee              =  employee
    doc.employee_applications = application
    doc.employee_name         = em_name
    doc.ap_status             = status
    doc.applications          = applications
    doc.attachment            = attachment
    doc.refrence              = refrence
    doc.refrence_type         = refrence_type
    doc.insert(ignore_permissions=True)
    doc.save()
    frappe.db.commit()





def update_status(approved , application):

	res = frappe.db.sql('''
		UPDATE `tabEmployee applications`
		SET ap_status='%s' WHERE name = '%s'
		'''%(approved,application))



def send_mail(subjec , name):
    gmail_user = 'alqimmacompany2020@gmail.com'
    gmail_password = 'mbtykzqbetlucizn'

    sent_from = gmail_user
    to = ['beshoyatef31@gmail.com']
    # subject =str(sub) + ":" + str(employee)
    # body = 'Hey, what'
    # body =  subjec.encode('utf-8')
    subject = ("your request has been created ")
    body = "Application %s  has been created  "%name
    email_text = """\
    From: %s
    To: %s
    Subject: %s

    %s
    """ % (sent_from, ", ".join(to), subject,body)

    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()

        print ('Email sent!')
    except:
        print ('Something went wrong...')
