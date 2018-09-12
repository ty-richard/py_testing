#Initializing our blockchain list
blockchain = []

def get_last_blockchain_value():
    """ Returns the last value in the blockchain. """
    return blockchain[-1]


def add_value(transaction_amount, last_transaction=[1]):
    """ Appends a new value to the blockchain as well as he last value

    Arguments:
        :transaction_amount: The amount that should be added.
        :last_transaction: The last blockchain transaction (default[1])

    """
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



tx_amount = get_transaction_value()
add_value(tx_amount)


while True:
    print('Please choose')
    print('1: Add a new transaction ')
    print('2: Output the blockchain blocks')
    user_choice = get_user_choice()
    if user_choice == '1':
        tx_amount = get_transaction_value()
        add_value(last_transaction=get_last_blockchain_value(), transaction_amount=tx_amount)
    elif user_choice == '2':
        print_blockchain_info()
    else:
        print('Choice was invalid, Please only use valid options.')


print('Done!')
