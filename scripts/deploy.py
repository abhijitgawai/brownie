from brownie import accounts

def deploy_simple_storage():
    account = accounts[0]
    print(account)
    pass

def main():
    deploy_simple_storage()