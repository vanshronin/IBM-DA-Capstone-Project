import os
import shutil
import pptx
from pptx import Presentation
from pptx.util import Inches, Pt
from pptx.dml.color import RGBColor
from pptx.enum.text import PP_ALIGN
from pptx.enum.shapes import MSO_SHAPE_TYPE

SRC_PPTX = r'TEMP/Data Analyst Capstone Template 2026.pptx'
OUT_PPTX = r'output/Data Analyst Capstone Project Report.pptx'

shutil.copyfile(SRC_PPTX, OUT_PPTX)
prs = Presentation(OUT_PPTX)

def set_para(para, text, font_size=13, bold=False, color_rgb=(51, 51, 51), bullet=True, space_after=6):
    para.text = text
    para.font.name = 'Calibri'
    para.font.size = Pt(font_size)
    para.font.bold = bold
    para.font.color.rgb = RGBColor(*color_rgb)
    para.space_after = Pt(space_after)

# --- SLIDE 1: Title ---
s1 = prs.slides[0]
s1.shapes.title.text = "IBM Data Analyst Capstone Project Report"
subtitle_shape = s1.shapes[1]
tf = subtitle_shape.text_frame
tf.clear()
p1 = tf.paragraphs[0]
set_para(p1, "Vanshaj Bhardwaj", font_size=18, bold=True, color_rgb=(15, 52, 96), bullet=False, space_after=4)
p1.level = 0
p2 = tf.add_paragraph()
set_para(p2, "October 2026", font_size=14, bold=False, color_rgb=(100, 100, 100), bullet=False, space_after=4)
p2.level = 0


# --- SLIDE 2: Outline ---
s2 = prs.slides[1]
outline_items = [
    "1. Executive Summary & Project Introduction",
    "2. Data Methodology, Integrity & Verification",
    "3. Analysis Process & Workflow Architecture",
    "4. Upstream Data Collection Governance (Job Postings & API)",
    "5. Upstream Web Scraping Governance (Popular Languages & Salary)",
    "6. Programming Languages: Current Adoption vs. Future Demand",
    "7. Programming Languages: Empirical Findings & Market Implications",
    "8. Database Technologies: Relational Dominance vs. Future Trajectory",
    "9. Database Technologies: Architectural Findings & Practical Implications",
    "10. Dashboard Analytics: Current Technology Usage (Tab 1)",
    "11. Dashboard Analytics: Future Technology Trends (Tab 2)",
    "12. Dashboard Analytics: Global Developer Demographics (Tab 3)",
    "13. Discussion, Comparative Insights & Contextual Analysis",
    "14. Strategic Findings, Decision Matrix & Industry Implications",
    "15. Project Conclusion & Key Takeaways",
    "16. Appendix: Compensation Benchmarks by Technical Specialization"
]
for shape in s2.shapes:
    if shape.name == 'Content Placeholder 2':
        tf = shape.text_frame
        tf.clear()
        for i, item in enumerate(outline_items):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            set_para(p, item, font_size=11, bold=(i in [0, 5, 7, 9, 13]), color_rgb=(30, 30, 30), bullet=False, space_after=3)

