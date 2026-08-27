import json
from datetime import datetime


incident_type = input("Incident Type: ")

severity = input(
    "Severity (Critical/High/Medium/Low): "
)

description = input("Description: ")


incident = {
    "id": "INC-1001",
    "type": incident_type,
    "severity": severity,
    "status": "Open",
    "description": description,
    "created_at": str(datetime.now())
}


with open("incidents.json", "r") as file:

    incidents = json.load(file)


incidents.append(incident)


with open("incidents.json", "w") as file:

    json.dump(incidents, file, indent=4)


print("\nINCIDENT SAVED SUCCESSFULLY")

print("=" * 50)

print(incident)
