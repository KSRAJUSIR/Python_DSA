def hash_fun(key):
    hash=0
    for i in key:
        hash+=ord(i)
    return hash%5
value=hash_fun('karthik')
value1=hash_fun('pavan')
print(value)
print(value1)