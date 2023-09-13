#!/usr/bin/python3
import requests
import os
hostname = os.environ.get("SCAMALYTICS_API_HOSTNAME")
key = os.environ.get("SCAMALYTICS_API_KEY")
username = os.environ.get("SCAMALYTICS_USERNAME")
def get_fraud_score(ip):
    url = f"{hostname}/{username}/?key={key}&ip={ip}"
    response = requests.get(url)
    if response.status_code == 200:
        fraud_data = response.json()
        if fraud_data['status'] == 'ok':
            return fraud_data['score'], fraud_data['risk']
        else:
            return None, None
    else:
        return None, None

ip = input("Enter the IP address: ")
score, risk = get_fraud_score(ip)

if score and risk:
    print(f"Fraud Score: {score}")
    print(f"Fraud Risk: {risk}")
else:
    print("Unable to retrieve fraud score and risk.")