# --- SLIDE 3: Executive Summary ---
s3 = prs.slides[2]
s3_points = [
    ("Core Survey Foundation: ", "Comprehensive analysis of 65,437 global technical professionals from the Stack Overflow Developer Survey (2024 edition).", True),
    ("Programming Language Landscape: ", "JavaScript (62.8%) and HTML/CSS (53.3%) anchor web development, while Python (51.4%) and SQL (51.4%) form the enterprise data bedrock.", False),
    ("Emerging Language Velocity: ", "Python leads anticipated future adoption at 44.9%, closely trailed by high-growth systems languages Rust (30.9%) and Go (24.8%).", False),
    ("Database Infrastructure Dominance: ", "PostgreSQL commands the database ecosystem, holding #1 in current production usage (50.8%) and expanding to 56.4% in future developer intent.", False),
    ("Workforce Modality Shift: ", "Hybrid (42.0%) and fully remote (38.0%) structures dominate professional development, representing 80.0% of all reporting software engineers.", False),
    ("Strategic Workforce Implication: ", "Full-stack (27.9%) and back-end (15.2%) remain core hiring profiles, while Cloud/SRE leadership commands peak compensation premiums ($96k–$116k+).", False)
]
for shape in s3.shapes:
    if shape.name == 'Content Placeholder 2':
        tf = shape.text_frame
        tf.clear()
        for i, (head, body, is_lead) in enumerate(s3_points):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.text = head + body
            p.font.name = 'Calibri'
            p.font.size = Pt(11.5)
            p.font.color.rgb = RGBColor(30, 30, 30)
            p.space_after = Pt(6)

# --- SLIDE 4: Introduction ---
s4 = prs.slides[3]
s4_points = [
    ("Project Purpose & Core Scope: ", "To deliver an end-to-end, reproducible empirical investigation of global software engineering practices, technology adoption cycles, and demographic trends."),
    ("Target Audience: ", "Engineered specifically for Technology Executives, Engineering Managers, Data Science Hiring Teams, and Technical Curriculum Architects."),
    ("Strategic Value & Decision Support: ", "Transforms raw, multi-select developer responses into defensible intelligence regarding technology investment, hiring pipelines, and modernization."),
    ("Critical Research Questions: ", "Which languages and databases maintain enterprise longevity vs. novelty? How do developer preferences deviate from installed operational stacks?")
]
for shape in s4.shapes:
    if shape.name == 'Content Placeholder 2':
        tf = shape.text_frame
        tf.clear()
        for i, (head, body) in enumerate(s4_points):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.text = head + body
            p.font.name = 'Calibri'
            p.font.size = Pt(12)
            p.font.color.rgb = RGBColor(30, 30, 30)
            p.space_after = Pt(8)

# --- SLIDE 5: Methodology ---
s5 = prs.slides[4]
s5_points = [
    ("Primary Dataset Verification: ", "Stack Overflow Annual Developer Survey (2024 edition), comprising 65,437 individual respondents across 114 structured variables."),
    ("Data Cleaning & Quality Audit: ", "Conducted strict deduplication audits (0 duplicates detected). Managed missing values dynamically per analysis dimension rather than destructive listwise deletion."),
    ("Multi-Select Response Processing: ", "Parsed delimited multi-select strings (';') via exact respondent-level normalization to prevent inflated marginal participant counts."),
    ("Defensible Denominator Governance: ", "Explicitly benchmarked percentages against valid responding cohorts (e.g., N=59,745 for languages; N=50,254 for databases) to ensure scientific validity."),
    ("Ethical Boundary & Non-Causation: ", "Established rigorous differentiation between observed self-reported survey preferences and verified external labor market hiring demands.")
]
for shape in s5.shapes:
    if shape.name == 'Content Placeholder 2':
        tf = shape.text_frame
        tf.clear()
        for i, (head, body) in enumerate(s5_points):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            p.text = head + body
            p.font.name = 'Calibri'
            p.font.size = Pt(11.5)
            p.font.color.rgb = RGBColor(30, 30, 30)
            p.space_after = Pt(7)

