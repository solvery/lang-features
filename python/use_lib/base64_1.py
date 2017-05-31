import base64
s = 'hello'
s_b64 = base64.b64encode(bytes(s))
s_b64d = base64.b64decode(s_b64)

print s_b64
print s_b64d
