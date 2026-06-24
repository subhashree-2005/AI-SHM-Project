from reportlab.platypus import SimpleDocTemplate
from reportlab.platypus import Paragraph
from reportlab.platypus import Spacer

from reportlab.lib.styles import getSampleStyleSheet

from datetime import datetime


def generate_report(frequency, rms, status):

    # Create PDF
    pdf = SimpleDocTemplate("SHM_Report.pdf")

    styles = getSampleStyleSheet()

    elements = []

    # Title
    title = Paragraph(
        "Structural Health Monitoring Report",
        styles['Title']
    )

    elements.append(title)

    elements.append(Spacer(1, 20))

    # Time
    time_text = Paragraph(
        f"Generated At: {datetime.now()}",
        styles['BodyText']
    )

    elements.append(time_text)

    elements.append(Spacer(1, 20))

    # Frequency
    frequency_text = Paragraph(
        f"Frequency: {frequency} Hz",
        styles['BodyText']
    )

    elements.append(frequency_text)

    elements.append(Spacer(1, 10))

    # RMS
    rms_text = Paragraph(
        f"RMS Vibration: {rms}",
        styles['BodyText']
    )

    elements.append(rms_text)

    elements.append(Spacer(1, 10))

    # Status
    status_text = Paragraph(
        f"Structure Status: {status}",
        styles['BodyText']
    )

    elements.append(status_text)

    elements.append(Spacer(1, 20))

    # Final note
    note = Paragraph(
        "This report was generated using AI-based SHM system.",
        styles['Italic']
    )

    elements.append(note)

    # Build PDF
    pdf.build(elements)

    print("PDF Report Generated Successfully!")