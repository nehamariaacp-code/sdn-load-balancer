#!/usr/bin/env python3
import socket
import threading
import sys
import time

def handle_client(conn, addr, server_id, delay):
    try:
        data = conn.recv(1024).decode('utf-8')
        if data:
            # Simulate asymmetric processing workload
            if delay > 0:
                time.sleep(delay)
            response = f"[REPLY FROM {server_id}] Processed: '{data.strip()}' (delay: {delay}s)\n"
            conn.sendall(response.encode('utf-8'))
    except Exception as e:
        print(f"[{server_id}] Connection error: {e}")
    finally:
        conn.close()

def start_server(host, port, server_id, delay):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(128)
    print(f"[{server_id}] TCP Server listening on {host}:{port} with synthetic delay {delay}s...")

    try:
        while True:
            conn, addr = sock.accept()
            threading.Thread(target=handle_client, args=(conn, addr, server_id, delay), daemon=True).start()
    except KeyboardInterrupt:
        print(f"\n[{server_id}] Server halted.")
    finally:
        sock.close()

if __name__ == '__main__':
    ip = sys.argv[1]
    port = int(sys.argv[2])
    name = sys.argv[3] if len(sys.argv) > 3 else f"Server-{ip}"
    delay = float(sys.argv[4]) if len(sys.argv) > 4 else 0.05
    start_server(ip, port, name, delay)
#!/usr/bin/env python3
import socket
import threading
import sys
import time

def handle_client(conn, addr, server_id):
    try:
        data = conn.recv(1024).decode('utf-8')
        if data:
            time.sleep(0.05)
            response = f"[REPLY FROM {server_id}] Processed: '{data.strip()}'\n"
            conn.sendall(response.encode('utf-8'))
    except Exception as e:
        print(f"[{server_id}] Connection error: {e}")
    finally:
        conn.close()

def start_server(host, port, server_id):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    sock.bind((host, port))
    sock.listen(128)
    print(f"[{server_id}] TCP Server listening on {host}:{port}...")

    try:
        while True:
            conn, addr = sock.accept()
            t = threading.Thread(target=handle_client, args=(conn, addr, server_id), daemon=True)
            t.start()
    except KeyboardInterrupt:
        print(f"\n[{server_id}] Stopped.")
    finally:
        sock.close()

if __name__ == '__main__':
    if len(sys.argv) < 3:
        print("Usage: python3 server.py <IP> <PORT> [SERVER_NAME]")
        sys.exit(1)
    
    ip = sys.argv[1]
    port = int(sys.argv[2])
    name = sys.argv[3] if len(sys.argv) > 3 else f"Server-{ip}"
    start_server(ip, port, name)
