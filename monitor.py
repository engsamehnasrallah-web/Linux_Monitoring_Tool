import socket
import psutil

# Initial display
print("=" * 30)
print(" Linux Monitoring Tool")
print("=" * 30)

# Display User Information
hostname = socket.gethostname()
ipaddress = socket.gethostbyname(hostname)

print(f"\nHostname: {hostname}")
print(f"IP Address: {ipaddress}")

# Display System Information
    # CPU Usage
cpu = psutil.cpu_percent(interval=1)
print(f"\nCPU Usage: {cpu}%")

    # Memory Usage
memory = psutil.virtual_memory()
print(f"Memory Usage: {memory.percent}%")

    # Disk Usage
disk = psutil.disk_usage('/')
print(f"Disk Usage: {disk.percent}%")

input("\nPress Enter to exit...")