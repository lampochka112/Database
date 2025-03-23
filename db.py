import sqlite3


connection = sqlite3.connect('zoo.db')
cursor = connection.cursor()

#cursor.execute('''
####)
#''')




#cursor.execute('INSERT INTO animals (name, species, age) VALUES ("Лев", "хищник", 5)')#
#cursor.execute('INSERT INTO animals (name, species, age) VALUES ("Черепаха", "млекопитающие", 10)')#
#cursor.execute('INSERT INTO animals (name, species, age) VALUES ("Попугай", "птица", 2)')#

cursor.execute("SELECT * FROM animals")
rows = cursor.fetchall()

for row in rows:
    print(row)



# connection.commit()#
connection.close()