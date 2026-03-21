import streamlit as st
import pandas as pd
import random
from io import BytesIO
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet

st.set_page_config(page_title="AI Ops Assessment", layout="wide")

CALENDLY_URL = "https://calendly.com/jdmcservices/"

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
    recommendations
):
    buffer = BytesIO()
    doc = SimpleDocTemplate(buffer, pagesize=letter)
    styles = getSampleStyleSheet()
    story = []

    title = Paragraph(
        "JDMC Services Executive AI Operations Assessment Report",
        styles["Title"]
    )
    story.append(title)
    story.append(Spacer(1, 12))

    subtitle = Paragraph(
        "AI Productivity for Critical Infrastructure | Executive Summary Report",
        styles["Heading2"]
    )
    story.append(subtitle)
    story.append(Spacer(1, 18))

    profile_heading = Paragraph("Organization Profile", styles["Heading2"])
    story.append(profile_heading)
    story.append(Spacer(1, 6))

    profile_data = [
        ["Organization Size", org_size],
        ["Industry", industry],
        ["Automation Maturity", maturity]
    ]

    profile_table = Table(profile_data, colWidths=[180, 280])
    profile_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.whitesmoke),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
        ("PADDING", (0, 0), (-1, -1), 6)
    ]))
    story.append(profile_table)
    story.append(Spacer(1, 18))

    snapshot_heading = Paragraph("Executive KPI Snapshot", styles["Heading2"])
    story.append(snapshot_heading)
    story.append(Spacer(1, 6))

    kpi_data = [
        ["Average Health Score", str(avg_health)],
        ["Total Incidents", str(total_incidents)],
        ["Average Automation %", f"{avg_automation}%"],
        ["Total Cost Impact", f"${total_cost:,}"],
        ["Estimated Annual Savings", f"${estimated_savings:,}"]
    ]

    kpi_table = Table(kpi_data, colWidths=[220, 240])
    kpi_table.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.whitesmoke),
        ("GRID", (0, 0), (-1, -1), 0.5, colors.grey),
        ("FONTNAME", (0, 0), (-1, -1), "Helvetica"),
        ("PADDING", (0, 0), (-1, -1), 6)
    ]))
    story.append(kpi_table)
    story.append(Spacer(1, 18))

    summary_heading = Paragraph("Executive Summary", styles["Heading2"])
    story.append(summary_heading)
    story.append(Spacer(1, 6))

    if high_risk_systems:
        summary_text = (
            f"The environment reflects elevated operational exposure across the following high-risk systems: "
            f"{', '.join(high_risk_systems)}. Current performance indicates an average health score of "
            f"{avg_health}, with {total_incidents} total incidents and an average automation maturity of "
            f"{avg_automation}%. Based on current operating conditions, the estimated annual optimization "
            f"opportunity is ${estimated_savings:,}."
        )
    else:
        summary_text = (
            f"The environment is operating within acceptable thresholds, with an average health score of "
            f"{avg_health}, {total_incidents} total incidents, and average automation maturity of "
            f"{avg_automation}%. Based on current operating conditions, the estimated annual optimization "
            f"opportunity is ${estimated_savings:,}."
        )

    story.append(Paragraph(summary_text, styles["BodyText"]))
    story.append(Spacer(1, 18))

    rec_heading = Paragraph("Top Recommended Actions", styles["Heading2"])
    story.append(rec_heading)
    story.append(Spacer(1, 6))

    for rec in recommendations[:3]:
        story.append(Paragraph(f"• {rec}", styles["BodyText"]))
        story.append(Spacer(1, 6))

    story.append(Spacer(1, 12))

    closing_heading = Paragraph("JDMC Services Recommendation", styles["Heading2"])
    story.append(closing_heading)
    story.append(Spacer(1, 6))

    closing_text = (
        f"JDMC Services recommends initiating a structured AI Operations Optimization Engagement to capture "
        f"the identified ${estimated_savings:,} annual savings opportunity, reduce operational risk, and "
        f"improve enterprise-wide performance visibility. Engagement options include a 2-week rapid "
        f"assessment, a 30-day optimization roadmap, or a phased implementation program aligned to "
        f"executive priorities."
    )
    story.append(Paragraph(closing_text, styles["BodyText"]))
    story.append(Spacer(1, 18))

    cta_heading = Paragraph("Next Step", styles["Heading2"])
    story.append(cta_heading)
    story.append(Spacer(1, 6))

    cta_text = (
        f"Schedule an executive review with JDMC Services to validate findings, refine assumptions, and "
        f"develop a phased optimization strategy. Booking link: {CALENDLY_URL}"
    )
    story.append(Paragraph(cta_text, styles["BodyText"]))
    story.append(Spacer(1, 18))

    footer_heading = Paragraph("Contact", styles["Heading2"])
    story.append(footer_heading)
    story.append(Spacer(1, 6))
    story.append(Paragraph("JDMC Services | AI Productivity for Critical Infrastructure", styles["BodyText"]))
    story.append(Paragraph(CALENDLY_URL, styles["BodyText"]))

    doc.build(story)
    buffer.seek(0)
    return buffer


