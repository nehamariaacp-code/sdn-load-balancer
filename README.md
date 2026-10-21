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

### Prerequisites

Use Ubuntu with Python 3, POX, Mininet, Open vSwitch, Matplotlib, and NumPy installed.

Clone the repository:

```bash
git clone https://github.com/nehamariaacp-code/sdn-load-balancer.git
cd sdn-load-balancer
```
### 1. Start the POX Controller
Copy the controller module into POX's `ext` directory.

For the adaptive load balancer:

```bash
cp ~/sdn_load_balancer/adaptive_lb.py ~/pox/ext/adaptive_lb.py
cd ~/pox
./pox.py openflow.of_01 --port=6633 adaptive_lb
```

Run only one controller at a time on port 6633.

For the Round Robin baseline, use this controller instead:

```bash
cp ~/sdn_load_balancer/lb_controller.py ~/pox/ext/lb_controller.py
cd ~/pox
./pox.py openflow.of_01 --port=6633 lb_controller
```

### 2. Start the Mininet Topology

Open a separate Ubuntu terminal and run:

```bash
sudo python3 ~/sdn_load_balancer/topo.py
```

The topology uses clients `h1` and `h2`, backend servers `h3`, `h4`, and `h5`, and virtual IP `10.0.0.100`.

### 3. Start the Backend Servers

From the Mininet CLI, open terminals for the three backend hosts:

```text
xterm h3 h4 h5
```

Run one command in each host terminal.

On `h3`:

```bash
python3 /home/neha/sdn_load_balancer/server.py 10.0.0.3 8000 Server-3 0.40
```

On `h4`:

```bash
python3 /home/neha/sdn_load_balancer/server.py 10.0.0.4 8000 Server-4 0.08
```

On `h5`:

```bash
python3 /home/neha/sdn_load_balancer/server.py 10.0.0.5 8000 Server-5 0.01
```

These delays simulate different backend processing times.

### 4. Run a Benchmark

From the Mininet CLI, run:

```text
h1 python3 /home/neha/sdn_load_balancer/benchmark.py 30 5 /home/neha/sdn_load_balancer/adaptive_results.csv
```

This runs 30 requests with a concurrency level of 5 and saves the results to `adaptive_results.csv`.

Run the same benchmark separately with the Round Robin controller, saving its results to `rr_results.csv`.

### 5. Generate the Performance Graph

From an Ubuntu terminal, run:

```bash
cd ~/sdn_load_balancer
python3 plot_metrics.py rr_results.csv adaptive_results.csv
```

The comparison graph is saved as `d2_performance_comparison.png`.



## Conclusion

The experiments demonstrate that adaptive server selection can improve response time under the tested synthetic server-delay conditions while maintaining successful request handling during the recorded failure test.
## Authors

This project was developed as a group project by:

- **Neha Maria Augustine**  PES1UG25CS332
- **[Om Swaroop]**
- **[Nishanth Basu]**

