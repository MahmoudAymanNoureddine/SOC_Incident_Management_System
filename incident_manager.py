import json
from datetime import datetime


# =========================
# Priority Engine
# =========================

def calculate_priority(severity):

    severity = severity.lower()

    if severity == "critical":
        return "P1"

    elif severity == "high":
        return "P2"

    elif severity == "medium":
        return "P3"

    else:
        return "P4"


# =========================
# Incident ID Generator
# =========================

def get_next_incident_id():

    try:

        with open("incidents.json", "r") as file:

            incidents = json.load(file)

            return f"INC-{1001 + len(incidents)}"

    except:

        return "INC-1001"


# =========================
# Add Incident
# =========================

def create_incident():

    incident_type = input("Incident Type: ")

    severity = input(
        "Severity (Critical/High/Medium/Low): ")

    description = input("Description: ")

    incident = {

        "id": get_next_incident_id(),

        "type": incident_type,

        "severity": severity.title(),

        "priority": calculate_priority(severity),

        "status": "Open",

        "description": description,

        "created_at": str(datetime.now())
    }

    try:

        with open("incidents.json", "r") as file:

            incidents = json.load(file)

    except:

        incidents = []

    incidents.append(incident)

    with open("incidents.json", "w") as file:

        json.dump(incidents, file, indent=4)

    print("\nINCIDENT SAVED SUCCESSFULLY")
    print("=" * 50)

    for key, value in incident.items():

        print(f"{key}: {value}")


# =========================
# View Incidents
# =========================

def view_incidents():

    try:

        with open("incidents.json", "r") as file:

            incidents = json.load(file)

    except:

        incidents = []

    print("\nALL INCIDENTS")
    print("=" * 50)

    if len(incidents) == 0:

        print("No incidents found.")
        return

    for incident in incidents:

        print(f"\nID: {incident['id']}")
        print(f"Type: {incident['type']}")
        print(f"Severity: {incident['severity']}")
        print(f"Priority: {incident['priority']}")
        print(f"Status: {incident['status']}")
        print("-" * 50)


# =========================
# Dashboard
# =========================

def dashboard():

    try:

        with open("incidents.json", "r") as file:

            incidents = json.load(file)

    except:

        incidents = []

    total = len(incidents)

    critical = 0
    high = 0
    medium = 0
    low = 0

    open_incidents = 0

    for incident in incidents:

        if incident["severity"] == "Critical":
            critical += 1

        elif incident["severity"] == "High":
            high += 1

        elif incident["severity"] == "Medium":
            medium += 1

        elif incident["severity"] == "Low":
            low += 1

        if incident["status"] == "Open":
            open_incidents += 1

    print("\nSOC INCIDENT DASHBOARD")
    print("=" * 50)

    print("Total Incidents :", total)

    print("\nOpen Incidents :", open_incidents)

    print("\nCritical :", critical)
    print("High     :", high)
    print("Medium   :", medium)
    print("Low      :", low)

    print("=" * 50)


# =========================
# Main Menu
# =========================

while True:

    print("\nSOC INCIDENT MANAGEMENT SYSTEM")

    print("=" * 50)

    print("1. Add Incident")
    print("2. View Incidents")
    print("3. Dashboard")
    print("4. Exit")

    print("=" * 50)

    choice = input("Choose Option: ")

    if choice == "1":

        create_incident()

    elif choice == "2":

        view_incidents()

    elif choice == "3":

        dashboard()

    elif choice == "4":

        print("Exiting System...")
        break

    else:

        print("Invalid Option")