# -----------------------------
# Page Header
# -----------------------------
st.title("AI Operations Assessment Dashboard")
st.caption("JDMC Services LLC | AI Productivity for Critical Infrastructure")
st.subheader("Mission-Critical Healthcare Environment - Executive Intelligence")

# -----------------------------
# Assessment Inputs
# -----------------------------
st.markdown("## Assessment Inputs")

colA, colB, colC = st.columns(3)

with colA:
    org_size = st.selectbox(
        "Organization Size",
        ["Small", "Medium", "Large", "Enterprise"]
    )

with colB:
    industry = st.selectbox(
        "Industry",
        ["Healthcare", "Finance", "Government", "Enterprise IT"]
    )

with colC:
    maturity = st.selectbox(
        "Automation Maturity",
        ["Low", "Moderate", "High"]
    )

st.markdown("---")

# -----------------------------
# Dynamic Behavior
# -----------------------------
if maturity == "Low":
    automation_floor = 10
    automation_ceiling = 50
elif maturity == "Moderate":
    automation_floor = 30
    automation_ceiling = 70
else:
    automation_floor = 60
    automation_ceiling = 90

systems = ["Network", "Telecom", "Security", "Helpdesk", "Cloud"]
data = []

for system in systems:
    incidents = random.randint(5, 25)
    automation = random.randint(automation_floor, automation_ceiling)
    health = random.randint(60, 95)
    cost = incidents * random.randint(500, 2000)

    risk = (
        (100 - health) * 0.5 +
        incidents * 2 +
        (100 - automation) * 0.3
    )

    data.append({
        "System": system,
        "Health Score": health,
        "Incidents": incidents,
        "Automation %": automation,
        "Cost Impact ($)": cost,
        "Risk Score": int(risk)
    })

df = pd.DataFrame(data)

# -----------------------------
# Risk Classification
# -----------------------------
def classify_risk(score):
    if score > 80:
        return "Critical"
    elif score > 60:
        return "High"
    elif score > 40:
        return "Moderate"
    else:
        return "Low"

df["Risk Level"] = df["Risk Score"].apply(classify_risk)

# -----------------------------
# Data Table
# -----------------------------
st.dataframe(df, width="stretch")

# -----------------------------
# KPI Metrics
# -----------------------------
col1, col2, col3, col4 = st.columns(4)

avg_health = int(df["Health Score"].mean())
total_incidents = int(df["Incidents"].sum())
avg_automation = int(df["Automation %"].mean())
total_cost = int(df["Cost Impact ($)"].sum())

col1.metric("Avg Health", avg_health)
col2.metric("Total Incidents", total_incidents)
col3.metric("Avg Automation %", avg_automation)
col4.metric("Total Cost Impact", f"${total_cost:,}")

# -----------------------------
# Estimated Savings
# -----------------------------
st.markdown("## Estimated Savings Opportunity")

automation_gap = (100 - df["Automation %"].mean()) / 100
incident_reduction = df["Incidents"].mean() * 0.15
estimated_savings = int(total_cost * 0.25 * automation_gap)

colS1, colS2, colS3 = st.columns(3)

colS1.metric("Optimization Potential", f"{int(automation_gap * 100)}%")
colS2.metric("Incident Reduction (Est.)", f"{int(incident_reduction)} incidents")
colS3.metric("Estimated Annual Savings", f"${estimated_savings:,}")

st.info(
    "Estimated savings are derived from automation uplift, reduced incident volume, "
    "and operational efficiency improvements aligned with AI-driven transformation."
)

# -----------------------------
# Executive Summary
# -----------------------------
st.markdown("## Executive Summary")

high_risk_df = df[df["Risk Score"] > 60]
high_risk_systems = high_risk_df["System"].tolist()

if high_risk_systems:
    st.error(f"High Risk Systems Identified: {', '.join(high_risk_systems)}")
