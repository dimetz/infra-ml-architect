import random
import math
import json

def generate_record():
    workload = random.choice(["oltp", "vdi", "analytics"])

    users = random.randint(100, 5000)
    tps = random.randint(50, 1000)
    iops_user = random.randint(10, 30)

    block = random.choice([4, 8, 16, 64, 128, 256])
    read_ratio = round(random.uniform(0.5, 0.95), 2)
    write_ratio = round(1 - read_ratio, 2)

    latency_target = random.choice([2, 3, 5, 10, 20])
    data_size = round(random.uniform(0.5, 20), 1)
    growth = random.choice([0.2, 0.25, 0.3])

    if workload == "oltp":
        io_per_tx = random.randint(20, 30)
        iops = tps * io_per_tx

    elif workload == "vdi":
        iops = users * iops_user * 2  # peak

    else:  # analytics
        throughput = random.randint(200, 1000)
        iops = int((throughput * 1024) / block)

    throughput = round(iops * block / 1024, 1)

    # Storage
    if iops > 20000:
        storage = "nvme"
    elif iops > 5000:
        storage = "ssd"
    else:
        storage = "hdd"

    raid = "raid10" if workload in ["oltp", "vdi"] else "raid6"

    disk_iops = 80000 if storage == "nvme" else 20000
    disks = math.ceil(iops / disk_iops)
    disks = disks if disks % 2 == 0 else disks + 1

    # Geo / replication
    geo = random.choice([True, False])
    distance = random.choice([0, 50, 70, 150, 300])

    rpo = random.choice([0, 15, 60])
    rto = random.choice([1, 5, 10, 30])

    latency = distance * 0.005 + random.uniform(0.5, 1.5)

    if geo and rpo == 0 and latency < 5:
        replication = "sync"
    elif geo:
        replication = "async"
    else:
        replication = "none"

    write_iops = iops * write_ratio
    replication_bw = int(write_iops * block / 1024 * 2)

    # SAN
    if iops > 20000:
        san = "fc"
        san_speed = 32
    elif iops > 5000:
        san = "iscsi"
        san_speed = 10
    else:
        san = "iscsi"
        san_speed = 1

    return {
        "workload_type": workload,
        "users": users,
        "transactions_per_sec": tps,
        "block_size_kb": block,
        "read_ratio": read_ratio,
        "write_ratio": write_ratio,
        "latency_target_ms": latency_target,
        "data_size_tb": data_size,
        "growth_annual": growth,
        "required_iops": iops,
        "required_throughput_mb": throughput,
        "storage_type": storage,
        "raid_type": raid,
        "disk_count": disks,
        "geo_distribution": geo,
        "distance_km": distance,
        "rpo": rpo,
        "rto_min": rto,
        "replication_type": replication,
        "replication_bandwidth_mbps": replication_bw,
        "network_latency_ms": round(latency, 2),
        "san_protocol": san,
        "san_speed_gbps": san_speed,
        "san_fabrics": 2 if san != "iscsi" else 1,
        "multipath": True
    }


dataset = [generate_record() for _ in range(150)]

with open("dataset.json", "w") as f:
    json.dump(dataset, f, indent=2)

print("Dataset generated: 150 records")