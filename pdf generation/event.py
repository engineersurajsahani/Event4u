title = "Freshers Party Report"
event_name = "Freshers Party"
event_date = "February 20, 2023"
c_name="Suraj Sahani"
c_email="surajsahani@gmail.com"
c_department="Computer Engineering"
l=[c_name,c_email,c_department]
s=[1000,400,600]
b=[100000,40000,60000]
def pdf_generator(title,event_name,event_date,l,s,b):
    from reportlab.lib.pagesizes import letter
    from reportlab.pdfgen import canvas
    from reportlab.lib.styles import getSampleStyleSheet
    from reportlab.lib.units import inch
    from reportlab.platypus import Paragraph, Image, SimpleDocTemplate, Spacer, Table, TableStyle
    from reportlab.lib import colors

    # Create a new PDF object
    pdf = SimpleDocTemplate("event_report.pdf", pagesize=letter)

    # Define the styles for the document
    styles = getSampleStyleSheet()
    title_style = styles["Heading1"]
    subtitle_style = styles["Heading2"]
    text_style = styles["Normal"]

    # Define the data for the event report
    title = title
    event_name = event_name
    event_date = event_date
    coordinator = [["Coordinator Name", "Email", "Department"], l, ["Jagdish Sahani", "jagdishsahani@email.com", "Computer Engineering"]]
    budget = [["Budget", "Utilise Budget", "Balance Budget"],b]
    student = [["Total No. Of Students", "Present", "Absent"], s]
    summary = "The goal of the event is to help new students feel welcome and supported as they begin their college journey. It can be a great opportunity for new students to make new friends and connections, get involved in campus life, and learn about the resources available to them."

    # Add content to the PDF
    story = []
    logo = Image("ltcoe.png", width=2*inch, height=2*inch)  # Replace "logo.png" with your logo file name
    story.append(logo)
    story.append(Paragraph(title, title_style))
    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph("Event Details", subtitle_style))
    story.append(Paragraph(f"Event Name: {event_name}", text_style))
    story.append(Paragraph(f"Event Date: {event_date}", text_style))


    story.append(Spacer(1, 0.2 * inch))
    story.append(Paragraph("Coordinator", subtitle_style))
    table = Table(coordinator)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), (0,0,1)), ('TEXTCOLOR', (0, 0), (-1, 0), colors.lemonchiffon), ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, 0), 12), ('BOTTOMPADDING', (0, 0), (-1, 0), 12), ('BACKGROUND', (0, 1), (-1, -1), (0.95, 0.95, 0.95)), ('TEXTCOLOR', (0, 1), (-1, -1), (0, 0, 0)), ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'), ('FONTSIZE', (0, 1), (-1, -1), 10), ('ALIGN', (0, 1), (-1, -1), 'CENTER'), ('BOTTOMPADDING', (0, 1), (-1, -1), 6)]))
    story.append(table)

    story.append(Spacer(1, 0.2 * inch))

    story.append(Paragraph("Student", subtitle_style))
    table = Table(student)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), (0,0,1)), ('TEXTCOLOR', (0, 0), (-1, 0), colors.lemonchiffon), ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, 0), 12), ('BOTTOMPADDING', (0, 0), (-1, 0), 12), ('BACKGROUND', (0, 1), (-1, -1), (0.95, 0.95, 0.95)), ('TEXTCOLOR', (0, 1), (-1, -1), (0, 0, 0)), ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'), ('FONTSIZE', (0, 1), (-1, -1), 10), ('ALIGN', (0, 1), (-1, -1), 'CENTER'), ('BOTTOMPADDING', (0, 1), (-1, -1), 6)]))
    story.append(table)

    story.append(Spacer(1, 0.2 * inch))

    story.append(Paragraph("Budget", subtitle_style))
    table = Table(budget)
    table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), (0,0,1)), ('TEXTCOLOR', (0, 0), (-1, 0), colors.lemonchiffon), ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, 0), 12), ('BOTTOMPADDING', (0, 0), (-1, 0), 12), ('BACKGROUND', (0, 1), (-1, -1), (0.95, 0.95, 0.95)), ('TEXTCOLOR', (0, 1), (-1, -1), (0, 0, 0)), ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'), ('FONTSIZE', (0, 1), (-1, -1), 10), ('ALIGN', (0, 1), (-1, -1), 'CENTER'), ('BOTTOMPADDING', (0, 1), (-1, -1), 6)]))
    story.append(table)

    story.append(Paragraph("Summary", subtitle_style))
    story.append(Paragraph(summary, text_style))

    # Build the PDF document
    pdf.build(story)
