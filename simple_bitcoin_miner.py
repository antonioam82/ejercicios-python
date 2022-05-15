import hashlib

#print(hashlib.sha256("Hello world".encode()).hexdigest())

NONCE_LIMIT = 100000000000

zeros = 4

def miner(block_number, transactions, previous_hash):
    for nonce in range(NONCE_LIMIT):
        base_text = str(block_number) + transactions + previous_hash + str(nonce)
        hash_try = hashlib.sha256(base_text.encode()).hexdigest()
        if hash_try.startswith('0' * zeros):
            print(f"Found Hash With Nonce: {nonce}")
            print(f"Hash: {hash_try}")
            return hash_try
    return -1


block_number = 24
transactions = "76123fcc2141"
previous_hash = "876de8756b967c87"

miner(block_number, transactions, previous_hash)
