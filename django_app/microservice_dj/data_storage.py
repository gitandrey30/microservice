import sqlite3


#
# create_db = sqlite3.connect('db.sqlite3')
# cursor = create_db.cursor()
# cursor.execute('''CREATE TABLE storage(data DATE, currenc TEXT );''')
# create_db.commit()
# create_db.close()



#
# cursor.execute('''SELECT * FROM storage;''')
# # for data in cursor:
# #     print(data)


connect_to_db = sqlite3.connect('db.sqlite3')
cursor = connect_to_db.cursor()
# cursor.execute('''UPDATE storage SET data="2020-10-12" WHERE currenc IS '2,8288 BYN';''')
# connect_to_db.commit()
# connect_to_db.close()


cursor.execute('''SELECT * FROM storage''')
data = cursor.fetchall()
for item in data:
    print(item)
connect_to_db.commit()
connect_to_db.close()
