import redis


def main():
    client = redis.Redis(host='192.168.1.102', port='6379')
    client.set('say', 'hello')
    client.hset('loginUser', 'username', 'johnyehyo')
    client.hset('loginUser', 'password', '123')
    print(client.exists('say'))
    print(client.hexists('loginUser', 'username'))
    print(client.get('say'))
    print(client.hget('loginUser', 'username'))
    print(client.hgetall('loginUser'))
    client.lpush('list1', 'a')
    client.lpush('list1', 'b')
    client.lpush('list1', 'c')
    print(client.lrange('list1', 0, -1))


if __name__ == '__main__':
    main()
