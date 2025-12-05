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
## Exporter Logic Summary

- Sends HTTP requests to the ONOS REST metrics API  
- Parses JSON responses returned by ONOS  
- Extracts timer-based internal metrics  
- Reformats the data into Prometheus-compatible text format  
- Serves the metrics through the `/metrics` endpoint on port `9000`

### Metrics Published
- `onos_up`
- `onos_error`
- `Mastership_requestRole_responseTime`

---

## Current Status

The monitoring and telemetry components are fully implemented and functioning:

- ONOS is reachable through its REST interface  
- The exporter successfully converts ONOS metrics into Prometheus format  
- Prometheus scrapes metrics from the exporter container  
- Grafana dashboards display the collected data  
- Deployment is hosted on a Google Cloud VM  
- Source code is maintained on GitHub

---
## Running the Project Using Docker Compose

This project is fully containerized. The entire monitoring stack can be started using Docker Compose.

### Prerequisites
Ensure the following are installed on the host machine:
- Docker
- Docker Compose

To verify:

`docker --version
docker compose version`

## Build and Start the Stack
From inside the project directory:
`docker compose up -d --build`

This command:
- builds the exporter image
- launches ONOS, Prometheus, Grafana, and the exporter

## Verify Running Containers:
`docker ps`

Expected containers:
- onos
- exporter
- prometheus
- grafana

## Verifying Component Status
1. Confirm Prometheus Targets
curl http://localhost:9090/api/v1/targets

Expected result:
- onos_exporter target should show "health": "up"

2. Confirm Exporter is Exporting Metrics
curl http://localhost:9000/metrics

Expected metrics:
onos_up 1
onos_error 0
Mastership_requestRole_responseTime 0

3. Confirm ONOS REST Metrics
curl -u onos:rocks http://<external_ip>:8181/onos/v1/metrics

Replace <external_ip> with the public VM IP if running on a cloud instance.

A JSON metrics response should be returned.

## Access Prometheus UI

Open a browser:

http://<external_ip>:9090

Access Grafana
http://<external_ip>:3000

Default login:

admin / admin

Add Prometheus Data Source in Grafana

In Grafana:

Settings → Data Sources

Add Prometheus

Use this endpoint:

http://prometheus:9090

## Recommended Grafana Metrics

Add panels for:
- onos_up
- onos_error
- Mastership_requestRole_responseTime

These values update in real time as Prometheus scrapes ONOS metrics through the exporter.
Stopping the Stack
docker compose down


---
## Future Extensions

Planned enhancements beyond the course submission:

- Integration of a reinforcement learning model for dynamic routing  
- Automated ONOS route updates through its REST API  
- Expansion of metric collection (latency thresholds, link utilization)  
- Traffic generation and benchmarking through Mininet  
- Performance comparison between static and AI-optimized routing strategies

## Project Participents
- Varun Reddy Mamidal
- Chandana Sunkara
  
