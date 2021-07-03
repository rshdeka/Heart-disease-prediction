#Python code to generate MD5 of string data
import hashlib

string = input("Enter any string:")
encode=string.encode()
#passing the encoded string to MD5 hash function
m=hashlib.md5(encode) 

print(m.hexdigest())