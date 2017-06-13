from neo4j.v1 import GraphDatabase,basic_auth

driver = GraphDatabase.driver('bolt://192.168.50.70:7687', auth=basic_auth("neo4j", "test1"))
session = driver.session()
session.run("CREATE (a:Person {name: {name}, title: {title}})",
            {"name": "Arthur", "title": "King"})
result = session.run("MATCH (a:Person) WHERE a.name = {name} "
                       "RETURN a.name AS name, a.title AS title",
                       {"name": "Arthur"})

for record in result:
    print("%s %s" % (record["title"], record["name"]))
session.close()