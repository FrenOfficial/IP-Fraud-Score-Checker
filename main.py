import requests

def get_fraud_score(ip, hostname, username, key):
    url = f"https://{hostname}/{username}/?ip={ip}&key={key}"
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
hostname = "api11.scamalytics.com"  
username = "manticwhale"  
key = "822dacb006623db2f168d5c29b1c5050c876058071fc982496080f06fea35235"  
score, risk = get_fraud_score(ip, hostname, username, key)

if score and risk:
    print(f"Fraud Score: {score}")
    print(f"Fraud Risk: {risk}")
else:
    print("Unable to retrieve fraud score and risk.")
