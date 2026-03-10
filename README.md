# Ducks Unlimited University Chapters ETL

This project implements a production-style ETL pipeline that:

- queries the Ducks Unlimited university chapters dataset
- filters California (`CA`) chapters
- stores the result in PostgreSQL
- runs locally via Docker Compose

## Data fields

- chapter_id
- chapter_name
- city
- state
- latitude
- longitude

## Run locally

```bash
docker compose up --build
