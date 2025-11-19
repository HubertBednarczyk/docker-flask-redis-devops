from flask import Flask
from datetime import datetime
import redis
import os

app = Flask(__name__)

# host i port bierzemy z ENV (domyślnie: redis:6379)
REDIS_HOST = os.getenv("REDIS_HOST", "redis")
REDIS_PORT = int(os.getenv("REDIS_PORT", "6379"))

r = redis.Redis(host=REDIS_HOST, port=REDIS_PORT, db=0)

@app.get("/")
def index():
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # inkrementujemy licznik
    visits = r.incr("visits")

    return (
        f"Siema, tu Hubert, to działa w Dockerze + Redis!<br>"
        f"Czas serwera: {now}<br>"
        f"Licznik odwiedzin: {visits}<br>"
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
