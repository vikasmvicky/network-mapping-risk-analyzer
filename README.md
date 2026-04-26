# Network Mapping & Risk Analyzer

This project uses Nmap and Python to analyze open ports and identify potential security risks in a local network.

## Features
- Extracts open ports and services from Nmap output
- Classifies services into risk levels (Low, Medium, High)
- Detects exposed databases and file-sharing services
- Generates an overall system risk score

## Technologies Used
- Nmap
- Python (Regex, File Handling)

## How to Run
1. Run Nmap scan:
   nmap -sS -sV -oN scan.txt <target-ip>

2. Run analyzer:
   python analyzer.py

## Sample Output
- Detected multiple exposed services
- Risk Score: HIGH