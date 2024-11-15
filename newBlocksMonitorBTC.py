import requests
import time

def get_latest_block():
    url = 'https://api.blockcypher.com/v1/btc/main'
    response = requests.get(url)
    data = response.json()
    return data['height'], data['hash']

if __name__ == "__main__":
    last_height, last_hash = get_latest_block()
    print(f"Monitoring new blocks... (Current Height: {last_height})")

    while True:
        current_height, current_hash = get_latest_block()
        if current_height > last_height:
            print(f"New Block Detected! Height: {current_height}, Hash: {current_hash}")
            last_height = current_height
            last_hash = current_hash
        time.sleep(10)  # Check every 10 seconds
