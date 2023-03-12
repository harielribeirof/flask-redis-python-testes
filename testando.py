import requests as rq
import redis

response = rq.get("https://google.com")

print(response)


client = redis.Redis(host='localhost', port=6379)

# set a key
# client.hmset('f111', {'time': 'flamengo', 'nome': 'hariel'})

# client.hset('f222', 'time', 'vasco')
# client.hset('f222', 'nome', 'junior')


client.delete('f222')
# get a value
# value = client.get('test-key')
value = client.hgetall('f111')

print(value)
print(client.keys())
print(client.hexists('f222', 'time'))
