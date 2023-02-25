from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle

# Create a new PDF object
pdf = SimpleDocTemplate("event_report.pdf", pagesize=letter)

# Define the styles for the document
styles = getSampleStyleSheet()
title_style = styles["Heading1"]
subtitle_style = styles["Heading2"]
text_style = styles["Normal"]

# Define the data for the event report
title = "Annual Event Report"
event_name = "ABC Annual Event"
event_date = "January 1, 2023"
attendees = [["Name", "Email", "Company"], ["John Doe", "johndoe@email.com", "ABC Inc."], ["Jane Smith", "janesmith@email.com", "XYZ Corp"]]
summary = "Lorem ipsum dolor sit amet, consectetur adipiscing elit. Sed sed risus vitae quam commodo sollicitudin. Morbi quis turpis vel eros commodo auctor sit amet vel justo."

# Add content to the PDF
story = []
story.append(Paragraph(title, title_style))
story.append(Spacer(1, 0.2 * inch))
story.append(Paragraph("Event Details", subtitle_style))
story.append(Paragraph(f"Event Name: {event_name}", text_style))
story.append(Paragraph(f"Event Date: {event_date}", text_style))
story.append(Spacer(1, 0.2 * inch))
story.append(Paragraph("Attendees", subtitle_style))
table = Table(attendees)
table.setStyle(TableStyle([('BACKGROUND', (0, 0), (-1, 0), (0.8, 0.8, 0.8)), ('TEXTCOLOR', (0, 0), (-1, 0), (0, 0, 0)), ('ALIGN', (0, 0), (-1, -1), 'CENTER'), ('FONTNAME', (0, 0), (-1, 0), 'Helvetica-Bold'), ('FONTSIZE', (0, 0), (-1, 0), 12), ('BOTTOMPADDING', (0, 0), (-1, 0), 12), ('BACKGROUND', (0, 1), (-1, -1), (0.95, 0.95, 0.95)), ('TEXTCOLOR', (0, 1), (-1, -1), (0, 0, 0)), ('FONTNAME', (0, 1), (-1, -1), 'Helvetica'), ('FONTSIZE', (0, 1), (-1, -1), 10), ('ALIGN', (0, 1), (-1, -1), 'CENTER'), ('BOTTOMPADDING', (0, 1), (-1, -1), 6)]))
story.append(table)
story.append(Spacer(1, 0.2 * inch))
story.append(Paragraph("Summary", subtitle_style))
story.append(Paragraph(summary, text_style))

# Build the PDF document
pdf.build(story)
