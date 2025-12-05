# AI-Driven Adaptive Data Center Network Optimizer

## Overview
This project sets up a cloud-hosted Software-Defined Network (SDN) controller and a monitoring pipeline to collect real-time data center metrics. The goal is to build the operational foundation for an adaptive, AI-enhanced routing optimizer that detects congestion and applies routing updates dynamically.

At this stage, the system runs on a Google Cloud VM, deploys all core network components as Docker containers, exposes ONOS metrics through a custom exporter, and scrapes them with Prometheus for visualization in Grafana.

---

## Core Architecture

### Cloud Infrastructure
- **Google Cloud Compute VM** (Ubuntu 22.04)
- Public IP used to access ONOS metrics, Prometheus UI, and Grafana dashboard

### Containers / Services
| Component | Purpose |
|----------|---------|
| **ONOS SDN Controller** | Provides REST APIs and internal metrics for network state (Mastership, topology, packet flow paths, etc.) |
| **ONOS Metrics Exporter** (Flask) | Fetches ONOS metrics and exposes them in Prometheus format |
| **Prometheus** | Scrapes metrics from ONOS and the exporter container |
| **Grafana** | Visualizes metrics through dashboards |
| **Docker Network (sdnnet)** | Internal isolated network for inter-container communication |

---

## Why This Satisfies Course Requirements

Your project must use **four datacenter software components**.  
This implementation actually uses **six**:

✔ RPC / API Interfaces  
→ ONOS REST API calls at:  
`http://<external_ip>:8181/onos/v1/metrics`

✔ Message Marshalling  
→ JSON metrics from ONOS parsed and converted to Prometheus text format

✔ Database  
→ Prometheus embedded time-series database (TSDB)

✔ Virtual Machines / Containers  
→ GCP VM + Dockerized services (ONOS, exporter, Prometheus, Grafana)

✔ Software-Defined Networking  
→ ONOS SDN controller managing virtual data center topology

✔ Monitoring Stack  
→ Prometheus metric scraping, Grafana visualization

This alone meets and exceeds the requirement.

---

## Key Functional Demonstrations

### 1. ONOS Metrics Retrieval
```bash
curl -u onos:rocks http://<external_ip>:8181/onos/v1/metrics
