async function calculate() {
    const users = document.getElementById("users").value;
    const iops = document.getElementById("iops").value;
    const throughput = document.getElementById("throughput").value;
    const latency = document.getElementById("latency").value;

    const response = await fetch("http://localhost:8000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            users: Number(users),
            iops: Number(iops),
            throughput: Number(throughput),
            latency: Number(latency)
        })
    });

    const data = await response.json();

    document.getElementById("result").innerHTML = `
        <h2>Result</h2>
        <p>Recommended disks: ${data.recommended_disks}</p>
        <p>${data.note}</p>
    `;
}