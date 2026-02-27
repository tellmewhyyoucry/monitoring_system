from fastapi import FastAPI, UploadFile, File, Depends
from sqlalchemy.orm import Session
import pandas as pd
import matplotlib.pyplot as plt
from io import BytesIO
from fastapi.responses import StreamingResponse

from .database import SessionLocal, engine, Base
from .models import Telemetry
from .anomaly import detect_anomalies

Base.metadata.create_all(bind=engine)

app = FastAPI()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


@app.post("/upload/")
async def upload_csv(file: UploadFile = File(...), db: Session = Depends(get_db)):
    df = pd.read_csv(file.file)

    # Очистка
    df.dropna(inplace=True)
    df["timestamp"] = pd.to_datetime(df["timestamp"])

    for _, row in df.iterrows():
        record = Telemetry(
            timestamp=row["timestamp"],
            temperature=row["temperature"],
            pressure=row["pressure"]
        )
        db.add(record)

    db.commit()

    return {"message": "Data uploaded successfully"}


@app.get("/telemetry/")
def get_telemetry(db: Session = Depends(get_db)):
    data = db.query(Telemetry).all()
    alerts = detect_anomalies(data)
    return {"data": data, "alerts": alerts}


@app.get("/plot/")
def plot_data(db: Session = Depends(get_db)):
    data = db.query(Telemetry).all()

    timestamps = [d.timestamp for d in data]
    temps = [d.temperature for d in data]

    plt.figure()
    plt.plot(timestamps, temps)
    plt.title("Temperature over time")

    buf = BytesIO()
    plt.savefig(buf, format="png")
    buf.seek(0)

    return StreamingResponse(buf, media_type="image/png")