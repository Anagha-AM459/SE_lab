"""Manage vehicle service records for a garage."""

import hashlib
import json
import shutil
from datetime import date
from pathlib import Path

SERVICE_COSTS = {
    "General": 2500,
    "Brake Check": 1200,
    "Oil Change": 1100,
    "Wheel Alignment": 1200,
}

SERVICE_RECORDS = {}


def add_service(vehicle_no, service_type="General"):
    """Add a service job for a vehicle."""
    if service_type not in SERVICE_COSTS:
        print("Unknown service type:", service_type)
        return

    SERVICE_RECORDS.setdefault(vehicle_no, []).append({
        "type": service_type,
        "cost": SERVICE_COSTS[service_type],
        "date": str(date.today()),
    })


def cancel_service(vehicle_no, service_type="General"):
    """Cancel a service job for a vehicle."""
    jobs = SERVICE_RECORDS.get(vehicle_no, [])

    for job in jobs:
        if job["type"] == service_type:
            jobs.remove(job)
            if not jobs:
                del SERVICE_RECORDS[vehicle_no]
            return

    print("No matching service for", vehicle_no)


def get_total_cost(vehicle_no):
    """Calculate the total service cost for a vehicle."""
    total_cost = 0
    for job in SERVICE_RECORDS.get(vehicle_no, []):
        total_cost += job["cost"]
    return total_cost


def job_card_id(vehicle_no):
    """Generate a job card ID for a vehicle."""
    return hashlib.sha256(vehicle_no.encode()).hexdigest()[:8]


def busiest_vehicle(records=None):
    """Return the vehicle with the most service jobs."""
    if records is None:
        records = SERVICE_RECORDS
    if not records:
        return None
    return max(records, key=lambda vehicle: len(records[vehicle]))


def save_records(file_name="services.json"):
    """Save service records to a JSON file."""
    with open(file_name, "w", encoding="utf-8") as file:
        json.dump(SERVICE_RECORDS, file, indent=2)


def load_records(file_name="services.json"):
    """Load service records from a JSON file."""
    try:
        with open(file_name, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}


def backup_records(folder):
    """Copy the saved service records to a backup folder."""
    source = Path("services.json")
    destination = Path(folder)
    destination.mkdir(parents=True, exist_ok=True)
    if source.exists():
        shutil.copy2(source, destination / source.name)


def main():
    """Run the vehicle service demonstration."""
    add_service("KA01AB1234", "Oil Change")
    add_service("KA01AB1234", "Wheel Alignment")
    add_service("KA05XY9876")
    add_service("KA03MN4455", "Brake Check")

    cancel_service("KA05XY9876", "Brake Check")
    cancel_service("KA09ZZ0001", "General")
    cancel_service("KA03MN4455", "Brake Check")

    print("Total for KA01AB1234:", get_total_cost("KA01AB1234"))
    print("Total for KA05XY9876:", get_total_cost("KA05XY9876"))
    print("Job card for KA01AB1234:", job_card_id("KA01AB1234"))

    save_records()
    loaded = load_records()
    print(
        "Vehicles on file:",
        len(loaded),
        "| busiest vehicle:",
        busiest_vehicle(loaded),
    )


if __name__ == "__main__":
    main()
