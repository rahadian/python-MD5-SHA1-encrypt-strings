import hashlib

x = raw_input("Enter the string :")
hash = hashlib.md5(x).hexdigest()
print hash
