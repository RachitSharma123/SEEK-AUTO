from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, HRFlowable
import os

# Define the file path
output_directory = r"C:\Users\rachi\Downloads\resume\UPDATED"
filename = "Rachit_SDResume.pdf"
output_path = os.path.join(output_directory, filename)

# Ensure the directory exists
os.makedirs(output_directory, exist_ok=True)

# Delete previous file if exists
if os.path.exists(output_path):
    os.remove(output_path)

# PDF setup with minimal margins
pdf = SimpleDocTemplate(output_path, pagesize=A4, leftMargin=2, rightMargin=2, topMargin=2, bottomMargin=2)

# Define styles with reduced font size
styles = getSampleStyleSheet()
header_style = ParagraphStyle('Header', parent=styles['Heading1'], fontSize=14, alignment=1, spaceAfter=8)
subheader_style = ParagraphStyle('Subheader', parent=styles['Heading2'], fontSize=12, spaceAfter=6, fontName="Helvetica-Bold", alignment=0)
body_style = ParagraphStyle('Body', parent=styles['Normal'], fontSize=9, leading=10, spaceAfter=6, alignment=0)
centered_body_style = ParagraphStyle('CenteredBody', parent=styles['Normal'], fontSize=9, leading=10, spaceAfter=6, alignment=1)
bullet_style = ParagraphStyle('Bullet', parent=styles['BodyText'], bulletIndent=10, fontSize=9, leading=10)

# Content List
elements = []

# Header Section
elements.append(Paragraph("RACHIT SHARMA", header_style))
elements.append(Paragraph("Passionate Software Developer", centered_body_style))
elements.append(Paragraph("📧 xxx | 📞 xxx", centered_body_style))
elements.append(Paragraph("LinkedIn: linkedin.com/in/rachit-sharma-0b9b44117", centered_body_style))
elements.append(HRFlowable(width="100%", thickness=1, color=colors.black, spaceBefore=6, spaceAfter=6))

# Career Objective
elements.append(Paragraph("Career Objective", subheader_style))
career_objective_text = (
    "Ambitious software developer with a strong foundation in Java, .NET, JavaScript, SQL, and C# and experience in full-stack development and backend integration. "
    "Seeking a challenging role in a dynamic team to apply technical skills and contribute to impactful projects, with a vision to grow as a technology expert and problem solver."
)
elements.append(Paragraph(career_objective_text, body_style))
elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.grey, spaceBefore=10, spaceAfter=10))

# Key Skills Summary
elements.append(Paragraph("Key Skills Summary", subheader_style))
skills = [
    "<b>Programming Languages:</b> Java, JavaScript, C#, Python, C++, PHP, ASP.NET, SQL, HTML, CSS",
    "<b>Frameworks & Technologies:</b> .NET Core, RESTful API, Bootstrap, MVC, DevOps",
    "<b>Database Management:</b> SQL Server, MongoDB, PostgreSQL",
    "<b>AI & Machine Learning:</b> Prompt Engineering, Open-source AI Server Maintenance",
    "<b>Tools & Platforms:</b> AWS, Docker, GitHub, Jira, Agile Methodologies"
]
for skill in skills:
    elements.append(Paragraph(f"• {skill}", bullet_style))
elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.grey, spaceBefore=10, spaceAfter=10))

# Education (always includes Master's degree from MIT)
elements.append(Paragraph("Education", subheader_style))
elements.append(Paragraph("<b>Master of Business Analytics</b>", body_style))
elements.append(Paragraph("Melbourne Institute of Technology, Mar 2023 - Present", body_style))
elements.append(Spacer(1, 6))
elements.append(Paragraph("<b>Bachelor of Computer Science Engineering</b>", body_style))
elements.append(Paragraph("S.R.M. University, India, Mar 2015 - Nov 2019", body_style))
elements.append(Paragraph("Special Interest: Web Development", body_style))
elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.grey, spaceBefore=10, spaceAfter=10))

# Professional Experience
elements.append(Paragraph("Professional Experience", subheader_style))
experience = [
    {
        "title": "Software Developer",
        "company": "Office Choice",
        "location": "Melbourne, VIC",
        "dates": "Jan 2024 – Oct 2024",
        "responsibilities": [
            "Provided comprehensive technical support and maintenance for server and client-side applications, improving uptime and efficiency.",
            "Developed documentation and troubleshooting guides to enhance support consistency across the team.",
            "Assisted in configuring network and endpoint security, promoting a secure IT environment."
        ]
    },
    {
        "title": "Software Developer",
        "company": "Quinnox (Client: Kotak Mahindra Bank)",
        "location": "Bangalore, India",
        "dates": "Jan 2020 - Dec 2022",
        "responsibilities": [
            "Managed upgrade of Calypso from version 14.0.1 to 16.0.59, enhancing API functionality and streamlining client operations.",
            "Implemented and maintained custom-client code updates, ensuring compatibility with the upgraded Calypso libraries.",
            "Developed and monitored DevOps pipelines for streamlined code deployment and service management within the client’s distributed architecture."
        ]
    },
    {
        "title": "Software Intern",
        "company": "MIT Melbourne",
        "location": "Melbourne, VIC",
        "dates": "Jul 2023 – Nov 2023",
        "responsibilities": [
            "Collaborated within an Agile team to develop .NET applications using C#, .NET Core, and MVC frameworks, enhancing web application functionality and performance.",
            "Implemented test-driven development (TDD) strategies, including unit testing, to ensure reliable and scalable code.",
            "Engaged in frontend development using HTML, CSS, JavaScript, and Bootstrap to create intuitive, responsive user interfaces."
        ]
    }
]

for job in experience:
    # Job Title, Company, Location, and Dates in Bold
    elements.append(Paragraph(f"<b>{job['title']}</b> – {job['company']}, {job['location']} ({job['dates']})", body_style))
    # Responsibilities as bullet points
    for responsibility in job["responsibilities"]:
        elements.append(Paragraph(f"• {responsibility}", bullet_style))
    elements.append(Spacer(1, 8))
elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.grey, spaceBefore=10, spaceAfter=10))

# Certifications
elements.append(Paragraph("Certifications", subheader_style))
certifications = [
    "AWS Concepts - Udemy | 2020",
    "Python Programming - Udemy | 2020",
    "SQL Fundamentals (Oracle 11g) - NIIT Limited | 2017",
    "Blockchain Essentials - Udemy | 2018"
]
for cert in certifications:
    elements.append(Paragraph(f"• {cert}", bullet_style))
elements.append(HRFlowable(width="100%", thickness=0.5, color=colors.grey, spaceBefore=10, spaceAfter=10))

# References
elements.append(Paragraph("References", subheader_style))
references = [
    " "
]
for ref in references:
    elements.append(Paragraph(f"• {ref}", bullet_style))

# Function to add border on each page
def add_border(canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.black)
    canvas.setLineWidth(1)
    canvas.rect(5, 5, A4[0] - 10, A4[1] - 10)
    canvas.restoreState()

# Generate the PDF with the custom border
pdf.build(elements, onFirstPage=add_border, onLaterPages=add_border)
print("PDF created successfully at", output_path)
