blockchain = []

def get_last_blockchain_value():
    """ Returns the last value of the blockchain """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]

def add_transaction(transaction_amount, last_transaction=[1]):
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])

def verify_blockchain():
    # block_index=0
    is_Valid=True
    for block_index in range(len(blockchain)):
        if block_index == 0:
            continue
        elif blockchain[block_index][0] == blockchain[block_index - 1]:
            is_Valid = True
        else:
            is_Valid = False
            break
    # for block in blockchain:
    #     if block_index == 0:
    #         block_index = block_index + 1
    #         continue
    #     elif block[0] == blockchain[block_index - 1]:
    #         is_Valid = True
    #     else:
    #         is_Valid = False
    #         break
    #     block_index = block_index + 1
    return is_Valid

def get_transaction_value():
    return float(input('Please enter the amount: '))

def get_user_input():
    return input("Your choice:")

def printing_blocks():
    for block in blockchain:
        print('outputting block')
        print(block)
    else:
        print('-' * 20)

waiting_for_input = True

while waiting_for_input:
    print("Please choose: ")
    print("1. I want to enter a transaction value")
    print("2. I want to print the blocks")
    print("3. Manipulate the chain")
    print("4. Quit")
    user_choice = get_user_input()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_transaction(tx_amount, get_last_blockchain_value())
    elif user_choice == '2':
        printing_blocks()
    elif user_choice == '3':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == '4':
        waiting_for_input = False
    else:
        print('Invalid choice. Choose again!')
    if not verify_blockchain():
        printing_blocks()
        print("Invalid Blockchain")
        break
else:
    print('User left!')

print('DONE')