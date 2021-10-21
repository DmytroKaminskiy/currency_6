import sqlite3

connection = sqlite3.connect('./chinook.db')
connection.row_factory = sqlite3.Row
cur = connection.cursor()

sql = '''
select LastName, CustomerId, FirstName from customers;
'''
cur.execute(sql)
results = cur.fetchall()
connection.close()

###################################################
# print(results)

# def get_full_name(obj):
#     return f'{user["FirstName"]} {user["LastName"]}'

# for user in results:
#     print(dict(user))
    # print(f'{user["CustomerId"]} {get_full_name(user)}')

class User:
    def __init__(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, key, value)

    def save(self):
        import sqlite3

        connection = sqlite3.connect('./chinook.db')
        connection.row_factory = sqlite3.Row
        cur = connection.cursor()

        sql = f'''
        UPDATE customers
        SET FirstName = "{self.FirstName}",
            LastName = "{self.LastName}"
        WHERE
            CustomerId = {self.CustomerId} 
        '''
        cur.execute(sql)
        connection.commit()
        connection.close()

users = [
    User(**data) for data in results
]
breakpoint()
