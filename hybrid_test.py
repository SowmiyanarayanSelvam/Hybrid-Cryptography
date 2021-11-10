from hybrid_encryption import HybridEncryption
from hybrid_decryption import HybridDecryption

print("                 Two Phase Hybrid Cryptography                   ")
print("_________________________________________________________________")
print("--------------------------Menu-----------------------------------")
print("1. Encryption")
print("2. Decryption")

switch = int(input("Enter your choice: "))
case = {
    1: HybridEncryption(),
    2: HybridDecryption()
}
