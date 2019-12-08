#IMPORTAMOS LIBRERIAS.
import psutil
import platform
from datetime import datetime

#FUNCION PARA REPRESENTAR TAMAÑOS EN BITS.
def get_size(bytes, suffix="B"):
    factor = 1024
    for unit in ["", "K", "M", "G", "T", "P"]:
        if bytes < factor:
            return f"{bytes:.2f}{unit}{suffix}"
        bytes /= factor

#INFORMACIÓN BÁSICA DEL SISTEMA.
print("="*40, "System Information", "="*40)
uname = platform.uname()
print(f"System: {uname.system}")
print(f"Node Name: {uname.node}")
print(f"Release: {uname.release}")
print(f"Version: {uname.version}")
print(f"Machine: {uname.machine}")
print(f"Processor: {uname.processor}")

#INFORMACIÓN DE LA CPU
print("="*40, "CPU Info", "="*40)
#Nº NUCLEOS
print("Physical cores:", psutil.cpu_count(logical=False))
print("Total cores:", psutil.cpu_count(logical=True))
#FRECUENCIAS CPU
cpufreq = psutil.cpu_freq()
print(f"Max Frequency: {cpufreq.max:.2f}Mhz")
print(f"Min Frequency: {cpufreq.min:.2f}Mhz")
print(f"Current Frequency: {cpufreq.current:.2f}Mhz")
#USO DE CPU
print("CPU Usage Per Core:")
for i, percentage in enumerate(psutil.cpu_percent(percpu=True)):
    print(f"Core {i}: {percentage}%")
print(f"Total CPU Usage: {psutil.cpu_percent()}%")
#MEMORIA
print("="*40, "Memory Information", "="*40)
svmem = psutil.virtual_memory()
print(f"Total: {get_size(svmem.total)}")
print(f"Available: {get_size(svmem.available)}")
print(f"Used: {get_size(svmem.used)}")
print(f"Percentage: {svmem.percent}%")
print("="*20, "SWAP", "="*20)
swap = psutil.swap_memory()
print(f"Total: {get_size(swap.total)}")
print(f"Free: {get_size(swap.free)}")
print(f"Used: {get_size(swap.used)}")
print(f"Percentage: {swap.percent}%")
#INFORMACIÓN DEL DISCO DURO
print("="*40, "Disk Information", "="*40)
print("Partitions and Usage:")
partitions = psutil.disk_partitions()
for partition in partitions:
    print(f"=== Device: {partition.device} ===")
    print(f"  Mountpoint: {partition.mountpoint}")
    print(f"  File system type: {partition.fstype}")
    try:
        partition_usage = psutil.disk_usage(partition.mountpoint)
    except PermissionError:
        continue
    print(f"  Total Size: {get_size(partition_usage.total)}")
    print(f"  Used: {get_size(partition_usage.used)}")
    print(f"  Free: {get_size(partition_usage.free)}")
    print(f"  Percentage: {partition_usage.percent}%")
disk_io = psutil.disk_io_counters()
print(f"Total read: {get_size(disk_io.read_bytes)}")
print(f"Total write: {get_size(disk_io.write_bytes)}")
#INFORMACIÓN DE REDES
print("="*40, "Network Information", "="*40)
if_addrs = psutil.net_if_addrs()
for interface_name, interface_addresses in if_addrs.items():
    for address in interface_addresses:
        print(f"=== Interface: {interface_name} ===")
        if str(address.family) == 'AddressFamily.AF_INET':
            print(f"  IP Address: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast IP: {address.broadcast}")
        elif str(address.family) == 'AddressFamily.AF_PACKET':
            print(f"  MAC Address: {address.address}")
            print(f"  Netmask: {address.netmask}")
            print(f"  Broadcast MAC: {address.broadcast}")
net_io = psutil.net_io_counters()
print(f"Total Bytes Sent: {get_size(net_io.bytes_sent)}")
print(f"Total Bytes Received: {get_size(net_io.bytes_recv)}")
