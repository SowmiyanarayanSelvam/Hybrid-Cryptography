import rsa

class RSA:

    def __init__(self,verbosity):
        self.pub_key, self.priv_key = rsa.newkeys(512)
        self.verbosity = verbosity
        if(self.verbosity):
            print("Object of class RSA created")

    def get_public_key(self):
        if(self.verbosity):
            print("Sending public key from RSA object: "+ str(self.pub_key))
        return self.pub_key

    def RSAencrypt(self, message, publickey):
        if(self.verbosity):
            print("Plain text has been RSA encrypted and returned")
        return rsa.encrypt(message, publickey)

    def RSAdecrypt(self, enc_message):
        if(self.verbosity):
            print("Cipher text has been RSA decrypted and returned")
        return rsa.decrypt(enc_message, self.priv_key)