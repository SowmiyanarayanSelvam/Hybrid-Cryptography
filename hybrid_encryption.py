#Project Authors: Sowmiyanarayan S, Dev Mithran J

#HYBRID CRYPTOSYSTEM USES COMBINATION OF MD5, ECC, RSA AND AES
#MESSAGE IS PADDED
#KEY PASSED IS ECC ENCRYPTED AND THEN PADDED OR REDUCED TO 256 BITS
#FIRST HALF OF MESSAGE IS ENCRYPTED USING AES AND THE ENCRYPTED KEY
#SECOND HALF IS ENCRYPTED USING RSA



import hashlib
import pyaes
import rsa
import ECC
import RSA
from Crypto.Util.Padding import pad
from sympy import isprime
import random


maxPrime = 10000
minPrime = 1000
primeLot = [i for i in range(minPrime,maxPrime) if isprime(i)]

class HybridEncryption:

    def __init__(self, verbosity = False):
        self.verbosity = verbosity
        if(self.verbosity):
            print("Creating new Hybrid Encryption object")
        self.rsaEntity = RSA.RSA(self.verbosity)
        self.eccEntity = ECC.ECC(self.verbosity)

    def getPublicKey(self):

        pubkey = self.rsaEntity.get_public_key()
        if(self.verbosity):
            print("Sending public key from Hybrid Encryption object: " + str(pubkey))
        return pubkey

    def hybEncrypt(self,message,key,pubkey):
        # message - Plain text
        # key - secret key of AES encryption


        message = message.encode('utf-8')           #Converting message to binary
        key = key.encode('utf-8')                   #converting key to binary

        if(self.verbosity):
            print("Message and key encoded")

        message = pad(message,16)                   #Padding to 128 bit block
        if(self.verbosity):
            print("Message padded")

        enc_key = self.eccEntity.ECCencrypt(key, self.eccEntity.get_public_key())    #Encrypting key using ECC

        len_k = len(enc_key)                                               #Padding to 256 bits
        if(len_k<32):
            enc_key = pad(enc_key,32)
        elif(len_k>32):
            enc_key = enc_key[:32]

        if(self.verbosity):
            print("Encrypted key padded")

        halfpoint = len(message)//2
        aes = pyaes.AESModeOfOperationCTR(enc_key)                          #Encrypting first half with AES
        enc_message1 = aes.encrypt(message[:halfpoint])
        if(self.verbosity):
            print("First half of message AES Encrypted")
        hash1 = hashlib.md5(enc_message1).digest()
        if(self.verbosity):
            print("First half of message hashed")


        enc_message2 = self.rsaEntity.RSAencrypt(message[halfpoint:], pubkey)
        if(self.verbosity):
            print("First half of message encrypted")
        hash2 = hashlib.md5(enc_message2).digest()
        if(self.verbosity):
            print("Second half of message hashed")
        return enc_message1, enc_message2, hash1+hash2, enc_key           #final set of parameters that shall be returned

    def checkHash(self, enc1, enc2, hash):
        if(self.verbosity):
            print("Comparing Hash")
        return (hash == (hashlib.md5(enc1).digest()+hashlib.md5(enc2).digest()))

    def hybDecrypt(self, enc1, enc2, hash, enc_key):

        if(not self.checkHash(enc1, enc2, hash)):
            return "Error! Message corrupted during transit!"

        if(self.verbosity):
            print("Message hash check successful!")
        aes = pyaes.AESModeOfOperationCTR(enc_key)                          #Decrypting first half with AES
        message1 = aes.decrypt(enc1)
        if(self.verbosity):
            print("First half of message decrypted")
        message2 = self.rsaEntity.RSAdecrypt(enc2)
        if(self.verbosity):
            print("Second half of message decrypted")

        message = (message1 + message2).decode('utf-8')
        if(self.verbosity):
            print("Message compiled")

        return message[:-1]                                                      #Returning decrypted message. Last special appended character is removed


    
HE1 = HybridEncryption(verbosity=True)
HE2 = HybridEncryption(verbosity=True)
m1, m2, hash, key = HE1.hybEncrypt("Hello there. I am Mithran. I am trying to use a message here. So let's see what happens.", "this is a key", HE2.getPublicKey())
print(HE2.hybDecrypt(m1, m2, hash, key))




























    # i=0
    # m = message[:n/2]
    
    # while(i<n/2):
    #     for j in range(n):
    #         k1 =ECCencrypt (TCPK, (ki−1))
    #     ci =E AES(k1,Bi)
    #     di = MD5 (ci)
    #     i+=1
    # i=(n/2)

    # #Let p and q two large prime numbers
    # x = p * q
    # phi(x)=(p − 1) * (q − 1)

    # #Let d a relatively prime number to φ(phi)
    # e * d = 1 % phi(x)

    # #Let (e, x) public key of DUAL RSA.
    # while(i<n):
    #     Mi = m[n//2+1:n]
    #     Ri =(Bi) e % x
    #     Li =ASCII (Bi)
    #     Ci =(Ri) XOR (Li)
    #     Di = MD5 (Ci)
    #     i+=1
    
    # Q =ci +Ci #cipher text
    # H =di + Di #hashed value
    
    # return (Q,H)