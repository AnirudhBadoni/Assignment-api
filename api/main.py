from fastapi import FastAPI, Request
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST
from fastapi.responses import Response

app = FastAPI()

# Prometheus counter
request_counter = Counter('http_requests_total', 'Total HTTP requests')

@app.post("/api")
async def handle_request(request: Request):
    request_counter.inc()

    headers = dict(request.headers)
    method = request.method
    try:
        body = await request.json()
    except Exception:
        body = "No JSON body"

    return {
        "message": "Welcome to our demo API, here are the details of your request:",
        "headers": headers,
        "method": method,
        "body": body
    }

@app.get("/metrics")
def metrics():
    return Response(generate_latest(), media_type=CONTENT_TYPE_LATEST)
