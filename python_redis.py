import redis
print("Ola eu sou Docker pytohn ")
r = redis.Redis(host='redis-compose', port=6379, db=0)
print ((r.get('valores').decode('utf-8')))