import json

data = {
'name' : 'ACME',
'shares' : 100,
'price' : 542.23
}

json_str = json.dumps(data)
data = json.loads(json_str)

print json_str
print data
