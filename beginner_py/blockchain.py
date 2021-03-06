#Initializing our blockchain list
blockchain = []

def get_last_blockchain_value():
    """ Returns the last value in the blockchain. """
    if len(blockchain) < 1:
        return None
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """ Appends a new value to the blockchain as well as he last value

    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The last blockchain transaction (default[1])

    """
    if last_transaction == None:
        last_transaction = [1]
    blockchain.append([last_transaction, transaction_amount])


def get_transaction_value():
    user_input = float(input('Enter new block: '))
    return user_input


def get_user_choice():
    user_input = input('Your choice: ')
    return user_input


def print_blockchain_info():
    #Output a list of the blockchain
    for block in blockchain:
        print('Outputting blockchain information')
        print(block)
    else:
        print('-' * 20)


def verify_chain():
    block_index = 0
    is_valid = True
    for block in blockchain:
        if block_index == 0:
            block_index += 1
            continue
        elif block[0] == blockchain[block_index - 1]:
            is_valid = True
        else:
            is_valid = False
            break
        block_index += 1
    return is_valid


tx_amount = get_transaction_value()
add_value(tx_amount)

waiting_for_input = True


while waiting_for_input:
    print('Please choose')
    print('1: Add a new transaction ')
    print('2: Output the blockchain blocks')
    print('h: Manipulate the chain')
    print('q: Quit')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)
    elif user_choice == '2':
        print_blockchain_info()
    elif user_choice == 'h':
        if len(blockchain) >= 1:
            blockchain[0] = [2]
    elif user_choice == 'q':
        waiting_for_input = False
    else:
        print('Choice was invalid, Please only use valid options.')
    if not verify_chain():
        print('Invalid block!')
        break
else:
    print('User left!')


print('Done!')
