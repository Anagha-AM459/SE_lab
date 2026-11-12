
import math


def validate_height_and_fastpass(rider_spec):
    try:
        if not isinstance(rider_spec, str):
            return "Invalid input: Expected text in Height:FastPass format"

        parts = rider_spec.strip().split(':')

        if len(parts) != 2:
            return "Invalid input: Use Height:FastPass format (e.g. 130:YES)"

        height_str, pass_str = parts

        height = int(height_str.strip())

        if height < 0:
            return "Invalid input: Height cannot be negative"

        pass_str = pass_str.strip().upper()

        pass_map = {"YES": True, "NO": False}

        if pass_str not in pass_map:
            return "Invalid input: FastPass must be YES or NO"

        has_fastpass = pass_map[pass_str]

        eligible = height >= 120

        status = "FastPass Priority" if has_fastpass else "Standard Entry"

        return f"Height {height}cm: {'Approved' if eligible else 'Denied'} ({status})"

    except (ValueError, TypeError):
        return "Invalid input: Please enter a valid height and FastPass value"


def compute_dispatch_throughput(ride_metric_str):
    try:
        if not isinstance(ride_metric_str, str):
            return "Invalid input: Expected riders/mins format"

        parts = ride_metric_str.split('/')

        if len(parts) != 2:
            return "Invalid input: Use riders/mins format (e.g. 48/2.5)"

        riders_str, mins_str = parts

        riders = float(riders_str)
        cycle_mins = float(mins_str)

        if not math.isfinite(riders) or not math.isfinite(cycle_mins):
            return "Invalid input: Values must be finite numbers"

        if riders < 0:
            return "Invalid input: Riders cannot be negative"

        if cycle_mins <= 0:
            return "Invalid input: Minutes must be greater than zero"

        rate = riders / cycle_mins

        return round(rate, 2)

    except (ValueError, TypeError):
        return "Invalid input: Please enter valid numeric values"


def resolve_safety_restraint_code(zone_code):
    try:
        if not isinstance(zone_code, str):
            return "Invalid input: Zone code must be text"

        prefix = zone_code.strip().upper()[:3]

        restraint_types = {
            "CST": "Over-the-Shoulder Harness",
            "WTR": "Lap Bar and Seatbelt",
            "DRP": "Hydraulic Shoulder Vest",
            "WHL": "Manual Safety Bar"
        }

        return restraint_types.get(
            prefix,
            "Unknown ride zone code"
        )

    except (ValueError, TypeError):
        return "Invalid input: Please enter a valid zone code"


def main():
    print("==== Running validate_height_and_fastpass ====")
    r_input = input("Enter rider spec (Height:FastPass, e.g. 140:YES): ")
    print(validate_height_and_fastpass(r_input))

    print("\n==== Running compute_dispatch_throughput ====")
    t_input = input("Enter riders/mins (e.g. 48/2.5): ")
    print("Throughput (riders/min):", compute_dispatch_throughput(t_input))

    print("\n==== Running resolve_safety_restraint_code ====")
    z_input = input("Enter ride zone code (e.g. CST_01, WTR_A): ")
    print("Restraint:", resolve_safety_restraint_code(z_input))


if __name__ == "__main__":
    main()
