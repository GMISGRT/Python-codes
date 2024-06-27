from simplejson import simplejson
x='{"name":"GM","age":20,"city:bbsr"}'

y=simplejson.loads(x)

print(y["age"])
print(y["name"])

q={
    "name":"Dio",
    "age":40,
    "city":"london",
}

y=simplejson.dump(q)
print(y)