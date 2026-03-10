import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1] / "app"))

from etl import transform_data


def test_transform_data_filters_ca():
    sample = [
        {
            "id": 1,
            "name": "California Chapter",
            "city": "Los Angeles",
            "state": "CA",
            "coordinates": {"lat": 34.05, "lng": -118.24},
        },
        {
            "id": 2,
            "name": "Texas Chapter",
            "city": "Austin",
            "state": "TX",
            "coordinates": {"lat": 30.26, "lng": -97.74},
        },
    ]

    result = transform_data(sample)

    assert len(result) == 1
    assert result[0]["chapter_id"] == "1"
    assert result[0]["state"] == "CA"
