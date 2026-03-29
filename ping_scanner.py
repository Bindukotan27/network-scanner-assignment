import subprocess
import platform
import time

# Step 1: Take input from user
host = input("Enter IP or hostname: ")

# Step 2: Detect OS and set parameter
param = "-n" if platform.system().lower() == "windows" else "-c"

try:
    # Step 3: Start time
    start = time.time()

    # Step 4: Execute ping command
    result = subprocess.run(
        ["ping", param, "1", host],
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True
    )

    # Step 5: End time
    end = time.time()

    # Step 6: Check result
    if result.returncode == 0:
        print("\n[+] Host is UP")
        print("Response Time:", round((end - start) * 1000, 2), "ms")
    else:
        print("\n[-] Host is DOWN")

# Step 7: Error handling
except Exception as e:
    print("[ERROR]", e)