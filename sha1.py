import hashlib

x = raw_input("Enter the strings:")
hash = hashlib.sha1(x).hexdigest()
print hash
