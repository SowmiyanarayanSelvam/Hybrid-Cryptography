def HybridDecryption(Q,H,s,L,d,D,k):
    # Q: Cipher text
    # H: Hashing value of cipher text
    # s: 128 bit size of block
    # L: key length
    # K: encrypted key using ECC

n=C/s
i=0

while(i<n/2):
    ci = Q[0:n//2]
    Ci = Q[n//2+1:n]
    di1 = MD5(ci)
    Di1 = MD5(Ci)

    if (di == di1) and (Di == Di1):
        for j in range(L):
            ki =ECCdec (TCPK, Kj−1)
        mi = DAES(Kj, ci)
    i+=1

i=n//2
Give (d, p, q) #private key used for decryption
dp =d % (p − 1)
dq =d % (q − 1)

while(i<n):
    Rpi = Ridp %  p
    Rqi = Ridq %  q
    S0 = (Rqi − Cpi) * p−1 %  q
    Si v= Rpi +S0 * P
    Wi = ASCII (Ci)
    Mi = XNOR (Si,Wi)
    i+=1

P= mi + Mi #decrypted message