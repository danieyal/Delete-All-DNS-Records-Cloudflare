
# Cloudflare DNS Records Deletion Script

This repository contains a Python script to delete all DNS records for a specific zone in Cloudflare. This can be useful for managing and cleaning up DNS records programmatically.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- You have installed Python 3.x.
- You have installed the `requests` library. You can install it using pip:
  
  ```sh
  pip install requests
  ```
- You have a Cloudflare account with an API key and the zone ID for the DNS records you wish to delete.

## Getting Started

To get a local copy up and running, follow these simple steps.

### Installation

1. Clone the repo:
   ```sh
   git clone https://github.com/danieyal/Delete-All-DNS-Records-Cloudflare.git
   ```

2. Navigate to the project directory:
   ```sh
   cd Delete-All-DNS-Records-Cloudflare
   ```

3. Install the required Python packages:
   ```sh
   pip install requests
   ```

### Configuration

1. Open `delete_dns_records.py` in your favorite text editor.

2. Replace the placeholders with your actual Cloudflare API credentials:
   ```python
   api_key = 'YOUR_CLOUDFLARE_API_KEY'
   email = 'YOUR_CLOUDFLARE_EMAIL'
   zone_id = 'YOUR_ZONE_ID'
   ```

### Usage

Run the script to delete all DNS records in the specified Cloudflare zone:
```sh
python delete_all_dns_records_cloudflare.py
```

- This script will only delete 100 DNS entries at a time, so you might need to run it multiple times.

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgments

- [Cloudflare API Documentation](https://developers.cloudflare.com/dns/zone-setups/troubleshooting/delete-all-records/)
- [Requests: HTTP for Humans](https://requests.readthedocs.io/en/master/)
