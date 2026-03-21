import streamlit as st
import pandas as pd
import random
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

st.set_page_config(page_title="AI Ops Assessment | JDMC Services", layout="wide")

# This is your Root Link. It cannot 404 as long as your account is active.
BASE_URL = "https://calendly.com/jdmcservices"

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
    story.append(Paragraph(f"Book Strategy Review: {BASE_URL}", styles["BodyText"]))
    doc.build(story)
    buffer.seek(0)
    return buffer

# -----------------------------
# Main Dashboard
# -----------------------------
st.title("AI Operations Assessment Dashboard")
st.caption("JDMC Services LLC | Infrastructure Governance • Automation • Operational Risk")

# ROI Calculator
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

# Final CTA Section
st.markdown("## Finalize Your Executive Report")
colCTA1, colCTA2 = st.columns(2)

with colCTA1:
    st.write("### 📅 Book Executive Review")
    # POINTING TO THE ROOT PROFILE - BULLETPROOF
    st.link_button(
        label="🚀 Get Your Detailed Implementation Roadmap", 
        url=BASE_URL, 
        type="primary", 
        use_container_width=True
    )
    st.caption(f"Booking via: {BASE_URL}")

with colCTA2:
    st.write("### 📄 Download PDF Report")
    pdf = generate_executive_pdf("Large", "Healthcare", "Moderate", 80, 50, 45, 100000, 25000, [], [], roi_annual_loss, roi_potential_savings)
    st.download_button("Download Executive PDF Report", data=pdf, file_name="jdmc_roi_report.pdf", mime="application/pdf", use_container_width=True)

st.divider()
st.caption("© 2026 JDMC Services LLC")