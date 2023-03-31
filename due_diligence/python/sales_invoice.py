import frappe
from due_diligence.due_diligence.doctype.due_diligence.due_diligence import send_email_due_diligence

def send_email(doc, event):
    send_email_due_diligence(
        send_to=frappe.db.get_single_value("Due Diligence Settings","sent_to_email"),
        email_template="",
        contact_person="",
        quotation=doc.name,
        source_doctype=doc.doctype
    ) 