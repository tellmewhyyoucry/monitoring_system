def detect_anomalies(data):
    alerts = []

    for i in range(len(data)):
        row = data[i]

        # Температура выше порога
        if row.temperature > 100:
            alerts.append(f"High temperature at {row.timestamp}")

        # Резкий скачок давления
        if i > 0:
            prev = data[i - 1]
            if abs(row.pressure - prev.pressure) > 3:
                alerts.append(f"Pressure spike at {row.timestamp}")

    return alerts