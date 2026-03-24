import streamlit as st
import pandas as pd
import random
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

# --- BROWSER CONFIGURATION ---
st.set_page_config(
    page_title="Healthcare Infra & AI-Ops ROI | JDMC Services", 
    layout="wide",
    page_icon="📊"
)

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
    
    # Executive Branding in PDF
    story.append(Paragraph("JDMC Services: Healthcare Infrastructure & AI-Ops ROI Report", styles["Title"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph("Strategic Assessment for Infrastructure Modernization & Operational Efficiency", styles["Heading2"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph(f"Current Estimated Annual Operational Leak: ${roi_annual_loss:,.0f}", styles["BodyText"]))
    story.append(Paragraph(f"Target Recoverable ROI: ${roi_potential_savings:,.0f}", styles["BodyText"]))
    story.append(Spacer(1, 12))
    story.append(Paragraph(f"Book Infrastructure Strategy Review: {BASE_URL}", styles["BodyText"]))
    
    doc.build(story)
    buffer.seek(0)
    return buffer

# -----------------------------
# Main Dashboard
# -----------------------------
st.title("Healthcare Infrastructure & AI-Ops ROI Evaluator")
st.caption("JDMC Services LLC | Infrastructure Governance • Telecom Orchestration • Operational Efficiency")

# ROI Calculator Container
with st.container(border=True):
    st.header("💰 Infrastructure & Automation ROI Calculator")
    st.markdown("""
    Use this tool to quantify the impact of manual workflows across your IT, Telecom, and Clinical Operations.
    """)
    
    colROI1, colROI2 = st.columns(2)
    
    with colROI1:
        employees = st.number_input(
            "Staff affected (IT, Telecom, or Ops)", 
            min_value=1, 
            value=15,
            help="Number of employees performing manual or repetitive tasks."
        )
        avg_hourly_rate = st.number_input(
            "Avg fully burdened hourly rate ($)", 
            min_value=15, 
            value=45,
            help="Include benefits and overhead in this hourly figure."
        )
        
    with colROI2:
        hours_lost = st.number_input(
            "Inefficiency hours lost per week", 
            min_value=1, 
            value=13,
            help="Average time spent per staff member on manual triage, updates, or legacy workflows."
        )
        auto_pct = st.slider(
            "Target Efficiency Gain (%)", 
            min_value=10, 
            max_value=100, 
            value=27,
            help="Percentage of tasks that can be optimized via AI Orchestration and Automation."
        )

    # Calculations
    roi_annual_loss = employees * hours_lost * avg_hourly_rate * 52
    roi_potential_savings = roi_annual_loss * (auto_pct / 100)

    st.divider()
    
    colM1, colM2 = st.columns(2)
    colM1.error(f"### Annual Operational Leak: ${roi_annual_loss:,.0f}")
    colM2.success(f"### Potential Recoverable ROI: ${roi_potential_savings:,.0f}")

st.divider()

# Final CTA Section
st.markdown("## Finalize Your Executive Report")
colCTA1, colCTA2 = st.columns(2)

with colCTA1:
    st.write("### 📅 Book Infrastructure Strategy Review")
    st.link_button(
        label="🚀 Get Your Implementation Roadmap", 
        url=BASE_URL, 
        type="primary", 
        use_container_width=True
    )
    st.caption(f"Secure booking via: {BASE_URL}")

with colCTA2:
    st.write("### 📄 Generate PDF Assessment")
    # Mock data passed to PDF generator based on inputs
    pdf = generate_executive_pdf(
        "Standard", "Healthcare", "Emerging", 80, 50, auto_pct, 100000, 
        roi_potential_savings, [], [], roi_annual_loss, roi_potential_savings
    )
    st.download_button(
        label="Download PDF Executive Summary", 
        data=pdf, 
        file_name="jdmc_infrastructure_roi_assessment.pdf", 
        mime="application/pdf", 
        use_container_width=True
    )

st.divider()
st.caption("© 2026 JDMC Services LLC | Empowering Healthcare IT through AI Orchestration")