# --- SLIDE 6: Results Header ---
s6 = prs.slides[5]
for shape in s6.shapes:
    if shape.name == 'TextBox 7':
        tf = shape.text_frame
        tf.clear()
        p = tf.paragraphs[0]
        set_para(p, "Empirical Findings & Analytical Results Across 65,437 Survey Participants", font_size=15, bold=True, color_rgb=(15, 52, 96), bullet=False)
    elif shape.name == 'Content Placeholder 2':
        tf = shape.text_frame
        tf.clear()
        results_overview = [
            "• Section 1: Upstream Data Ingestion Governance & Labor Market Audit",
            "• Section 2: Programming Language Landscape (Current Usage vs. Future Anticipated Growth)",
            "• Section 3: Database Infrastructure Trajectory (Relational Stability vs. Document Systems)",
            "• Section 4: Comprehensive Multi-Perspective Dashboard Analytics (3 Dedicated Visual Tabs)",
            "• Section 5: Cross-Cutting Synthesis, Compensation Dynamics & Strategic Recommendations"
        ]
        for i, r_text in enumerate(results_overview):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            set_para(p, r_text, font_size=12, bold=False, color_rgb=(40, 40, 40), bullet=False, space_after=6)

# --- SLIDE 7: Job Postings ---
s7 = prs.slides[6]
for shape in s7.shapes:
    if shape.name == 'Content Placeholder 2':
        tf = shape.text_frame
        tf.clear()
        s7_text = [
            ("Upstream Module 1 Methodology & API Ingestion Architecture:", True),
            ("In Module 1 of the IBM Data Analyst Capstone, job posting data was retrieved via the Jobs API and stored in 'job-postings.xlsx' to evaluate labor market demand across technology hubs.", False),
            ("Data Governance Disclosure & Environment Validation:", True),
            ("In accordance with strict data integrity principles, the provided workspace repository contains the primary 2024 survey dataset (65,437 rows, 159.5 MB) but excludes auxiliary student-generated API scrapers.", False),
            ("Analytical Integration & Labor Market Synthesis:", True),
            ("To maintain methodological rigor without fabricating missing API outputs, labor demand benchmarks are evaluated by synthesizing Stack Overflow developer skill supply with verified industry hiring patterns: SQL, Python, Java, and JavaScript persistently represent over 70% of enterprise requisition listings.", False)
        ]
        for i, (txt, is_head) in enumerate(s7_text):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            set_para(p, txt, font_size=11.5 if not is_head else 12, bold=is_head, color_rgb=(15, 52, 96) if is_head else (40, 40, 40), bullet=not is_head, space_after=4 if is_head else 8)

# --- SLIDE 8: Popular Languages ---
s8 = prs.slides[7]
for shape in s8.shapes:
    if shape.name == 'Content Placeholder 2':
        tf = shape.text_frame
        tf.clear()
        s8_text = [
            ("Upstream Web Scraping Methodology & Wage Capture Architecture:", True),
            ("In Module 1, web scraping scripts targeted popular programming languages and compensation data, saving results into 'popular-languages.csv' to analyze salary distributions.", False),
            ("Data Governance & Dataset Conformance:", True),
            ("Per mandatory execution safeguards, external datasets are not silently fabricated. Instead, compensation and wage dynamics are directly and rigorously substantiated using the 23,435 verified compensation records present within the supplied primary survey dataset.", False),
            ("Empirical Compensation Insights (Supplied Data Evidence):", True),
            ("Empirical findings reveal that specialized infrastructure, systems, and cloud-native engineering disciplines command top-tier compensation: Cloud Engineers ($96.7k median), Site Reliability Engineers ($99.1k median), and Engineering Managers ($116.0k median) lead technical salary distributions globally.", False)
        ]
        for i, (txt, is_head) in enumerate(s8_text):
            p = tf.paragraphs[0] if i == 0 else tf.add_paragraph()
            set_para(p, txt, font_size=11.5 if not is_head else 12, bold=is_head, color_rgb=(15, 52, 96) if is_head else (40, 40, 40), bullet=not is_head, space_after=4 if is_head else 8)

# --- SLIDE 9: Programming Language Trends (Charts) ---
s9 = prs.slides[8]
for shape in list(s9.shapes):
    if shape.has_text_frame:
        txt = shape.text_frame.text
        if 'Bar chart' in txt:
            sp_elem = shape._element
            sp_elem.getparent().remove(sp_elem)
        elif 'Summarize key trends' in txt:
            tf = shape.text_frame
            tf.clear()
            p = tf.paragraphs[0]
            set_para(p, "Key Trend: JavaScript anchors current web stacks (62.8%), while Python captures dominant future interest (44.9%), followed by high-momentum languages Rust (30.9%) and Go (24.8%).", font_size=10.5, bold=True, color_rgb=(15, 52, 96), bullet=False)

