
from hashlib import sha256

# text to hash
text = 'My current company offers me internships in Shanghai and Warsaw'


# print result
hash_result = sha256(text.encode())
print(hash_result.hexdigest())