else:
    st.success("All systems operating within acceptable thresholds")

st.markdown("### Operational Insight")
st.write(
    f"The environment shows an average system health score of {avg_health} with "
    f"{total_incidents} total incidents. Automation levels indicate opportunity "
    f"for efficiency gains and cost reduction across multiple domains."
)

# -----------------------------
# Risk Chart
# -----------------------------
st.markdown("## Risk Overview")
st.bar_chart(df.set_index("System")["Risk Score"])

# -----------------------------
# Recommendations
# -----------------------------
st.markdown("## Recommended Actions (Prioritized)")

df_sorted = df.sort_values(by="Risk Score", ascending=False)
recommendations = []

for _, row in df_sorted.iterrows():
    if row["Risk Level"] == "Critical":
        text = (
            f"{row['System']}: Immediate remediation required. Recommend incident reduction "
            f"and automation deployment."
        )
        recommendations.append(text)
        st.error(text)
    elif row["Risk Level"] == "High":
        text = (
            f"{row['System']}: High operational risk. Focus on process automation and "
            f"monitoring improvements."
        )
        recommendations.append(text)
        st.warning(text)
    elif row["Risk Level"] == "Moderate":
        text = (
            f"{row['System']}: Optimization opportunity. Improve efficiency and reduce "
            f"manual workflows."
        )
        recommendations.append(text)
        st.info(text)
    else:
        text = f"{row['System']}: Stable and optimized."
        recommendations.append(text)
        st.success(text)

# -----------------------------
# Lead Capture + Scheduling
# -----------------------------
st.markdown("---")
st.markdown("## Request AI Optimization Assessment")

name = st.text_input("Full Name")
email = st.text_input("Business Email")
company = st.text_input("Organization Name")

st.markdown("### Next Step: Executive Review")
st.link_button("Schedule Executive Review", CALENDLY_URL)

st.markdown("#### Or request follow-up")

if st.button("Request Executive Assessment"):
    if name and email:
        st.success(
            f"Thank you {name}. JDMC Services will contact you to review your "
            f"estimated ${estimated_savings:,} annual optimization opportunity."
        )
    else:
        st.warning("Please complete required fields.")

# -----------------------------
# PDF Download
# -----------------------------
st.markdown("## Download Executive Report")

pdf_file = generate_executive_pdf(
    org_size=org_size,
    industry=industry,
    maturity=maturity,
    avg_health=avg_health,
    total_incidents=total_incidents,
    avg_automation=avg_automation,
    total_cost=total_cost,
    estimated_savings=estimated_savings,
    high_risk_systems=high_risk_systems,
    recommendations=recommendations
)

st.download_button(
    label="Download Executive PDF Report",
    data=pdf_file,
    file_name="jdmc_services_executive_ai_ops_assessment.pdf",
    mime="application/pdf"
)

st.caption("Book directly with JDMC Services to review findings and discuss next-step optimization strategy.")
import streamlit as st

st.header("💰 Automation ROI Calculator")
st.write("Calculate how much manual processes are currently costing your organization.")

# 1. Inputs - Use columns for a clean UI
col1, col2 = st.columns(2)

with col1:
    employees = st.number_input("Number of employees affected", min_value=1, value=10)
    avg_hourly_rate = st.number_input("Average hourly rate ($)", min_value=15, value=45)

with col2:
    hours_lost_per_week = st.number_input("Hours lost to manual tasks/week (per person)", min_value=1, value=5)
    automation_potential = st.slider("Target automation percentage (%)", 10, 100, 70)

# 2. Calculation Logic
weekly_loss = employees * hours_lost_per_week * avg_hourly_rate
annual_loss = weekly_loss * 52
potential_savings = annual_loss * (automation_potential / 100)

# 3. The "Executive Hook" Visuals
st.divider()
st.subheader("Your Annual Operational Leak")
st.error(f"### ${annual_loss:,.0f} / year")

st.success(f"### Potential Recoverable Revenue: ${potential_savings:,.0f}")

st.info(f"**Coach's Note:** This represents {hours_lost_per_week * employees * 52:,.0f} hours that could be redirected to high-value revenue growth.")

# 4. The Closing CTA
if st.button("Get Your Detailed Implementation Roadmap"):
    st.write("Redirecting to JDMC Services Strategy Booking...")
    # Link this to your Calendly
    st.markdown(f'<a href="YOUR_CALENDLY_LINK" target="_blank">Click here to book your 15-minute Diagnosis</a>', unsafe_allow_stdio=True)