import requests
from config import DU_API_URL, TARGET_STATE


def fetch_data():
    response = requests.get(DU_API_URL, timeout=30)
    response.raise_for_status()
    return response.json()


def normalize_records(payload):
    if isinstance(payload, list):
        return payload

    if isinstance(payload, dict) and "features" in payload:
        normalized = []

        for feature in payload["features"]:
            attrs = feature.get("attributes", {}) or {}
            geom = feature.get("geometry", {}) or {}

            normalized.append(
                {
                    "id": attrs.get("id")
                    or attrs.get("chapter_id")
                    or attrs.get("OBJECTID"),
                    "name": attrs.get("name")
                    or attrs.get("chapter_name")
                    or attrs.get("Chapter_Name"),
                    "city": attrs.get("city") or attrs.get("City"),
                    "state": attrs.get("state") or attrs.get("State"),
                    "coordinates": {
                        "lat": geom.get("y")
                        or attrs.get("latitude")
                        or attrs.get("Latitude"),
                        "lng": geom.get("x")
                        or attrs.get("longitude")
                        or attrs.get("Longitude"),
                    },
                }
            )

        return normalized

    if isinstance(payload, dict) and "data" in payload and isinstance(payload["data"], list):
        return payload["data"]

    raise ValueError("Unsupported API response format")


def transform_data(payload):
    data = normalize_records(payload)
    result = []

    for record in data:
        if record.get("state") == TARGET_STATE:
            coords = record.get("coordinates") or {}

            result.append(
                {
                    "chapter_id": str(record.get("id")),
                    "chapter_name": record.get("name"),
                    "city": record.get("city"),
                    "state": record.get("state"),
                    "latitude": coords.get("lat"),
                    "longitude": coords.get("lng"),
                }
            )

    return result
