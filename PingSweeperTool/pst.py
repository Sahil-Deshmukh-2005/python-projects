import subprocess
import sys
from pathlib import Path
import time
import os


path = Path("/home/sahil/Projects/ping sweep tool/active_host.log")
path.touch(exist_ok=True)

def validate(section):
    for octet in section:
        try:
            if int(octet) < 0 or int(octet) > 255:
                print("[ERROR] : IP not valid!")
                sys.exit(0)
        except:
            print("[ERROR] : IP should only be numbers.")
            sys.exit(0)

def statistics(active_count, result, section_start, section_end):
    total = int(section_end[-1])-int(section_start[-1])+1
    print("="*30)
    print(f"Total Hosts: {total}.")
    print(f"Total Active Hosts: {active_count}")
    print(f"Total Deactive Hosts: {total - active_count}")
    print(f"Scan Duration: {result.stdout.split(" ")[12].split("=")[1]}")
    print("="*30)

def ping_sweep_tool():

    starting_ip = input("Enter the starting IP address, ex., (10.1.1.1): ").strip().replace(" ", "")
    ending_ip = input("Enter the ending IP address, ex, (10.1.1.100): ").strip().replace(" ", "")

    section_start = starting_ip.split(".")
    section_end = ending_ip.split(".")

    if len(section_start) != 4 or len(section_end) != 4:
        return "[ERROR] : IP not valid!"
    
    validate(section_start)
    validate(section_end)

    active_count = 0

    if int(section_start[-1]) > int(section_end[-1]):
        return "[ERROR] : Starting IP cannot be greater than Ending IP."

    base_address = ".".join(section_start[0:3])

    with open(path, "a") as f:
        for ip in range(int(section_start[-1]), int(section_end[-1])+1):
            result = subprocess.run(["ping","-c","1",f"{base_address}.{ip}"], capture_output=True, text=True)
            if result.returncode == 0:
                active_count += 1
                f.write(f"{time.strftime("%d/%m/%Y || %H:%M:%S")} || Host with IP : {base_address}.{ip} is active.\n")

    statistics(active_count, result, section_start, section_end)
    
    return "Ping Sweep Done.✔️"

print(ping_sweep_tool())
os.remove("/home/sahil/Projects/ping sweep tool/active_host.log")
