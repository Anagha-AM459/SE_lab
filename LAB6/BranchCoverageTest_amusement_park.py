
import pytest

from amusement_park_ride_access import (
    process_ride_admissions,
    inspect_safety_restraints
)


# -------------------------------
# PROCESS RIDE ADMISSIONS TESTS
# -------------------------------

def test_single_adult_family_ride():
    groups = [{
        "is_open": True,
        "ride_type": "family",
        "has_fast_lane": False,
        "patrons": [
            {"height_cm": 150, "health_warning": False, "is_child": False}
        ]
    }]

    result = process_ride_admissions(groups, 5.0)
    assert result["total_revenue"] == 10.0
    assert result["status"] == "COMPLETED"


def test_invalid_groups():
    with pytest.raises(ValueError):
        process_ride_admissions("invalid", 5.0)


def test_negative_express_pass_fee():
    with pytest.raises(ValueError):
        process_ride_admissions([], -5.0)


def test_closed_ride():
    groups = [{"is_open": False, "ride_type": "family"}]
    result = process_ride_admissions(groups, 5.0)
    assert result["status"] == "ZERO_ADMISSIONS"


def test_roller_coaster_admission():
    groups = [{
        "is_open": True,
        "ride_type": "roller_coaster",
        "patrons": [{"height_cm": 150}]
    }]
    result = process_ride_admissions(groups, 5.0)
    assert result["total_revenue"] == 25.0


def test_water_ride_admission():
    groups = [{
        "is_open": True,
        "ride_type": "water_ride",
        "patrons": [{"height_cm": 150}]
    }]
    result = process_ride_admissions(groups, 5.0)
    assert result["total_revenue"] == 18.0


def test_family_ride_child_discount():
    groups = [{
        "is_open": True,
        "ride_type": "family",
        "patrons": [{"height_cm": 130, "is_child": True}]
    }]
    result = process_ride_admissions(groups, 5.0)
    assert result["total_revenue"] == 6.0


def test_unknown_ride_type():
    groups = [{
        "is_open": True,
        "ride_type": "unknown",
        "patrons": []
    }]
    result = process_ride_admissions(groups, 5.0)
    assert result["status"] == "ZERO_ADMISSIONS"


def test_invalid_height():
    groups = [{
        "is_open": True,
        "ride_type": "family",
        "patrons": [{"height_cm": 0}]
    }]
    result = process_ride_admissions(groups, 5.0)
    assert result["status"] == "ZERO_ADMISSIONS"


def test_below_minimum_height():
    groups = [{
        "is_open": True,
        "ride_type": "family",
        "patrons": [{"height_cm": 100}]
    }]
    result = process_ride_admissions(groups, 5.0)
    assert result["status"] == "ZERO_ADMISSIONS"


def test_health_warning_on_family_ride():
    groups = [{
        "is_open": True,
        "ride_type": "family",
        "patrons": [
            {"height_cm": 150, "health_warning": True},
            {"height_cm": 150}
        ]
    }]
    result = process_ride_admissions(groups, 5.0)
    assert result["total_revenue"] == 10.0


def test_health_warning_on_roller_coaster():
    groups = [{
        "is_open": True,
        "ride_type": "roller_coaster",
        "patrons": [
            {"height_cm": 150, "health_warning": True},
            {"height_cm": 150}
        ]
    }]
    result = process_ride_admissions(groups, 5.0)
    assert result["total_revenue"] == 0.0


def test_fast_lane_fee():
    groups = [{
        "is_open": True,
        "ride_type": "family",
        "has_fast_lane": True,
        "patrons": [{"height_cm": 150}]
    }]
    result = process_ride_admissions(groups, 5.0)
    assert result["total_revenue"] == 15.0


def test_safety_audit():
    patrons = [{"height_cm": 0} for _ in range(5)]
    patrons.append({"height_cm": 150})

    groups = [{
        "is_open": True,
        "ride_type": "family",
        "patrons": patrons
    }]

    result = process_ride_admissions(groups, 5.0)
    assert result["status"] == "SAFETY_AUDIT"


# -------------------------------
# INSPECT SAFETY RESTRAINTS TESTS
# -------------------------------

def test_no_sensor_data():
    assert inspect_safety_restraints([]) == "NO_DATA"


def test_empty_sensor_readings():
    assert inspect_safety_restraints([[]]) == "SAFE"


def test_single_unlatched_reading():
    assert inspect_safety_restraints([[0]]) == "SAFE"


def test_emergency_lock():
    assert inspect_safety_restraints([[0, 0]]) == "EMERGENCY_LOCK"


def test_latched_sensor_resets_streak():
    assert inspect_safety_restraints([[0, 1, 0]]) == "SAFE"


def test_multiple_sensor_streams():
    assert inspect_safety_restraints([[0], [0]]) == "SAFE"
