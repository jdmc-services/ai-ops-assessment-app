import streamlit as st
import pandas as pd
import random
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

st.set_page_config(page_title="AI Ops Assessment | JDMC Services", layout="wide")

# THE CONSTANT - Hardcoded to ensure no string math errors
TARGET_LINK = "https://calendly.com/jdmcservices/15min"

# -----------------------------
# PDF Generator
# -----------------------------
def generate_executive_pdf(
    org_size, industry, maturity, avg_health, total_incidents, 
    avg_automation, total_cost, estimated_savings, high_risk_systems, 
    recommendations, roi_annual_loss, roi_potential_savings
):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    story.append(Paragraph("JDMC Services Executive AI Operations Assessment", styles["Title"]))
    story.append(Spacer(1, 12))

    story.append(Paragraph("Financial Impact Summary", styles["Heading2"]))
    roi_data = [
        ["Annual Operational Leak (Manual)", f"${roi_annual_loss:,}"],
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

    story.append(Paragraph("Next Steps", styles["Heading2"]))
    story.append(Paragraph(f"Book Strategy Review: {TARGET_LINK}", styles["BodyText"]))

    doc.build(story)
    buffer.seek(0)
    return buffer

# -----------------------------
# App Layout
# -----------------------------
st.title("AI Operations Assessment Dashboard")
st.caption("JDMC Services LLC | Infrastructure Governance • Automation • Operational Risk")

st.container(border=True)
st.header("💰 Automation ROI Calculator")
colROI1, colROI2 = st.columns(2)
with colROI1:
    employees = st.number_input("Employees affected", min_value=1, value=15)
    avg_hourly_rate = st.number_input("Avg hourly rate ($)", min_value=15, value=45)
with colROI2:
    hours_lost = st.number_input("Hours lost/week", min_value=1, value=13)
    auto_pct = st.slider("Target automation %", 10, 100, 27)

roi_annual_loss = employees * hours_lost * avg_hourly_rate * 52
roi_potential_savings = roi_annual_loss * (auto_pct / 100)

colM1, colM2 = st.columns(2)
colM1.error(f"### Annual Leak: ${roi_annual_loss:,.0f}")
colM2.success(f"### Recoverable: ${roi_potential_savings:,.0f}")

st.divider()
st.markdown("## Infrastructure Assessment")
colA, colB, colC = st.columns(3)
with colA: org_size = st.selectbox("Org Size", ["Small", "Medium", "Large", "Enterprise"])
with colB: industry = st.selectbox("Industry", ["Healthcare", "Finance", "Government", "Enterprise IT"])
with colC: maturity = st.selectbox("Maturity", ["Low", "Moderate", "High"])

systems = ["Network", "Telecom", "Security", "Helpdesk", "Cloud"]
data = []
for system in systems:
    health, incidents, automation = random.randint(60, 95), random.randint(5, 25), random.randint(30, 80)
    cost = incidents * random.randint(500, 2000)
    risk = int((100 - health) * 0.5 + incidents * 2 + (100 - automation) * 0.3)
    data.append({"System": system, "Health": health, "Incidents": incidents, "Auto %": automation, "Cost": cost, "Risk": risk})

df = pd.DataFrame(data)
st.dataframe(df, use_container_width=True)

st.divider()
st.markdown("## Finalize Your Executive Report")
colCTA1, colCTA2 = st.columns(2)

with colCTA1:
    st.write("### 📅 Book Executive Review")
    # HARDCODED LINK
    st.link_button(
        label="🚀 Get Your Detailed Implementation Roadmap", 
        url=TARGET_LINK, 
        type="primary", 
        use_container_width=True
    )
    # DEBUG LINE: Click this to see if the link itself is the problem
    st.write(f"Link Debug: [Click here to test manually]({TARGET_LINK})")

with colCTA2:
    st.write("### 📄 Download PDF Report")
    pdf = generate_executive_pdf(org_size, industry, maturity, 80, 50, 45, 100000, 25000, [], [], roi_annual_loss, roi_potential_savings)
    st.download_button("Download Executive PDF Report", data=pdf, file_name="jdmc_roi_report.pdf", mime="application/pdf", use_container_width=True)

st.caption("© 2026 JDMC Services LLC")