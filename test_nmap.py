import nmap

nm = nmap.PortScanner()
nm.scan('127.0.0.1', arguments='-sn')

print("Hosts found:")
print(nm.all_hosts())