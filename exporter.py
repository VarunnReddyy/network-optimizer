from flask import Flask, Response
import requests
import os

app = Flask(__name__)

ONOS_HOST = os.getenv("ONOS_HOST", "onos")
ONOS_URL = f"http://{ONOS_HOST}:8181/onos/v1/metrics"
ONOS_USER = "onos"
ONOS_PASS = "rocks"

@app.route("/metrics")
def metrics():
    try:
        r = requests.get(ONOS_URL, auth=(ONOS_USER, ONOS_PASS), timeout=3)
        if r.status_code != 200:
            return Response(f"onos_up 0\nonos_error 1\n# HTTP status: {r.status_code}", mimetype="text/plain")

        data = r.json()

        output = ["onos_up 1", "onos_error 0"]
        for item in data.get("metrics", []):
            name = item["name"].replace(".", "_")
            value = item["metric"]["timer"]["counter"]
            output.append(f"{name} {value}")

        return Response("\n".join(output), mimetype="text/plain")

    except Exception as e:
        return Response(f"onos_up 0\nonos_error 1\n# Exception: {e}", mimetype="text/plain")

if __name__ == "__main__":
    print("Exporter started...")
    app.run(host="0.0.0.0", port=9000)






