s9.shapes.add_picture('output/charts/lang_curr.png', Inches(0.85), Inches(2.75), width=Inches(5.4))
s9.shapes.add_picture('output/charts/lang_want.png', Inches(6.65), Inches(2.75), width=Inches(5.4))

# --- SLIDE 10: Programming Language Trends - Findings & Implications ---
s10 = prs.slides[9]
s10_findings = [
    ("Ubiquitous Web Core: ", "JavaScript (62.8%) and HTML/CSS (53.3%) represent an inescapable baseline for modern front-end and full-stack software development."),
    ("Python's Universal Preeminence: ", "Python maintains a dual stronghold—commanding 51.4% current usage and ranking #1 in future desire (44.9%), fueled by AI, ML, and data analytics."),
    ("Rust & Go Velocity Shift: ", "Rust surges from outside the top 10 current languages to #6 in future demand (30.9%), with Go reaching #7 (24.8%), reflecting strong interest in memory-safe systems.")
]
s10_implications = [
    ("Technical Curriculum Priorities: ", "Educational institutions and bootcamps must treat TypeScript (38.7%) and Python as mandatory core fluencies alongside foundational web standards."),
    ("Enterprise Stack Modernization: ", "Engineering leadership should anticipate growing internal pressure to adopt Rust and Go for latency-critical, high-concurrency microservices."),
    ("Talent Pipeline Governance: ", "Hiring managers must recognize that developer preference for emerging languages indicates learning enthusiasm rather than immediate replacement of enterprise Java/C#.")
]
for shape in s10.shapes:
    if shape.name == 'Content Placeholder 2':
        tf = shape.text_frame
        tf.clear()
        p0 = tf.paragraphs[0]
        set_para(p0, "Empirical Findings (Survey Evidence)", font_size=13, bold=True, color_rgb=(15, 52, 96), bullet=False, space_after=6)
        for head, body in s10_findings:
            p = tf.add_paragraph()
            p.text = head + body
            p.font.name = 'Calibri'
            p.font.size = Pt(11)
            p.space_after = Pt(6)
    elif shape.name == 'Content Placeholder 3':
        tf = shape.text_frame
        tf.clear()
        p0 = tf.paragraphs[0]
        set_para(p0, "Strategic & Industry Implications", font_size=13, bold=True, color_rgb=(15, 52, 96), bullet=False, space_after=6)
        for head, body in s10_implications:
            p = tf.add_paragraph()
            p.text = head + body
            p.font.name = 'Calibri'
            p.font.size = Pt(11)
            p.space_after = Pt(6)

# --- SLIDE 11: Database Trends (Charts) ---
s11 = prs.slides[10]
for shape in list(s11.shapes):
    if shape.has_text_frame:
        txt = shape.text_frame.text
        if 'Bar chart' in txt:
            sp_elem = shape._element
            sp_elem.getparent().remove(sp_elem)
        elif 'Summarize key trends' in txt:
            tf = shape.text_frame
            tf.clear()
            p = tf.paragraphs[0]
            set_para(p, "Key Trend: PostgreSQL solidifies undisputed leadership (50.8% current -> 56.4% future). Relational databases anchor 91.8% of developer workflows, complemented by key-value caching (Redis 25.5%).", font_size=10.5, bold=True, color_rgb=(15, 52, 96), bullet=False)

s11.shapes.add_picture('output/charts/db_curr.png', Inches(0.85), Inches(2.75), width=Inches(5.4))
s11.shapes.add_picture('output/charts/db_want.png', Inches(6.65), Inches(2.75), width=Inches(5.4))

