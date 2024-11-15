import requests

def get_block_details(block_hash):
    url = f'https://api.blockcypher.com/v1/btc/main/blocks/{block_hash}'
    response = requests.get(url)
    data = response.json()
    return data

if __name__ == "__main__":
    block_hash = input("Enter the block hash: ")
    block_details = get_block_details(block_hash)
    
    print(f"Block Hash: {block_details['hash']}")
    print(f"Height: {block_details['height']}")
    print(f"Time: {block_details['time']}")
    print(f"Number of Transactions: {block_details['n_tx']}")
    print(f"Total Fees: {block_details['total_fees']} satoshis")
