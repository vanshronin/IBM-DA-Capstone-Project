# IBM Data Analyst Capstone Project — Final Submission

**Author:** Vanshaj Bhardwaj  
**Date:** October 2026  
**Project Repository:** `FINALpROJECTsUB`  

---

## 1. Project Overview

This repository contains the completed, validated, end-to-end deliverables for the **IBM Data Analyst Capstone Project**. The analysis is based on the 2024 Stack Overflow Developer Survey (`DATASET/survey_data.csv`, 65,437 rows, 114 columns, 159.5 MB) and populates the official PowerPoint presentation template (`TEMP/Data Analyst Capstone Template 2026.pptx`).

---

## 2. Directory & Deliverable Structure

```text
FINALpROJECTsUB/
│
├── DATASET/
│   └── survey_data.csv                    # Primary survey dataset (65,437 rows, 159.5 MB)
│
├── TEMP/
│   └── Data Analyst Capstone Template 2026.pptx  # Preserved original PowerPoint template
│
├── output/
│   ├── Data Analyst Capstone Project Report.pptx # Final editable 20-slide presentation
│   ├── Data Analyst Capstone Project Report.pdf  # Final submission-ready 20-page PDF
│   ├── analysis_summary.md               # Empirical findings, metrics & methodology audit
│   ├── charts/                           # High-resolution (300 DPI) chart images
│   │   ├── lang_curr.png                 # Top 10 languages: current usage
│   │   ├── lang_want.png                 # Top 10 languages: future interest
│   │   ├── db_curr.png                   # Top 10 databases: current usage
│   │   ├── db_want.png                   # Top 10 databases: future interest
│   │   ├── dashboard_tab1.png            # Dashboard Tab 1: Current Technology Usage
│   │   ├── dashboard_tab2.png            # Dashboard Tab 2: Future Technology Trends
│   │   ├── dashboard_tab3.png            # Dashboard Tab 3: Developer Demographics
│   │   └── comp_by_role.png              # Appendix: Median annual compensation by role
│   └── pdf_preview/                      # Rendered inspection images of all 20 PDF slides
│
├── calculate_metrics.py                  # Standalone reproducible data calculation script
├── generate_charts.py                    # Standalone reproducible visualization pipeline
├── build_presentation.py                 # Standalone script populating the PPTX template
└── README.md                             # Reproduction guide and execution workflow
```

---

## 3. How to Reproduce the Analysis & Regenerate Deliverables

### Prerequisites:
- Python 3.12+ (or compatible Python 3 environment)
- Dependencies: `pandas`, `numpy`, `matplotlib`, `python-pptx`, `seaborn`, `pywin32`, `pymupdf`

```powershell
pip install pandas numpy matplotlib python-pptx seaborn pywin32 pymupdf
```

### Execution Steps:
1. **Calculate All Metrics:**
   ```powershell
   python calculate_metrics.py
   ```
2. **Generate All Publication-Ready Visualizations:**
   ```powershell
   python generate_charts.py
   ```
3. **Populate Presentation:**
   ```powershell
   python build_presentation.py
   ```
4. **Export to Submission-Ready PDF (via Microsoft PowerPoint COM automation):**
   ```powershell
   python -c "import win32com.client, os; ppt = win32com.client.Dispatch('PowerPoint.Application'); pres = ppt.Presentations.Open(os.path.abspath('output/Data Analyst Capstone Project Report.pptx'), WithWindow=False); pres.SaveAs(os.path.abspath('output/Data Analyst Capstone Project Report.pdf'), 32); pres.Close(); ppt.Quit()"
   ```

---

## 4. Key Analytical Insights
- **JavaScript & Python Lead:** JavaScript commands current web engineering (62.8%), while Python captures peak future interest (44.9%) and dominates data/AI stacks.
- **PostgreSQL Hegemony:** Commands 50.8% current usage and expands to 56.4% future intent; relational databases anchor 91.8% of developer workflows.
- **Workplace Transformation:** 80.0% of professional developers work under remote-capable arrangements (42.0% Hybrid, 38.0% Fully Remote).
- **High-Value Technical Roles:** Cloud Infrastructure ($96.7k) and Site Reliability Engineers ($99.1k) command top technical wage tiers below executive leadership ($116k–$127k+).
