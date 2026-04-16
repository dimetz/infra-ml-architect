# Infra ML Architect

ML-driven infrastructure sizing system:
- Storage (IOPS, RAID, disks)
- SAN (protocol, speed)
- Replication (sync/async)
- Geo-distribution

## Features
- Synthetic enterprise dataset
- ML model (RandomForest)
- FastAPI service

## Run

```bash
## python data/generate_dataset.py
## python models/train_model.py
docker-compose up --build

## Open

```bash
http://localhost:3000
