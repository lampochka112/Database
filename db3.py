import sqlite3


connection = sqlite3.connect('zoo db')
cursor = connection.cursor

cursor.execute('ALTER TABLE animals ADD COLUMN room INTIGER')

cursor.execute('INSERT INTO animals')