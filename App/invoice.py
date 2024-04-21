from django.http import JsonResponse, HttpResponse
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Table, TableStyle, Spacer
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
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
    doc = SimpleDocTemplate(response, pagesize=(custom_page_width, custom_page_height),
                            leftMargin=30,
                            rightMargin=20,
                            topMargin=20,
                            bottomMargin=20)
    
    title_style = ParagraphStyle(
            name='TitleStyle',
            fontSize=22,
            textColor=colors.darkgoldenrod,
            leading=30,  # line spacing
            fontName="Helvetica-Bold",
            background=colors.lightcoral
    )

    styles = getSampleStyleSheet ()
    elements = []
    elements.append(Paragraph("Divine Enterprises Invoice", title_style))
    elements.append(Spacer(1, 2))
    elements.append(Paragraph(f"Order ID: {id}", styles["Heading2"]))
    elements.append(Spacer(1, 10))
    elements.append(Paragraph(f"Customer Name: {invoice_data['Customer_name']}", styles["Normal"]))
    elements.append(Spacer(1, 2))
    elements.append(Paragraph(f"Invoice Amount: {invoice_data['Invoice_amount']}", styles["Normal"]))
    elements.append(Spacer(1, 2))
    elements.append(Paragraph(f"Invoice Date: {invoice_data['Invoice_date']}", styles["Normal"]))
    elements.append(Spacer(1, 2))
    elements.append(Paragraph(f"Product Name: {invoice_data['Product_name']}", styles["Normal"]))
    elements.append(Spacer(1, 2))
    elements.append(Paragraph(f"Order Quantity: {invoice_data['Order_quantity']}", styles["Normal"]))
    elements.append(Spacer(1, 2))
    #     ["Customer Name", invoice_data['Customer_name']],
    #     ["Invoice Amount", invoice_data['Invoice_amount']],
    #     ["Invoice Date", invoice_data['Invoice_date']],
    #     ["Product Name", invoice_data['Product_name']],
    #     ["Order Quantity", invoice_data['Order_quantity']],
    #     ["Order Date", invoice_data['Order_date']],
    #     ["Delivery Date", invoice_data['Delivery_date']],
    # ]

    # # Create table
    # table = Table(data)
    # table.setStyle(TableStyle([
    #     ('BACKGROUND', (0, 0), (-1, 0), colors.grey),
    #     ('TEXTCOLOR', (0, 0), (-1, 0), colors.whitesmoke),
    #     ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
    #     ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'),
    #     ('BOTTOMPADDING', (0, 0), (-1, 0), 12),
    #     ('BACKGROUND', (0, 1), (-1, -1), colors.beige),
    #     ('GRID', (0, 0), (-1, -1), 1, colors.black)
    # ]))
    # elements.append(table)

    doc.build(elements)
    return response