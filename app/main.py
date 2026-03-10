from etl import fetch_data, transform_data
from db import init_db, load_data


def main():
    init_db()
    data = fetch_data()
    records = transform_data(data)
    load_data(records)
    print(f"Loaded {len(records)} CA chapters into database")


if __name__ == "__main__":
    main()