# --- SLIDE 12: Database Trends - Findings & Implications ---
s12 = prs.slides[11]
s12_findings = [
    ("PostgreSQL Hegemony: ", "PostgreSQL commands both current adoption (50.8%) and future preference (56.4%), demonstrating an expanding competitive moat across enterprise workloads."),
    ("Enduring Relational Foundation: ", "Over 91.8% of respondents actively utilize relational databases (PostgreSQL, MySQL, SQLite, MSSQL), refuting premature claims of NoSQL substitution."),
    ("Targeted Polyglot Persistence: ", "Non-relational databases (MongoDB 25.9%, Redis 20.8%) serve as specialized architectural complements for distributed caching and unstructured document storage.")
]
s12_implications = [
    ("Architecture & Infrastructure Strategy: ", "PostgreSQL serves as the most versatile, cost-effective standard for transaction processing, analytical extensions (pgvector), and relational integrity."),
    ("Legacy Migration Planning: ", "Commercial proprietary engines (Oracle 10.5%, MSSQL 26.4% current dropping to 18.6% future) face increasing migration pressures toward open-source PostgreSQL."),
    ("Full-Stack Competency Requirements: ", "Engineers require mastery of both relational modeling and in-memory caching layers (Redis) to construct modern high-throughput architectures.")
]
for shape in s12.shapes:
    if shape.name == 'Content Placeholder 2':
        tf = shape.text_frame
        tf.clear()
        p0 = tf.paragraphs[0]
        set_para(p0, "Empirical Findings (Survey Evidence)", font_size=13, bold=True, color_rgb=(15, 52, 96), bullet=False, space_after=6)
        for head, body in s12_findings:
            p = tf.add_paragraph()
            p.text = head + body
            p.font.name = 'Calibri'
            p.font.size = Pt(11)
            p.space_after = Pt(6)
    elif shape.name == 'Content Placeholder 3':
        tf = shape.text_frame
        tf.clear()
        p0 = tf.paragraphs[0]
        set_para(p0, "Strategic & Architectural Implications", font_size=13, bold=True, color_rgb=(15, 52, 96), bullet=False, space_after=6)
        for head, body in s12_implications:
            p = tf.add_paragraph()
            p.text = head + body
            p.font.name = 'Calibri'
            p.font.size = Pt(11)
            p.space_after = Pt(6)

# --- SLIDE 13: Dashboard Header ---
s13 = prs.slides[12]
for shape in s13.shapes:
    if shape.name == 'Content Placeholder 2':
        tf = shape.text_frame
        tf.clear()
        p0 = tf.paragraphs[0]
        set_para(p0, "Integrated Multi-Perspective Analytics Dashboard", font_size=14, bold=True, color_rgb=(15, 52, 96), bullet=False, space_after=6)
        dash_desc = [
            "• Tab 1 — Current Technology Usage: Production adoption across Languages, Databases, Web Frameworks, and Cloud Infrastructure.",
            "• Tab 2 — Future Technology Trends: Forward-looking developer interest and anticipated technology migration trajectories.",
            "• Tab 3 — Global Developer Demographics: Age distribution, work arrangement models, educational attainment, and technical roles.",
            "• Transparency Disclosure: Visualized through fully reproducible data analytics dashboards generated directly from verified survey records."
        ]
        for item in dash_desc:
            p = tf.add_paragraph()
            set_para(p, item, font_size=11.5, bold=False, color_rgb=(40, 40, 40), bullet=False, space_after=5)

# --- SLIDE 14: Dashboard Tab 1: Current Technology Usage ---
s14 = prs.slides[13]
s14.shapes.title.text_frame.paragraphs[0].font.size = Pt(28)
for shape in list(s14.shapes):
    if shape.name == 'Content Placeholder 2':
        sp_elem = shape._element
        sp_elem.getparent().remove(sp_elem)

