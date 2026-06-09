import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Devansh Mishra",
    page_icon="📈",
    layout="wide"
)

with open("style.css") as f:
    st.markdown(
        f"<style>{f.read()}</style>",
        unsafe_allow_html=True
    )

img = Image.open("profile.jpg")

col1,col2 = st.columns([1,2])

with col1:
    st.image(img,use_container_width=True)

with col2:
    st.markdown("""
    <div class='hero-title'>
    DEVANSH MISHRA
    </div>
    """,unsafe_allow_html=True)

    st.markdown("""
    <div class='hero-sub'>
    MBA Graduate | Business Development | Sales Analytics | Market Intelligence
    </div>
    """,unsafe_allow_html=True)

    st.write("📍 Indore, Madhya Pradesh")
    st.write("📧 mishradevansh987@gmail.com")
    st.write("📞 +91 6264262302")
    st.write("🔗 www.linkedin.com/in/devansh-mishra-mbdo7")

st.divider()

st.markdown(
"""
<div class='section-title'>
About Me
</div>
""",
unsafe_allow_html=True
)

st.write("""
MBA Graduate specializing in Marketing and Operations with practical experience in sales forecasting, dealership engagement, market analysis, and business intelligence. During my internship at Volvo Eicher Commercial Vehicles, I worked across sales, planning, procurement, and after-sales functions to support commercial decision-making and demand planning.
""")

st.divider()

st.markdown(
"""
<div class='section-title'>
Impact Snapshot
</div>
""",
unsafe_allow_html=True
)

c1,c2,c3,c4 = st.columns(4)

with c1:
    st.markdown("""
    <div class='metric-box'>
    <h2>3</h2>
    Plants Analyzed
    </div>
    """,unsafe_allow_html=True)

with c2:
    st.markdown("""
    <div class='metric-box'>
    <h2>30+</h2>
    Inventory Lines
    </div>
    """,unsafe_allow_html=True)

with c3:
    st.markdown("""
    <div class='metric-box'>
    <h2>2</h2>
    Analytics Projects
    </div>
    """,unsafe_allow_html=True)

with c4:
    st.markdown("""
    <div class='metric-box'>
    <h2>1</h2>
    Automotive Internship
    </div>
    """,unsafe_allow_html=True)

st.divider()

st.markdown("""
<div class='section-title'>
Experience
</div>
""",unsafe_allow_html=True)

st.markdown("""
<div class='card'>
<h3>Sales & Marketing Intern</h3>
<b>Volvo Eicher Commercial Vehicles Ltd.</b><br>
June 2025 – August 2025

<ul>
<li>Built HDT forecasting models.</li>
<li>Conducted dealership and channel visits.</li>
<li>Prepared sales MIS reports.</li>
<li>Analyzed competitor activities.</li>
<li>Supported inventory planning decisions.</li>
<li>Worked with Sales, Planning, Procurement and After-Sales teams.</li>
</ul>
</div>
""",unsafe_allow_html=True)

st.divider()

st.markdown("""
<div class='section-title'>
Featured Project
</div>
""",unsafe_allow_html=True)

st.markdown("""
<div class='card'>
<h3>Commercial Vehicle Forecasting & Alternative Fuel Analysis</h3>

<ul>
<li>PESTEL Analysis</li>
<li>HDT Forecasting</li>
<li>LNG Adoption Analysis</li>
<li>CNG Penetration Analysis</li>
<li>EV Impact Assessment</li>
<li>Industry Volume Forecasting</li>
</ul>
</div>
""",unsafe_allow_html=True)

st.markdown("""
<div class='card'>
<h3>Adidas Sales Analytics Dashboard</h3>

Analyzed:
<ul>
<li>Retail Performance</li>
<li>Regional Sales Trends</li>
<li>Product Category Profitability</li>
<li>Operating Margins</li>
<li>Channel Performance</li>
</ul>
</div>
""",unsafe_allow_html=True)

st.divider()

st.markdown("""
<div class='section-title'>
Skills
</div>
""",unsafe_allow_html=True)

col1,col2,col3 = st.columns(3)

with col1:
    st.markdown("""
    **Analytics**
    - Excel
    - Tableau
    - Power BI
    - Dashboarding
    """)

with col2:
    st.markdown("""
    **Business**
    - Sales Forecasting
    - Market Research
    - Territory Planning
    - Business Analysis
    """)

with col3:
    st.markdown("""
    **Professional**
    - Communication
    - Stakeholder Management
    - Problem Solving
    - Presentations
    """)

st.divider()

st.markdown("""
<div class='section-title'>
Education
</div>
""",unsafe_allow_html=True)

st.write("""
**MBA (Marketing & Operations)**  
Prestige Institute of Management and Research  
Sept 2024 – May 2026
""")

st.write("""
**BBA (Analytics & Finance)**  
Prestige Institute of Management and Research  
Sept 2021 – July 2024
""")

st.divider()

st.markdown("""
<div class='section-title'>
Leadership & Volunteering
</div>
""",unsafe_allow_html=True)

st.write("""
• Volunteer – Documentary Making Competition (Mathan, PIMR)

• Volunteer – Cyclothon
""")

st.divider()

st.markdown("""
### Let's Connect

📧 mishradevansh987@gmail.com

📱 6264262302

🔗 LinkedIn: www.linkedin.com/in/devansh-mishra-mbdo7
""")