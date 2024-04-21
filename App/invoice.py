from django.http import JsonResponse, HttpResponse
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph
from reportlab.lib.styles import getSampleStyleSheet
from . models import *
import datetime

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
    return data

def downloadInvoicePdf(request, id):
    invoice_data = getInvoiceData(id)
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = f'attachment; filename="invoice.pdf'
    custom_page_width = 5 * inch
    custom_page_height = 4.5 * inch
    doc = SimpleDocTemplate(response, pagesize=(custom_page_width, custom_page_height))
    styles = getSampleStyleSheet ()
    elements = []
    elements.append(Paragraph("Invoice", styles['Heading1']))
    elements.append(Paragraph("Company Name: Divine Enterprises", styles['Heading2']))
    elements.append(Paragraph(f"Customer Name: {invoice_data['Customer_name']}", styles["Normal"]))
    elements.append(Paragraph(f"Invoice Amount: {invoice_data['Invoice_amount']}", styles["Normal"]))
    elements.append(Paragraph(f"Invoice Date: {invoice_data['Invoice_date']}", styles["Normal"]))
    elements.append(Paragraph(f"Product Name: {invoice_data['Product_name']}", styles["Normal"]))
    elements.append(Paragraph(f"Order Quantity: {invoice_data['Order_quantity']}", styles["Normal"]))
    elements.append(Paragraph(f"Order Date: {invoice_data['Order_date']}", styles["Normal"]))
    elements.append(Paragraph(f"Delivery Date: {invoice_data['Delivery_date']}", styles["Normal"]))
    doc.build(elements)
    return response