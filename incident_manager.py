import json
from datetime import datetime


def create_incident():

    incident_type = input("Incident Type: ")

    severity = input("Severity (Critical/High/Medium/Low): ")

    description = input("Description: ")

    incident = {
        "id": "INC-1001",
        "type": incident_type,
        "severity": severity,
        "status": "Open",
        "description": description,
        "created_at": str(datetime.now())
    }

    print("\nINCIDENT CREATED")

    print("=" * 40)

    for key, value in incident.items():
        print(f"{key}: {value}")


create_incident()
