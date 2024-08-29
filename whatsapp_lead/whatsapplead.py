from __future__ import unicode_literals
import frappe, erpnext

def addlead(self, method):
    ldoc = frappe.new_doc('Lead')    
    ldoc.first_name=self.get('from')
    ldoc.whatsapp_no=self.get('from')
    ldoc.status='Lead'    
    ldoc.message_id=self.get('message_id') 
    ldoc.text_xgyf=self.get('message')
    #ldoc.text_wsik=self.get('message')
    frappe.msgprint('inside hook')
    ldoc.save(ignore_permissions=True)
   
    



    
    
