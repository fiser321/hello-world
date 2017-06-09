from rediscluster import StrictRedisCluster
startup_nodes = [{"host": "10.10.20.231", "port": "6379"}]
rc = StrictRedisCluster(startup_nodes=startup_nodes, decode_responses=True)
print(rc.get("ff"))