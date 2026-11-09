"""Minimalny punkt startowy backendu SoundScope."""

from fastapi import FastAPI

app = FastAPI(title="SoundScope API")


@app.get("/health")
def health_check() -> dict[str, str]:
    """Zwraca prostą informację, że API odpowiada."""
    return {"status": "ok"}
