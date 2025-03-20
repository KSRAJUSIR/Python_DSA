hash_table=[[] for _ in range(10)]

def hashing(keyvalue):
    return keyvalue%len(hash_table)

def insert(hash_table,keyvalue,value):
    hash_key=hashing(keyvalue)
    hash_table[hash_key].append(value)

def display(keyvalue):
    h=hashing(keyvalue)
    return hash_table[h]

insert(hash_table,10,'allahabad')
insert(hash_table,21,'punjab')
insert(hash_table,21,"noida")
insert(hash_table,20,"hyderabad")
res=display(21)
rs=display(10)
print(res)
print(rs)