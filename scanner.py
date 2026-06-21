import socket
import errno
from pathlib import Path
import os
import time
import sys

well_known_ports = [20,21,22,23,25,53,80,110,123,143,443]

def take_input():
    addr = input("Enter the IP address or domain: ")
    try:
        start_port = int(input("Enter the starting port: "))
        end_port = int(input("Enter the ending port: "))
    except:
        print("Enter integer port numbers.")
        sys.exit(1)
    
    if start_port > end_port or start_port < 0 or end_port > 65535:
        print("Enter proper ports between 0-65535.")
        sys.exit(1)
    
    closed_log_file = Path("PortScanner/closed_ports.log")
    opened_log_file = Path("PortScanner/opened_ports.log")

    closed_log_file.touch(exist_ok=True)
    opened_log_file.touch(exist_ok=True)
    return addr, start_port, end_port

def read_open_log():
    with open("PortScanner/opened_ports.log", "r") as f:
        lines = f.readlines()
        for line in lines:
            print(line.strip())

    return 

def switch(command):
    match(command):
        case "c":
            os.remove("PortScanner/closed_ports.log")
        case "o":
            os.remove("PortScanner/opened_ports.log")
        case "b":
            os.remove("PortScanner/opened_ports.log")
            os.remove("PortScanner/closed_ports.log")
        case "n":
            pass
        case _:
            print("Enter O/C/B/n only.")
            return 0
    return 1

def closed(port, result, close_count):
    close_count += 1
    if port in well_known_ports:
        error = errno.errorcode.get(result,"Unknown Error")
        with open("PortScanner/closed_ports.log", "a") as f:
            try:
                f.write(f"{time.strftime("%d/%b/%Y || %H:%M:%S")} || [CLOSE] : {port} ---> {socket.getservbyport(port)} || [ERROR] : {error}\n")
            except:
                f.write(f"{time.strftime("%d/%b/%Y || %H:%M:%S")} || [CLOSE] : {port} || [ERROR] : {error}\n")
    return close_count

def opened(port, open_count):
    open_count += 1
    with open("PortScanner/opened_ports.log", "a") as f:
        try:
            f.write(f"{time.strftime("%d/%b/%Y || %H:%M:%S")} || [OPEN] : {port} ---> {socket.getservbyport(port)}\n")

        except:
            f.write(f"{time.strftime("%d/%b/%Y || %H:%M:%S")} || [OPEN] : {port}\n")
    return open_count

def delete_log():
    while True:
        command = input("Delete the ports log file's content (O for open ports, C for close ports, B for both, n for none): ").strip().lower()
        if switch(command):
            break

def statistics(open_count, close_count, execution_time):
    print("="*4+" Statistical Data "+"="*4)
    print(f"Open Ports: {open_count}")
    print(f"Close Ports: {close_count}")
    print(f"Scan Duration: {execution_time:.2f}sec")
    print("="*26)

def main():
    addr, start_port, end_port = take_input()
    open_count = 0
    close_count = 0
    start_time = time.time()
    for port in range(start_port,end_port+1):
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as ss:
            ss.settimeout(1.0)
            try:
                result = ss.connect_ex((addr,port))
            except :
                print(f"The IP/Domain does not exist.")
                return

            if result == 0:
                open_count = opened(port,open_count)

            else:
                close_count = closed(port, result, close_count)
    stop_time = time.time()
    execution_time = stop_time - start_time
    read_open_log()
    delete_log()
    statistics(open_count, close_count, execution_time)

main()