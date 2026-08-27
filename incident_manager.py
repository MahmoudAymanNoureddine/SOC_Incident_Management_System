import json
from datetime import datetime

INCIDENTS_FILE = "incidents.json"


# -------------------------
# FILE FUNCTIONS
# -------------------------

def load_incidents():
    try:
        with open(INCIDENTS_FILE, "r") as file:
            return json.load(file)
    except:
        return []


def save_incidents(incidents):
    with open(INCIDENTS_FILE, "w") as file:
        json.dump(incidents, file, indent=4)


# -------------------------
# PRIORITY & RISK ENGINE
# -------------------------

def calculate_priority(severity):

    severity = severity.lower()

    if severity == "critical":
        return "P1"

    elif severity == "high":
        return "P2"

    elif severity == "medium":
        return "P3"

    return "P4"


def get_recommendation(severity):

    severity = severity.lower()

    recommendations = {
        "critical": "Immediate Containment Required",
        "high": "Start Investigation Immediately",
        "medium": "Review and Monitor",
        "low": "Continue Monitoring"
    }

    return recommendations.get(
        severity,
        "No Recommendation"
    )


# -------------------------
# ADD INCIDENT
# -------------------------

def add_incident():

    incidents = load_incidents()

    incident_type = input("Incident Type: ")

    severity = input(
        "Severity (Critical/High/Medium/Low): "
    )

    description = input(
        "Description: "
    )

    incident_id = f"INC-{1001 + len(incidents)}"

    incident = {

        "id": incident_id,

        "type": incident_type,

        "severity": severity.title(),

        "priority": calculate_priority(
            severity
        ),

        "status": "Open",

        "description": description,

        "risk_level": severity.title(),

        "recommendation": get_recommendation(
            severity
        ),

        "created_at": str(
            datetime.now()
        ),

        "updated_at": None
    }

    incidents.append(
        incident
    )

    save_incidents(
        incidents
    )

    print("\nINCIDENT SAVED SUCCESSFULLY")

    for key, value in incident.items():
        print(f"{key}: {value}")


# -------------------------
# VIEW INCIDENTS
# -------------------------

def view_incidents():

    incidents = load_incidents()

    if not incidents:
        print("\nNo Incidents Found")
        return

    for incident in incidents:

        print("\n" + "=" * 50)

        for key, value in incident.items():
            print(f"{key}: {value}")

        print("=" * 50)


# -------------------------
# SEARCH INCIDENT
# -------------------------

def search_incident():

    incident_id = input(
        "Enter Incident ID: "
    )

    incidents = load_incidents()

    for incident in incidents:

        if incident["id"] == incident_id:

            print("\nINCIDENT FOUND")

            print("=" * 50)

            for key, value in incident.items():
                print(f"{key}: {value}")

            return

    print("\nIncident Not Found")


# -------------------------
# UPDATE STATUS
# -------------------------

def update_status():

    incident_id = input(
        "Enter Incident ID: "
    )

    incidents = load_incidents()

    for incident in incidents:

        if incident["id"] == incident_id:

            print(
                f"\nCurrent Status: {incident['status']}"
            )

            new_status = input(
                "New Status (Open/Investigating/Resolved/Closed): "
            )

            incident["status"] = new_status

            incident["updated_at"] = str(
                datetime.now()
            )

            save_incidents(
                incidents
            )

            print(
                "\nStatus Updated Successfully"
            )

            return

    print("Incident Not Found")


# -------------------------
# DELETE INCIDENT
# -------------------------

def delete_incident():

    incident_id = input(
        "Enter Incident ID: "
    )

    incidents = load_incidents()

    for incident in incidents:

        if incident["id"] == incident_id:
            incidents.remove(
                incident
            )

            save_incidents(
                incidents
            )

            print(
                "\nIncident Deleted Successfully"
            )

            return

    print(
        "\nIncident Not Found"
    )


# -------------------------
# DASHBOARD
# -------------------------

def dashboard():

    incidents = load_incidents()

    total = len(
        incidents
    )

    open_count = 0
    investigating_count = 0
    resolved_count = 0
    closed_count = 0

    critical = 0
    high = 0
    medium = 0
    low = 0

    for incident in incidents:

        status = incident[
            "status"
        ]

        severity = incident[
            "severity"
        ]

        if status == "Open":
            open_count += 1

        elif status == "Investigating":
            investigating_count += 1

        elif status == "Resolved":
            resolved_count += 1

        elif status == "Closed":
            closed_count += 1

        if severity == "Critical":
            critical += 1

        elif severity == "High":
            high += 1

        elif severity == "Medium":
            medium += 1

        elif severity == "Low":
            low += 1

    print("\nSOC INCIDENT DASHBOARD")

    print("=" * 60)

    print(
        f"Total Incidents : {total}"
    )

    print("\nStatus Summary")

    print("-" * 60)

    print(
        f"Open          : {open_count}"
    )

    print(
        f"Investigating : {investigating_count}"
    )

    print(
        f"Resolved      : {resolved_count}"
    )

    print(
        f"Closed        : {closed_count}"
    )

    print("\nSeverity Summary")

    print("-" * 60)

    print(
        f"Critical      : {critical}"
    )

    print(
        f"High          : {high}"
    )

    print(
        f"Medium        : {medium}"
    )

    print(
        f"Low           : {low}"
    )

    print("=" * 60)


# -------------------------
# REPORTS
# -------------------------

def generate_reports():

    incidents = load_incidents()

    report = []

    report.append(
        "SOC SECURITY REPORT"
    )

    report.append("=" * 60)

    report.append(
        f"Generated: {datetime.now()}"
    )

    report.append("=" * 60)

    for incident in incidents:

        report.append("")

        for key, value in incident.items():

            report.append(
                f"{key}: {value}"
            )

    with open(
        "security_report.txt",
        "w"
    ) as file:

        file.write(
            "\n".join(report)
        )

    with open(
        "security_report.json",
        "w"
    ) as file:

        json.dump(
            incidents,
            file,
            indent=4
        )

    print(
        "\nReports Generated Successfully"
    )


# -------------------------
# MAIN MENU
# -------------------------

while True:

    print("\nSOC INCIDENT MANAGEMENT SYSTEM")

    print("=" * 60)

    print("1. Add Incident")
    print("2. View Incidents")
    print("3. Search Incident")
    print("4. Update Status")
    print("5. Delete Incident")
    print("6. Dashboard")
    print("7. Generate Reports")
    print("8. Exit")

    print("=" * 60)

    choice = input(
        "Choose Option: "
    )

    if choice == "1":
        add_incident()

    elif choice == "2":
        view_incidents()

    elif choice == "3":
        search_incident()

    elif choice == "4":
        update_status()

    elif choice == "5":
        delete_incident()

    elif choice == "6":
        dashboard()

    elif choice == "7":
        generate_reports()

    elif choice == "8":

        print(
            "\nExiting System..."
        )

        break

    else:

        print(
            "\nInvalid Option"
        )
