# from hashlib import sha3_256
import hashlib
def hashing(data:str):
    h = hashlib.sha3_256(data.encode())
    return h.hexdigest()

def checking_hash(data:str, hash:str):
    h = hashlib.sha3_256(data.encode())
    return h.hexdigest()==hash

if __name__=='__main__':
    print(checking_hash('hello1',hashing("hello")))
    print(checking_hash('hello',hashing("hello")))
