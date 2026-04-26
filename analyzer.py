import re

# Step 1: Read scan file
with open("scan.txt", "r") as file:
    data = file.read()

# Step 2: Extract ports and services
ports = re.findall(r"(\d+)/tcp\s+open\s+([\w\-]+)", data)

# Step 3: Print extracted data
print("=== Open Ports & Services ===\n")

for port, service in ports:
    print(f"Port {port} → {service}")

# Step 4: Risk Analysis
risk_score = 0

print("\n=== Security Analysis ===\n")

for port, service in ports:
    if port in ["139", "445"]:
        print(f" Port {port}: Windows File Sharing (HIGH RISK)")
        risk_score += 3
    elif port in ["3306", "5432"]:
        print(f" Port {port}: Database Service Exposed (MEDIUM RISK)")
        risk_score += 2
    elif port == "5500":
        print(f" Port 5500: Unknown → Likely Web App (INVESTIGATE)")
        risk_score += 2
    else:
        print(f" Port {port}: Standard Service (LOW RISK)")
        risk_score += 1

# Step 5: Final Score
print("\n=== Overall Risk Score ===")
print(f"Total Risk Score: {risk_score}")

if risk_score >= 10:
    print(" System Risk Level: HIGH")
elif risk_score >= 6:
    print(" System Risk Level: MEDIUM")
else:
    print(" System Risk Level: LOW")