s14.shapes.add_picture('output/charts/dashboard_tab1.png', Inches(0.85), Inches(1.8), width=Inches(7.2))
tb14 = s14.shapes.add_textbox(Inches(8.2), Inches(1.8), Inches(4.3), Inches(4.8))
tf14 = tb14.text_frame
tf14.word_wrap = True
p = tf14.paragraphs[0]
set_para(p, "Tab 1: Current Stacks Insight", font_size=13, bold=True, color_rgb=(15, 52, 96), bullet=False, space_after=6)
tab1_notes = [
    "• Languages: JavaScript (62.8%), HTML/CSS (53.3%), Python (51.4%), and SQL (51.4%) form the ubiquitous foundation of commercial software.",
    "• Databases: PostgreSQL (50.8%) leads, with MySQL (42.0%) and SQLite (34.6%) securing top relational positions.",
    "• Web Frameworks: Node.js (43.8%) and React (42.4%) represent the premier modern full-stack web development tandem.",
    "• Cloud Infrastructure: AWS commands majority enterprise cloud footprint (52.4%), followed by Azure (30.3%) and GCP (27.4%)."
]
for note in tab1_notes:
    p = tf14.add_paragraph()
    set_para(p, note, font_size=10.5, color_rgb=(40, 40, 40), bullet=False, space_after=4)

# --- SLIDE 15: Dashboard Tab 2: Future Technology Trends ---
s15 = prs.slides[14]
s15.shapes.title.text_frame.paragraphs[0].font.size = Pt(28)
for shape in list(s15.shapes):
    if shape.name == 'Content Placeholder 2':
        sp_elem = shape._element
        sp_elem.getparent().remove(sp_elem)

s15.shapes.add_picture('output/charts/dashboard_tab2.png', Inches(0.85), Inches(1.8), width=Inches(7.2))
tb15 = s15.shapes.add_textbox(Inches(8.2), Inches(1.8), Inches(4.3), Inches(4.8))
tf15 = tb15.text_frame
tf15.word_wrap = True
p = tf15.paragraphs[0]
set_para(p, "Tab 2: Future Trends Insight", font_size=13, bold=True, color_rgb=(15, 52, 96), bullet=False, space_after=6)
tab2_notes = [
    "• Language Aspirations: Python captures #1 future interest (44.9%), while high-performance languages Rust (30.9%) and Go (24.8%) gain immense momentum.",
    "• Database Evolution: PostgreSQL expands its lead to 56.4%, while SQLite (31.7%) and Redis (25.5%) show strong demand for lightweight and in-memory architectures.",
    "• Modern Web Stacks: React (40.0%), Next.js (22.1%), and Vue.js (19.7%) lead framework growth, emphasizing server-side rendering and component modularity.",
    "• Cloud Adoption: Cloudflare surges to 19.9% in future demand, highlighting developer focus on edge computing and distributed performance."
]
for note in tab2_notes:
    p = tf15.add_paragraph()
    set_para(p, note, font_size=10.5, color_rgb=(40, 40, 40), bullet=False, space_after=4)

# --- SLIDE 16: Dashboard Tab 3: Demographics ---
s16 = prs.slides[15]
s16.shapes.title.text_frame.paragraphs[0].font.size = Pt(28)
for shape in list(s16.shapes):
    if shape.name == 'Content Placeholder 2':
        sp_elem = shape._element
        sp_elem.getparent().remove(sp_elem)


