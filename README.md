# AI-Driven Adaptive Data Center Network Optimizer

## Overview
This project implements a cloud-hosted Software-Defined Networking (SDN) controller and a complete monitoring pipeline for real-time data center telemetry. The objective is to build the operational foundation required for an AI-driven routing optimizer that detects congestion and dynamically adjusts traffic paths to improve network performance.

The system is deployed on a Google Cloud Compute VM (Ubuntu 22.04) and uses Docker containers to run ONOS, Prometheus, Grafana, and a custom Python-based metrics exporter. Metrics from ONOS are extracted through its REST API, normalized, and exposed to Prometheus in text format. Grafana dashboards provide live visual monitoring.

---

## System Components

### Cloud Infrastructure
- Google Cloud Compute Engine VM (Ubuntu 22.04)
- Public IP address used for external access

### Docker Services
| Component | Description |
|----------|------------|
| ONOS SDN Controller | Exposes network metrics and manages device mastership and topology tables |
| Metrics Exporter (Flask) | Converts ONOS REST API metrics to Prometheus-compatible format |
| Prometheus | Scrapes metrics and stores them in a time-series database |
| Grafana | Renders the collected metrics through dashboards |
| Private Docker Network (sdnnet) | Allows internal communication between components |

---

## Mapping to Course Requirements

The project uses six valid datacenter software components:

1. Software Defined Networking: ONOS manages the virtual network
2. RPC/API Interfaces: JSON REST communication with ONOS metrics endpoint
3. Message Marshalling and Encoding: ONOS JSON metrics converted into Prometheus text format
4. Databases: Prometheus internal time-series storage
5. Virtual Machines and Containers: Full deployment within Docker containers on a GCP VM
6. Monitoring Systems: Prometheus for scraping and Grafana for visualization

---
## Verification of System Operation

### ONOS Metrics via REST
```bash
curl -u onos:rocks http://<external_ip>:8181/onos/v1/metrics

Expected output:

{
  "metrics":[
    {
      "name":"Mastership.requestRole.responseTime",
      "metric":{"timer":{"counter":0,"mean":0.0}}
    }
  ]
}
## Exporter Endpoint

```bash
curl http://localhost:9000/metrics

Expected output:

onos_up 1
onos_error 0
Mastership_requestRole_responseTime 0

## Prometheus Target Health
curl http://localhost:9090/api/v1/targets


Expected:

exporter:9000 listed with health status "up"

onos:8181 listed as active scrape target
