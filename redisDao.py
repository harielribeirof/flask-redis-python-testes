import redis

class RedisDao():

    def __init__(self) -> None:
        self.client = redis.Redis(host='localhost', port=6379)
        pass       
    

    def inserirKey(self, usuario: dict) -> None:
        self.client.hset(usuario['chave'], 'chave', usuario['chave'])
        self.client.hset(usuario['chave'], 'email', usuario['email'])
        self.client.hset(usuario['chave'], 'role', usuario['role'])
    
    def consultarKey(self, chave: str) -> dict:
        chave = self.client.hgetall(chave)
        return eval(str(chave).replace("b'", "'"))
    
    def deletarKey(self, chave: str):
        self.client.delete(chave)

    def listarTodasKeys(self) -> list:
        return {'lista': self.client.keys()}


    # # set a key
    # # client.hmset('f111', {'time': 'flamengo', 'nome': 'hariel'})

    # # client.hset('f222', 'time', 'vasco')
    # # client.hset('f222', 'nome', 'junior')


    # client.delete('f222')
    # # get a value
    # # value = client.get('test-key')
    # value = client.hgetall('f111')

    # print(value)
    # print(client.keys())
    # print(client.hexists('f222', 'time'))
