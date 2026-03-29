import subprocess

try:
    print("\n[+] Fetching ARP Table...\n")

    # Run ARP command
    result = subprocess.run(
        "arp -a",
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Check if command executed successfully
    if result.returncode == 0:
        print(result.stdout)
    else:
        print("[ERROR] Unable to retrieve ARP table")

except Exception as e:
    print("[ERROR]", e)