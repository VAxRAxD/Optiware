from django.http import JsonResponse, HttpResponse
from reportlab.lib.pagesizes import letter, A4
from reportlab.platypus import SimpleDocTemplate, Table, TableStyle, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from . models import *
import datetime
import json

def getInvoiceData(id):
    order_obj = Order.objects.get(id=id)
    data ={
        "Customer_name": order_obj.customer.name,
        "Invoice_amount": order_obj.amount,
        "Product_name": order_obj.product,
        "Order_quantity": order_obj.quantity,
        "Order_date": order_obj.ordered_date,
        "Delivery_date": order_obj.delivered_date,
        "Invoice_date": datetime.datetime.now()
        }
    # print(data)
    # return HttpResponse(json.dumps(data, default=str))
    return data

def downloadInvoicePdf(request, id):
    invoice_data = getInvoiceData(id)
    print(type(invoice_data))
    print(invoice_data)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice_{invoice_data['Customer_name']}.pdf"'
    
    doc = SimpleDocTemplate(response, pagesize=letter)
    styles = getSampleStyleSheet ()
    elements = [Paragraph("Invoice", styles['Heading1']),
                Paragraph(f"Company Name: Divine Enterprises", styles['Heading2']),
                Paragraph(f"Customer_name: {invoice_data['Customer_name']}", styles["Normal"]),
                Paragraph(f"Invoice_amount: {invoice_data['Invoice_amount']}", styles["Normal"]),
                Paragraph(f"Invoice_date: {invoice_data['Invoice_date']}", styles["Normal"]),
                Paragraph(f"Product_name: {invoice_data['Product_name']}", styles["Normal"]),
                Paragraph(f"Order_quantity: {invoice_data['Order_quantity']}", styles["Normal"]),
                Paragraph(f"Order_date: {invoice_data['Order_date']}", styles["Normal"]),
                Paragraph(f"Delivery_date: {invoice_data['Delivery_date']}", styles["Normal"])]

    # Add other fields from invoice_data to the PDF
    print("This is elements var ", elements)
    # Build the PDF document
    doc.build(elements)
    print(elements)
    return response