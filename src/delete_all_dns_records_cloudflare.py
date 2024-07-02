import requests
import json

# Cloudflare API credentials
api_key = 'YOUR_CLOUDFLARE_API_KEY'
email = 'YOUR_CLOUDFLARE_EMAIL'
zone_id = 'YOUR_ZONE_ID'

# Headers for authentication
headers = {
    'X-Auth-Email': email,
    'X-Auth-Key': api_key,
    'Content-Type': 'application/json'
}

# Step 1: Get all DNS records
url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records'
response = requests.get(url, headers=headers)
dns_records = response.json().get('result', [])

if not dns_records:
    print("No DNS records found.")
else:
    print(f"Found {len(dns_records)} DNS records. Deleting...")

    # Step 2: Delete each DNS record
    for record in dns_records:
        record_id = record['id']
        delete_url = f'https://api.cloudflare.com/client/v4/zones/{zone_id}/dns_records/{record_id}'
        delete_response = requests.delete(delete_url, headers=headers)
        
        if delete_response.status_code == 200:
            print(f"Deleted DNS record {record_id}")
        else:
            print(f"Failed to delete DNS record {record_id}. Error: {delete_response.text}")

print("Finished deleting DNS records.")
