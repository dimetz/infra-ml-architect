# Infra ML Architect

ML-driven system for infrastructure sizing and architecture design.

## Features

- Storage sizing (IOPS, RAID, disks)
- SAN selection (FC / iSCSI)
- Replication type (sync / async)
- Geo-distribution support
- Web UI (v2)

---

## Architecture

- Backend: FastAPI
- ML: RandomForest
- Frontend: HTML + JS
- Deployment: Docker

---

## Run project

### 1. Generate dataset

```bash
cd data
python generate_dataset.py
```
---

### 2. Train model

```bash
cd ../models
python train_model.py
```
---

### 3. Run services

```bash
cd ..
docker-compose up --build
```
---

## Access UI

- Open in browser:

```bash
http://localhost:3000
```
---

## UI Features

- Select workload type (OLTP / VDI / Analytics)
- Configure geo-distribution
- Set RPO and distance

Get:
- disk recommendation
- replication type
- SAN configuration

---
