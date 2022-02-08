from brownie import accounts, SimpleStorage, config, network

def deploy_simple_storage():
    # account = accounts[0]                         # For Development server/network
    account = get_account()                         # For real Network


    # print(account)
    # account = accounts.load("abhijit_account")
    # print(account)
    
    # There are many ways to keep private key in .env etc..learn at https://youtu.be/M576WGiDBdQ?t=16796

    simple_storage = SimpleStorage.deploy({"from":account})
    # Transaction            // brownie smart enough to understand this is transaction
    # Call

    stored_value = simple_storage.retrieve()      # this is reading only (view function)
    print(stored_value )

    transaction = simple_storage.store(15, {"from":account} )    # Here we are updating state in blockchain
    transaction.wait(1)                                          # How many blocks we want to 
    updated_stored_value = simple_storage.retrieve() 
    print(updated_stored_value)


def get_account():
    if network.show_active() == "development":                              # Devlopment enviormnet will use ganache accounts
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])                  # For real networks we will use our real wallet (test wallet)

def main():
    deploy_simple_storage()