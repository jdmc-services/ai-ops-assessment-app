import streamlit as st
import pandas as pd
import random
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

st.set_page_config(page_title="AI Ops Assessment | JDMC Services", layout="wide")

# Base URL for your Calendly
CALENDLY_URL = "https://calendly.com/jdmcservices"

# -----------------------------
# PDF Generator
# -----------------------------
def generate_executive_pdf(
    org_size,
    industry,
    maturity,
    avg_health,
    total_incidents,
    avg_automation,
    total_cost,
    estimated_savings,
    high_risk_systems,
    recommendations,
    roi_annual_loss,
    roi_potential_savings
):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("JDMC Services Executive AI Operations Assessment", styles["Title"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Financial Impact Summary", styles["Heading2"]))
    roi_data = [
        ["Annual Operational Leak (Manual Tasks)", f"${roi_annual_loss:,}"],
        ["Potential Recoverable Revenue", f"${roi_potential_savings:,}"]
    ]
    roi_table = Table(roi_data, colWidths=[250, 200])
    roi_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.whitesmoke),
        ("TEXTCOLOR", (1, 0), (1, 0), colors.red),
        ("TEXTCOLOR", (1, 1), (1, 1), colors.green),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica-Bold"),
        ("PADDING", (0, 0), (-1, -1), 8)
    ]))
    story.append(roi_table)
    story.append(Spacer(1, 20))

    story.append(Paragraph("System Health Snapshot", styles["Heading2"]))
    kpi_data = [
        ["Avg Health Score", str(avg_health)],
        ["Total Incidents", str(total_incidents)],
        ["Automation Maturity", f"{avg_automation}%"],
        ["Total Cost Impact", f"${total_cost:,}"]
    ]
    kpi_table = Table(kpi_data, colWidths=[200, 250])
    kpi_table.setStyle(TableStyle([
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("PADDING", (0, 0), (-1, -1), 6)
    ]))
    story.append(kpi_table)
    
    story.append(Spacer(1, 20))
    story.append(Paragraph("Next Steps", styles["Heading2"]))
    # Fixed URL logic for PDF
    story.append(Paragraph(f"Schedule your 15-minute Strategy Diagnosis at: {CALENDLY_URL.rstrip('/')}/15min", styles["BodyText"]))

    doc.build(story)
    buffer.seek(0)
    return buffer

# -----------------------------
# Header
# -----------------------------
st.title("AI Operations Assessment Dashboard")
st.caption("JDMC Services LLC | Infrastructure Governance • Automation • Operational Risk")

# -----------------------------
# ROI Calculator (The Hook)
# -----------------------------
st.container(border=True)
st.header("💰 Automation ROI Calculator")
st.write("Calculate the financial impact of manual process 'leakage' in your organization.")

colROI1, colROI2 = st.columns(2)
with colROI1:
    employees = st.number_input("Number of employees affected", min_value=1, value=15)
    avg_hourly_rate = st.number_input("Average hourly rate ($)", min_value=15, value=45)
with colROI2:
    hours_lost_per_week = st.number_input("Hours lost to manual tasks/week (per person)", min_value=1, value=13)
    automation_potential = st.slider("Target automation percentage (%)", 10, 100, 27)

roi_annual_loss = employees * hours_lost_per_week * avg_hourly_rate * 52
roi_potential_savings = roi_annual_loss * (automation_potential / 100)

colM1, colM2 = st.columns(2)
colM1.error(f"### Annual Operational Leak\n## ${roi_annual_loss:,.0f}")
colM2.success(f"### Potential Recoverable Revenue\n## ${roi_potential_savings:,.0f}")

# -----------------------------
# Assessment Inputs
# -----------------------------
st.divider()
st.markdown("## Infrastructure Assessment")
colA, colB, colC = st.columns(3)
with colA:
    org_size = st.selectbox("Organization Size", ["Small", "Medium", "Large", "Enterprise"])
with colB:
    industry = st.selectbox("Industry", ["Healthcare", "Finance", "Government", "Enterprise IT"])
with colC:
    maturity = st.selectbox("Automation Maturity", ["Low", "Moderate", "High"])

# -----------------------------
# Logic & Data Generation
# -----------------------------
systems = ["Network", "Telecom", "Security", "Helpdesk", "Cloud"]
data = []
for system in systems:
    health = random.randint(60, 95)
    incidents = random.randint(5, 25)
    automation = random.randint(30, 80)
    cost = incidents * random.randint(500, 2000)
    risk = ((100 - health) * 0.5 + incidents * 2 + (100 - automation) * 0.3)
    data.append({"System": system, "Health Score": health, "Incidents": incidents, "Automation %": automation, "Cost Impact ($)": cost, "Risk Score": int(risk)})

df = pd.DataFrame(data)
avg_health = int(df["Health Score"].mean())
total_incidents = int(df["Incidents"].sum())
avg_automation = int(df["Automation %"].mean())
total_cost = int(df["Cost Impact ($)"].sum())
estimated_savings = int(total_cost * 0.25)
high_risk_systems = df[df["Risk Score"] > 60]["System"].tolist()

# -----------------------------
# Results Display
# -----------------------------
st.dataframe(df, use_container_width=True)

col1, col2, col3, col4 = st.columns(4)
col1.metric("Avg Health", avg_health)
col2.metric("Total Incidents", total_incidents)
col3.metric("Avg Automation %", avg_automation)
col4.metric("Total Cost Impact", f"${total_cost:,}")

st.divider()

# -----------------------------
# Final Call to Action
# -----------------------------
st.markdown("## Finalize Your Executive Report")
colCTA1, colCTA2 = st.columns(2)

with colCTA1:
    st.write("### 📅 Book Executive Review")
    
    # FIXED LOGIC: Ensure exactly one slash between URL and 15min
    full_calendly_path = f"{CALENDLY_URL.rstrip('/')}/15min"
    
    st.link_button(
        label="🚀 Get Your Detailed Implementation Roadmap", 
        url=full_calendly_path, 
        type="primary", 
        use_container_width=True
    )
    st.caption(f"Redirecting to: {full_calendly_path}")

with colCTA2:
    st.write("### 📄 Download PDF Report")
    pdf_file = generate_executive_pdf(
        org_size, industry, maturity, avg_health, total_incidents, 
        avg_automation, total_cost, estimated_savings, high_risk_systems, 
        ["Implement Zero-Trust Automation", "Harden Telecom Resiliency", "Optimize Helpdesk Workflows"],
        roi_annual_loss, roi_potential_savings
    )
    st.download_button(
        label="Download Executive PDF Report",
        data=pdf_file,
        file_name="jdmc_services_roi_assessment.pdf",
        mime="application/pdf",
        use_container_width=True
    )

st.divider()
st.caption("© 2026 JDMC Services LLC. Mission-critical focus. Governance-first.")