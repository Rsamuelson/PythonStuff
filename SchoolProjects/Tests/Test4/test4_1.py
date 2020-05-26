import sqlite3

# Headers: ['id', 'first_name','last_name','address']
rows = [
    [1,'James','Butt','5 Littleton Ave, Bemidji, MN 56601'],
    [2,'Josephine','Darakjy','7397 Silver Spear St, Long Beach, NY 11561'],
    [3,'Art','Venere','725 Somerset Ave, Fremont, OH 43420'],
    [4,'Lenna','Paprocki','220 Carpenter Dr, Vista, CA 92083'],
    [5,'Donette','Foller','603 Depot Ave, Stuart, FL 34997'],
    [6,'Simona','Morasca','907 Salmon Dr, The Villages, FL 32162'],
    [7,'Mitsue','Tollner','443 N. Nicolls Ave, Liverpool, NY 13090'],
    [8,'Leota','Dilliard','8837 Hilltop St, Syosset, NT 11791'],
    [9,'Sage','Wieser','318 Forest St, Oswego, NT 13126'],
    [10,'Kris','Marrier','625 Lees Creek St, Beckley, WV 25801'],
    [11,'Minna','Amigon','144 Bayberry St, Acworth, GA 30101']
]

sqlite_filename = input("Enter name of the SQLite file: ")
conn = sqlite3.connect(sqlite_filename)
c = conn.cursor()
# Run the CREATE TABLE statement for the columns named in the header.
create_table_stmt = "CREATE TABLE IF NOT EXISTS customer (ID 'INTEGER' PRIMARY KEY AUTOINCREMENT, first_name 'TEXT', last_name 'TEXT', address 'TEXT')"
c.execute(create_table_stmt)
conn.commit()

for row in rows:
    insert_command = 'INSERT INTO {tn} VALUES ("{ID}","{fn}", "{ln}","{address}")'.format(tn='"customer"', ID=row[0], fn=row[1], ln=row[2], address=row[3])
    c.execute(insert_command)

conn.commit()

c.execute('SELECT * FROM customer ORDER BY last_name, first_name')
for row in c:
    print(row)

conn.close()