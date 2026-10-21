# SDN Adaptive Load Balancer

## Project Overview

This project implements and evaluates a Software-Defined Networking (SDN) load balancer using the POX controller, Mininet, and Open vSwitch.

It compares a Round Robin load-balancing approach with an adaptive load balancer that considers server load and availability when distributing TCP requests.

## Technologies Used

- Python 3
- POX SDN controller
- Mininet network emulator
- Open vSwitch
- TCP client-server applications
- CSV-based performance measurements
- Matplotlib for plotting results

## Project Files

- `adaptive_lb.py` — Adaptive load-balancing controller.
- `lb_controller.py` — Load-balancing controller for the baseline approach.
- `server.py` — Backend TCP server application.
- `topo.py` — Mininet network topology.
- `benchmark.py` — Benchmarking client used to generate requests and record response times.
- `health_monitor.py` — Server health monitoring support.
- `plot_metrics.py` — Script for plotting performance metrics.
- `rr_results.csv` — Round Robin benchmark results.
- `adaptive_results.csv` — Adaptive load-balancer benchmark results.
- `rr_results_final.csv` — Final Round Robin benchmark results.
- `adaptive_results_final.csv` — Final adaptive benchmark results.
- `d2_performance_comparison.png` — Performance comparison graph.

## Experimental Setup

The experiment uses a Mininet topology with client hosts and three backend TCP servers. The load balancer distributes client requests through a virtual IP address.

The tests include request distribution, response-time measurement, concurrent requests, server overload monitoring, and server-failure handling.

## Final Performance Results

| Metric | Round Robin | Adaptive Load Balancer |
|---|---:|---:|
| Requests tested | 30 | 30 |
| Successful requests | 30/30 | 30/30 |
| Average response time | 173.78 ms | 60.64 ms |

In the recorded experiment, the adaptive load balancer reduced average response time by approximately 65.1% compared with Round Robin.

The adaptive test distributed requests according to the observed conditions rather than evenly across all servers.

## Additional Tests

- Concurrent-request test: 20 out of 20 requests succeeded at concurrency 10.
- Server-failure test: 10 out of 10 requests succeeded when Server-3 was unavailable, with traffic routed to the remaining servers.

These results describe the recorded test runs and may vary with system load and experimental conditions.

## Running the Project

Run the experiments from the Ubuntu environment configured with POX, Mininet, and Open vSwitch.

1. Start the Mininet topology using `topo.py`.
2. Start the appropriate POX controller module.
3. Start the backend TCP servers.
4. Run `benchmark.py` to generate requests and collect response-time measurements.
5. Use `plot_metrics.py` to generate performance visualizations.

Exact commands may depend on the local POX and Mininet configuration.

## Conclusion

The experiments demonstrate that adaptive server selection can improve response time under the tested synthetic server-delay conditions while maintaining successful request handling during the recorded failure test.
