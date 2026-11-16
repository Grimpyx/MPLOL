import random as r

# Encrypted names
names_encrypted = ["Mzxxfr","Otsfymfs","Qzpfx","Txhfw","Kfgnfs","Ji{ns","Ijssnx","Snpnyf","Otxjk","Qzhfx","Fsyts","[nwffo","Kjqn}","Ofptg","Rnqyts","Rf}","Lzxyf{","Jrjqnj","Tqn{nf"]

# Encrypt/decrypt methods
def encrypt_and_output_as_list(words):
    list = ["".join([chr(ord(c)+5) for c in word]) for word in words]
    print(f"[\"{"\",\"".join(list)}\"]")
def decrypt(words):
    return ["".join([chr(ord(c)-5) for c in word]) for word in words]

# Decrypt names
L = decrypt(names_encrypted)

# Deep copy
queue = [x for x in L]

# Pick random from queue until empty
r.shuffle(queue)
index = 0
while len(queue) > 0:
    index += 1
    name = queue.pop()
    
    print(f"Namn kvar: {len(queue)}")
    print(f"{index}: {name}")

    if len(queue) > 0:
        input("Klicka på enter för nästa...")