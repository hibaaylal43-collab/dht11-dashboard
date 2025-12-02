async function loadTempHistory() {
    try {
        const res = await fetch("/api/");
        const json = await res.json();

        const labels = json.data.map(row => new Date(row.dt).toLocaleTimeString());
        const temps = json.data.map(row => row.temp);

        const ctx = document.getElementById("tempChart");

        new Chart(ctx, {
            type: "line",
            data: {
                labels: labels,
                datasets: [{
                    label: "Température (°C)",
                    data: temps,
                    borderColor: "rgb(239, 68, 68)",
                    backgroundColor: "rgba(239, 68, 68, 0.1)",
                    borderWidth: 3,
                    fill: true,
                    tension: 0.4,
                    pointRadius: 4,
                    pointHoverRadius: 6,
                    pointBackgroundColor: "rgb(239, 68, 68)",
                    pointBorderColor: "#fff",
                    pointBorderWidth: 2
                }]
            },
            options: {
                responsive: true,
                maintainAspectRatio: false,
                plugins: {
                    legend: {
                        display: true,
                        position: 'top',
                        labels: {
                            font: {
                                size: 14,
                                weight: 'bold'
                            },
                            color: '#333'
                        }
                    },
                    title: {
                        display: true,
                        text: 'Historique de la Température',
                        font: {
                            size: 18,
                            weight: 'bold'
                        },
                        color: '#333',
                        padding: 20
                    }
                },
                scales: {
                    y: {
                        beginAtZero: false,
                        ticks: {
                            callback: function(value) {
                                return value + '°C';
                            },
                            font: {
                                size: 12
                            }
                        },
                        grid: {
                            color: 'rgba(0, 0, 0, 0.05)'
                        }
                    },
                    x: {
                        ticks: {
                            font: {
                                size: 11
                            },
                            maxRotation: 45,
                            minRotation: 45
                        },
                        grid: {
                            display: false
                        }
                    }
                },
                interaction: {
                    intersect: false,
                    mode: 'index'
                }
            }
        });
    } catch (error) {
        console.error("Erreur lors du chargement des données de température:", error);
        document.getElementById("tempChart").insertAdjacentHTML('beforebegin',
            '<div style="color: red; text-align: center; padding: 20px;">Erreur de chargement des données</div>'
        );
    }
}

loadTempHistory();