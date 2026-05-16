from flask import Flask
import redis
import os

app = Flask(__name__)

# Connect to Redis running on host machine
redis_host = os.environ.get("REDIS_HOST", "host.docker.internal")
redis_port = 6379

r = redis.Redis(host=redis_host, port=redis_port, decode_responses=True)

@app.route("/")
def home():
    try:
        # Increment visitor count
        visits = r.incr("counter")
        return f"""
        <h1>Flask + Redis App</h1>
        <h2>Visitor Count: {visits}</h2>
        <p>Connected to Redis on Host Port 6379</p>
        """
    except Exception as e:
        return f"Redis Connection Error: {e}"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
