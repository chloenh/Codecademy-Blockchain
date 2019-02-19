
from hashlib import sha256

# text to hash
text = 'My current company offers me internships in Shanghai and Warsaw'


# print result
hash_result = sha256(text.encode())
print(hash_result.hexdigest())

#prints 16187538efed08c1a2f00df1e9560341a748a8aeeb46cb84d55c130908ecdd97