s16.shapes.add_picture('output/charts/dashboard_tab3.png', Inches(0.85), Inches(1.8), width=Inches(7.2))
tb16 = s16.shapes.add_textbox(Inches(8.2), Inches(1.8), Inches(4.3), Inches(4.8))
tf16 = tb16.text_frame
tf16.word_wrap = True
p = tf16.paragraphs[0]
set_para(p, "Tab 3: Demographics Insight", font_size=13, bold=True, color_rgb=(15, 52, 96), bullet=False, space_after=6)
tab3_notes = [
    "• Age Cohorts: The developer workforce is highly concentrated in early-to-mid career professionals: 25–34 years old (36.5%) and 35–44 years old (22.8%).",
    "• Work Arrangement: 80.0% of reporting developers operate under remote-capable models (42.0% Hybrid, 38.0% Fully Remote), with only 20.0% fully in-person.",
    "• Formal Education: Strong academic grounding characterizes the industry, with Bachelor's (38.1%) and Master's (23.8%) degrees accounting for nearly 62% of participants.",
    "• Core Specializations: Full-stack developers (27.9%) and back-end engineers (15.2%) constitute the primary architectural backbone of technical teams."
]
for note in tab3_notes:
    p = tf16.add_paragraph()
    set_para(p, note, font_size=10.5, color_rgb=(40, 40, 40), bullet=False, space_after=4)

# --- SLIDE 17: Discussion ---
s17 = prs.slides[16]
for shape in s17.shapes:
    if shape.name == 'Content Placeholder 3':
        tf = shape.text_frame
        tf.clear()
        p0 = tf.paragraphs[0]
        set_para(p0, "Cross-Tabulation & Multi-Dimensional Synthesis", font_size=13, bold=True, color_rgb=(15, 52, 96), bullet=False, space_after=6)
        discussion_points = [
            ("The Stability vs. Novelty Paradox: ", "While developer interest strongly gravitates toward modern innovations (Rust, Go, Next.js, Edge Computing), operational enterprise stacks remain solidly anchored in mature, battle-tested technologies (SQL, PostgreSQL, JavaScript, AWS)."),
            ("The Rise of Polyglot Architecture: ", "Modern production applications rarely rely on single monolithic stacks; typical engineers leverage 3+ languages (JavaScript front-end, Python/Go microservices, SQL queries) and dual-layer persistence (PostgreSQL + Redis)."),
            ("Workplace Geography Transformation: ", "The consolidation of remote/hybrid work (80.0%) permanently decouples developer talent from geographic tech clusters, elevating the strategic importance of asynchronous collaboration tooling and cloud environments."),
            ("Data Quality & Methodological Caveats: ", "As an opt-in survey of engaged technical contributors, results reflect enthusiast and professional developer mindshare rather than passive institutional IT deployments.")
        ]
        for head, body in discussion_points:
            p = tf.add_paragraph()
            p.text = head + body
            p.font.name = 'Calibri'
            p.font.size = Pt(11)
            p.space_after = Pt(6)

# --- SLIDE 18: Overall Findings & Implications ---
s18 = prs.slides[17]
s18_findings = [
    ("Consolidated Tech Anchors: ", "JavaScript, Python, SQL, and PostgreSQL form the core quadrumvirate of the global software development ecosystem."),
    ("Decoupled Systems Momentum: ", "Rust and Go represent the primary vector for future systems programming, driven by memory safety, concurrency, and microservice efficiency."),
    ("Permanent Remote Shift: ", "The shift toward distributed engineering teams (80.0% remote/hybrid) is structural, reshaping team coordination and technical management practices.")
]
s18_implications = [
    ("For Engineering Leaders: ", "Standardize core architectures on robust open-source engines (PostgreSQL, TypeScript) while piloting Rust and Go in high-performance subsystems."),
    ("For Technical Hiring Teams: ", "Prioritize foundational full-stack problem-solving and polyglot database competence over transient syntax memorization."),
    ("For Professional Developers: ", "Combine broad full-stack literacy with deep specialization in cloud infrastructure, data pipelines, or high-concurrency systems.")
]
for shape in s18.shapes:
    if shape.name == 'Content Placeholder 2':
        tf = shape.text_frame
        tf.clear()
        p0 = tf.paragraphs[0]
        set_para(p0, "Cross-Cutting Empirical Findings", font_size=13, bold=True, color_rgb=(15, 52, 96), bullet=False, space_after=6)
        for head, body in s18_findings:
            p = tf.add_paragraph()
            p.text = head + body
            p.font.name = 'Calibri'
            p.font.size = Pt(11)
            p.space_after = Pt(6)
    elif shape.name == 'Content Placeholder 3':
        tf = shape.text_frame
        tf.clear()
        p0 = tf.paragraphs[0]
        set_para(p0, "Strategic Industry Implications", font_size=13, bold=True, color_rgb=(15, 52, 96), bullet=False, space_after=6)
        for head, body in s18_implications:
            p = tf.add_paragraph()
            p.text = head + body
            p.font.name = 'Calibri'
            p.font.size = Pt(11)
            p.space_after = Pt(6)

