# SOC Incident Management System

## Overview

SOC Incident Management System (SIMS) is a Python-based cybersecurity project designed to help Security Operations Center (SOC) analysts track, manage, prioritize, and report security incidents.

The system provides incident lifecycle management, risk assessment, severity classification, priority assignment, reporting capabilities, and dashboard analytics through a simple command-line interface.

---

## Features

- Add Security Incidents
- View All Incidents
- Search Incident by ID
- Update Incident Status
- Delete Incidents
- Severity Classification
- Automatic Priority Assignment
- Risk Assessment Engine
- Recommendation Engine
- Incident Lifecycle Management
- Dashboard Analytics
- TXT Report Generation
- JSON Report Generation
- JSON Incident Database
- Automatic Timestamp Tracking

---

## Incident Lifecycle
Open
↓
Investigating
↓
Resolved
↓
Closed

---

## Severity Levels
Critical
High
Medium
Low

---

## Priority Mapping
Critical → P1
High     → P2
Medium   → P3
Low      → P4

---

## Technologies Used

- Python 3
- JSON
- File Handling
- Datetime Module

---

## Project Structure
SOC_Incident_Management_System

├── screenshots
│   ├── README.md
│   ├── main-menu.png
│   ├── add-incident.png
│   ├── search-incident.png
│   ├── dashboard-report.png
│   ├── security-report-generation.png
│   ├── security-report-txt.png
│   └── incidents-json-database.png
│
├── incident_manager.py
├── incidents.json
├── security_report.txt
├── security_report.json
├── config.json
├── README.md
└── LICENSE

---

## Dashboard Capabilities

The dashboard provides:

- Total Incidents
- Open Incidents
- Investigating Incidents
- Resolved Incidents
- Closed Incidents
- Critical Incidents
- High Incidents
- Medium Incidents
- Low Incidents
- Overall Risk Assessment

---

## Risk Assessment Engine

The system automatically evaluates security risk levels based on incident severity distribution.

### Risk Levels
LOW
MEDIUM
HIGH
CRITICAL

---

## Recommendations Engine

Example recommendations:
Immediate Containment Required

Start Investigation Immediately

Review Security Events

Continue Monitoring

---

## Reports Generated

### TXT Report
security_report.txt

Contains:

- Incident Details
- Severity Information
- Priority Levels
- Status Tracking
- Recommendations

### JSON Report
security_report.json

Provides structured incident data for future processing and automation.

---

## Screenshots

### Main Menu
Demonstrates access to all system functionalities.

### Add Incident
Shows incident creation and automatic classification.

### Search Incident
Retrieves incidents using unique Incident IDs.

### Dashboard Report
Displays incident statistics and severity distribution.

### Security Report Generation
Demonstrates successful report export.

### Security Report (TXT)
Shows detailed incident reporting.

### Incident Database (JSON)
Demonstrates structured JSON-based storage.

---

## Skills Demonstrated

- Python Programming
- File Handling
- JSON Processing
- Data Management
- Automation
- Incident Lifecycle Management
- Risk Assessment
- Security Reporting
- SOC Operations Concepts
- Cybersecurity Fundamentals

---

## Future Enhancements

- Search by Severity
- Search by Status
- CSV Export
- User Authentication
- Threat Intelligence Integration
- Database Integration
- SIEM Integration

---

## Author

Mahmoud Ayman Noureddine

Cybersecurity engineer | SOC Analyst  | Blue Team 
