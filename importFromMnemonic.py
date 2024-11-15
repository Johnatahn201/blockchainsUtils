from mnemonic import Mnemonic
from bip32 import BIP32

def import_wallet_from_mnemonic(mnemonic_phrase):
    mnemo = Mnemonic("english")
    if not mnemo.check(mnemonic_phrase):
        print("Invalid mnemonic phrase.")
        return None
    seed = mnemo.to_seed(mnemonic_phrase)
    bip32 = BIP32.from_seed(seed)
    return bip32

if __name__ == "__main__":
    mnemonic_phrase = input("Enter your mnemonic phrase: ")
    bip32 = import_wallet_from_mnemonic(mnemonic_phrase)
    if bip32:
        print(f"Wallet imported successfully. Public Key: {bip32.get_public_key_from_path("m/44'/0'/0'/0/0")}")
