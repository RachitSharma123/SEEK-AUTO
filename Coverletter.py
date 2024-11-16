from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch

def create_cover_letter(content, filename="cover_letter.pdf"):
    # Set up the canvas with A4 size and custom margins
    c = canvas.Canvas(filename, pagesize=A4)
    width, height = A4

    # Define margins and boundary width
    margin = 0.5 * inch  # Small margin on all sides
    boundary_width = 5  # Width of the side boundaries

    # Draw boundaries
    c.setStrokeColorRGB(0, 0, 0)  # Black boundary color
    c.setLineWidth(boundary_width)
    c.line(margin, margin, margin, height - margin)  # Left boundary
    c.line(width - margin, margin, width - margin, height - margin)  # Right boundary

    # Adjust text starting position
    text_x = margin + boundary_width + 10
    text_y = height - margin - 50

    # Set font and font size
    c.setFont("Helvetica", 12)

    # Add the cover letter content
    text = c.beginText(text_x, text_y)
    text.setLeading(14)  # Set line spacing

    # Insert the content line by line
    for line in content.splitlines():
        text.textLine(line)

    # Draw the text on the canvas
    c.drawText(text)

    # Save the PDF
    c.save()
    print(f"Cover letter created as '{filename}'")

# Example content to be included
content = """ XXX 
                XXX
                XXX
                XXX
                XXX
                    """

# Create the cover letter
create_cover_letter(content)
