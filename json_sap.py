import json

obj ={'item':'apple','price':120}
json_text = json.dumps(obj)

print(json_text)
print(type(json_text))

text='{"id":123,"is_student":true}'
obj=json.loads(text)
print(obj)
print(type(obj))
print(obj['id'])