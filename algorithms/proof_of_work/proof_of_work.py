# import sha256
from hashlib import sha256

new_transactions = [{'amount': '30', 'sender':'alice', 'receiver':'bob'},{'amount': '55', 'sender':'bob', 'receiver':'alice'}]

# This function will find a hash that has the required amount of leading zeros.
def pow(transactions, difficulty):
    nonce = 0
    proof = sha256((str(nonce) + str(transactions)).encode()).hexdigest()
    while proof[:difficulty] != "0" * difficulty: 
        nonce += 1
        proof = sha256((str(nonce)+str(transactions)).encode()).hexdigest()
    return proof 

final_proof = pow(new_transactions, 3)

# Output the result that was found. 
print(f"final proof: {final_proof}")