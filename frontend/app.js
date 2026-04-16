function buildArchitecture(input, prediction) {
    let replication = "none";

    if (input.geo === true && input.rpo === 0 && input.latency < 5) {
        replication = "sync";
    } else if (input.geo === true) {
        replication = "async";
    }

    let san = "iscsi";
    let sanSpeed = 10;

    if (input.iops > 20000) {
        san = "fc";
        sanSpeed = 32;
    } else if (input.iops < 5000) {
        sanSpeed = 1;
    }

    return {
        storage: `${prediction.recommended_disks} disks`,
        replication: replication,
        san: `${san.toUpperCase()} ${sanSpeed}Gb`,
    };
}

async function calculate() {
    const input = {
        workload: document.getElementById("workload").value,
        users: Number(document.getElementById("users").value),
        iops: Number(document.getElementById("iops").value),
        throughput: Number(document.getElementById("throughput").value),
        latency: Number(document.getElementById("latency").value),
        geo: document.getElementById("geo").value === "true",
        distance: Number(document.getElementById("distance").value),
        rpo: Number(document.getElementById("rpo").value)
    };

    const response = await fetch("http://localhost:8000/predict", {
        method: "POST",
        headers: {"Content-Type": "application/json"},
        body: JSON.stringify(input)
    });

    const data = await response.json();
    const arch = buildArchitecture(input, data);

    document.getElementById("result").innerHTML = `
        <h2>Result</h2>
        <p><b>Disks:</b> ${data.recommended_disks}</p>

        <h3>Architecture</h3>
        <p><b>Storage:</b> ${arch.storage}</p>
        <p><b>Replication:</b> ${arch.replication}</p>
        <p><b>SAN:</b> ${arch.san}</p>
    `;
}