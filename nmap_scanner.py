import nmap

# Step 1: Take user input
target = input("Enter IP / Network (e.g., 127.0.0.1 or 192.168.1.0/24): ")

try:
    nm = nmap.PortScanner()

    print("\n[1] Host Discovery")
    nm.scan(hosts=target, arguments='-sn')
    print("Active Hosts:", nm.all_hosts())

    print("\n[2] Port Scanning")
    nm.scan(hosts=target, arguments='-sS')

    for host in nm.all_hosts():
        print(f"\nHost: {host}")
        for proto in nm[host].all_protocols():
            ports = nm[host][proto].keys()
            for port in ports:
                state = nm[host][proto][port]['state']
                print(f"Port {port}: {state}")

    print("\n[3] Service Detection")
    nm.scan(hosts=target, arguments='-sV')

    print("\n[4] OS Detection (Run as Administrator)")
    nm.scan(hosts=target, arguments='-O')

except Exception as e:
    print("[ERROR]", e)