from brownie import accounts, SimpleStorage

def deploy_simple_storage():
    account = accounts[0]
    # print(account)
    # account = accounts.load("abhijit_account")
    # print(account)
    
    # There are many ways to keep private key in .env etc..learn at https://youtu.be/M576WGiDBdQ?t=16796

    simple_storage = SimpleStorage.deploy({"from":account})
    # Transaction            // brownie smart enough to understand this is transaction
    # Call
    print(simple_storage    )



def main():
    deploy_simple_storage()