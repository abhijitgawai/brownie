from brownie import SimpleStorage, accounts, config


def read_contract():
    # print(SimpleStorage[0])
    simple_storage = SimpleStorage[-1]          # -1 for most recent deployment

    # To interact with sm we need ABI and Address

    print(simple_storage.retrieve())

def main():
    read_contract() 