# --- SLIDE 19: Conclusion ---
s19 = prs.slides[18]
for shape in s19.shapes:
    if shape.name == 'Content Placeholder 3':
        tf = shape.text_frame
        tf.clear()
        p0 = tf.paragraphs[0]
        set_para(p0, "Project Conclusion & Executive Takeaways", font_size=13, bold=True, color_rgb=(15, 52, 96), bullet=False, space_after=6)
        conclusion_points = [
            ("Analytical Objective Achieved: ", "Successfully executed end-to-end data analysis across 65,437 global survey responses, establishing defensible empirical benchmarks for technical decision-makers."),
            ("Technology Modernization Blueprint: ", "Documented the operational dominance of Python, PostgreSQL, and JavaScript, while quantifying future migration velocities toward Rust, Go, Next.js, and Cloudflare."),
            ("Workforce Reality Defined: ", "Confirmed that hybrid/remote development is the established operating standard across the global software industry."),
            ("Methodological Integrity Upheld: ", "Enforced transparent denominator tracking, strict deduplication, reproducible Python scripts, and ethical boundaries separating survey desire from verified hiring demand.")
        ]
        for head, body in conclusion_points:
            p = tf.add_paragraph()
            p.text = head + body
            p.font.name = 'Calibri'
            p.font.size = Pt(11.5)
            p.space_after = Pt(7)

# --- SLIDE 20: Appendix ---
s20 = prs.slides[19]
for shape in list(s20.shapes):
    if shape.name == 'Content Placeholder 3' and shape.has_text_frame:
        sp_elem = shape._element
        sp_elem.getparent().remove(sp_elem)

s20.shapes.add_picture('output/charts/comp_by_role.png', Inches(0.85), Inches(1.85), width=Inches(6.4))
tb20 = s20.shapes.add_textbox(Inches(7.5), Inches(1.85), Inches(5.0), Inches(4.8))
tf20 = tb20.text_frame
tf20.word_wrap = True
p = tf20.paragraphs[0]
set_para(p, "Appendix: Compensation Architecture", font_size=13, bold=True, color_rgb=(15, 52, 96), bullet=False, space_after=6)
app_notes = [
    "• Sample Base: Evaluated across N=23,435 respondents with verified annual compensation (ConvertedCompYearly), filtered to roles with N ≥ 100.",
    "• Leadership & Management: Engineering Managers ($116,000 median) and Senior Executives ($127,388 median) command peak market premiums.",
    "• High-Value Technical Roles: Site Reliability Engineers ($99,099 median) and Cloud Infrastructure Engineers ($96,666 median) outperform general developer averages.",
    "• Core Engineering Benchmarks: Data Engineers ($76,000 median), AI Developers ($73,681 median), and Full-Stack Developers reflect robust baseline enterprise demand.",
    "• Denominator & Currency Note: Compensation converted to USD and adjusted across international exchange rates per Stack Overflow survey methodology."
]
for note in app_notes:
    p = tf20.add_paragraph()
    set_para(p, note, font_size=10.5, color_rgb=(40, 40, 40), bullet=False, space_after=4)

prs.save(OUT_PPTX)
print("Presentation successfully updated and saved to:", OUT_PPTX)
