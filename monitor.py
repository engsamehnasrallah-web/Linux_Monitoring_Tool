import socket
import psutil
import platform

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
    # OS Information
os_name = platform.system()
os_version = platform.release()
architecture = platform.machine()

print(f"\nOperating System: {os_name} {os_version}")
print(f"Architecture: {architecture}")

    # CPU Usage
physical_cores = psutil.cpu_count(logical=False)
logical_cores = psutil.cpu_count(logical=True)
cpu = psutil.cpu_percent(interval=1)

print(f"Physical Cores: {physical_cores}")
print(f"Logical Cores: {logical_cores}")
print(f"\nCPU Usage: {cpu}%")

    # Memory Usage
memory = psutil.virtual_memory()
total_ram = memory.total / (1024 ** 3)
used_ram = memory.used / (1024 ** 3)

print(f"Memory Usage: {memory.percent}%")
print(f"Total RAM: {total_ram:.2f} GB")
print(f"Used RAM: {used_ram:.2f} GB")

    # Disk Usage
disk = psutil.disk_usage('/')
print(f"Disk Usage: {disk.percent}%")

# Generate Report
with open("system_report.txt", "w") as report:
    report.write("Linux Monitoring Tool Report\n")
    report.write("=" * 30 + "\n")
    report.write(f"Hostname: {hostname}\n")
    report.write(f"IP Address: {ipaddress}\n")
    report.write(f"Operating System: {os_name} {os_version}\n")
    report.write(f"Architecture: {architecture}\n")
    report.write(f"Physical Cores: {physical_cores}\n")
    report.write(f"Logical Cores: {logical_cores}\n")
    report.write(f"CPU Usage: {cpu}%\n")
    report.write(f"Memory Usage: {memory.percent}%\n")
    report.write(f"Total RAM: {total_ram:.2f} GB\n")
    report.write(f"Used RAM: {used_ram:.2f} GB\n")
    report.write(f"Disk Usage: {disk.percent}%\n")

input("\nPress Enter to exit...")