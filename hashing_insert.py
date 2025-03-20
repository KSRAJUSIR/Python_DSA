hash_table=[[]]*10
def hash_fun(key):
    hash=0
    for i in key:
        hash+=ord(i)
    return hash%10
def insert_data(key,data):
    h=hash_fun(key)
    hash_table[h]=data
def get_data(key):
    h=hash_fun(key)
    return hash_table[h]
insert_data('523','suresh')
insert_data('123','naresh')
insert_data('679','mahesh')
result=get_data('523')
result1=get_data('679')
print(result)
print(result1)