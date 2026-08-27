import json
from datetime import datetime


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


def get_next_incident_id():

    try:

        with open("incidents.json", "r") as file:

            incidents = json.load(file)

            return f"INC-{1001 + len(incidents)}"

    except:

        return "INC-1001"


def create_incident():

    incident_type = input("Incident Type: ")

    severity = input("Severity (Critical/High/Medium/Low): ")

    description = input("Description: ")

    priority = calculate_priority(severity)

    incident = {

        "id": get_next_incident_id(),

        "type": incident_type,

        "severity": severity.title(),

        "priority": priority,

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


create_incident()
