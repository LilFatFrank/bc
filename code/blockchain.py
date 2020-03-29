blockchain = [[1]]

def get_last_blockchain_value():
    """ Returns the last value of the blockchain """
    return blockchain[-1]

def add_value(transaction_amount, last_transaction = [1]):
    blockchain.append([last_transaction, transaction_amount])

def get_transaction_amount():
    return float(input('Please enter the amount: '))

tx_amount=get_transaction_amount()
add_value(tx_amount)
tx_amount=get_transaction_amount()
add_value(last_transaction=get_last_blockchain_value(),
          transaction_amount=tx_amount)
tx_amount=get_transaction_amount()
add_value(tx_amount, get_last_blockchain_value())

print(blockchain)