import hashlib
import pyaes    
def HybridEncryption(message,k,s): 
    # message Plain text
    # k secret key of AES encryption
    # s 128 bit size of block
    P = len(message)
    n=P/s
    i=0
    m = message[:n/2]
    
    while(i<n/2):
        for j in range(n):
            k1 =ECCenc (TCPK, ki−1)
        ci =E AES(k1,Bi)
        di = MD5 (ci)
        i+=1
    i=(n/2)

    #Let p and q two large prime numbers
    x = p * q
    phi(x)=(p − 1) * (q − 1)

    #Let d a relatively prime number to φ(phi)
    e * d = 1 % phi(x)

    #Let (e, x) public key of DUAL RSA.
    while(i<n):
        Mi = m[n//2+1:n]
        Ri =(Bi) e % x
        Li =ASCII (Bi)
        Ci =(Ri) XOR (Li)
        Di = MD5 (Ci)
        i+=1
    
    Q =ci +Ci #cipher text
    H =di + Di #hashed value
    
    return (Q,H)