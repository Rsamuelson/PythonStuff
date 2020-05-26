import sqlite3

sqlite_file = 'corny.sqlite'
table_name = 'prod'   # name of the table to be queried

conn = sqlite3.connect(sqlite_file)

story_co_corn_prod = \
    [
        {'year': 2007, 'bushels': 33822000},
        {'year': 2008, 'bushels': 27000000},
        {'year': 2009, 'bushels': 29782000},
        {'year': 2010, 'bushels': 26790000},
        {'year': 2011, 'bushels': 28220000},
        {'year': 2012, 'bushels': 27086000},
        {'year': 2013, 'bushels': 21689000},
        {'year': 2014, 'bushels': 26923000},
        {'year': 2015, 'bushels': 30286000},
        {'year': 2016, 'bushels': 36402000},
        {'year': 2017, 'bushels': 33264000},
        {'year': 2018, 'bushels': 30457000}
    ]

cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS {tn} (year INTEGER PRIMARY KEY, "
            "bushels INTEGER NOT NULL)".format(tn=table_name))
# Remove any rows that might already be in the table
cur.execute("DELETE FROM {tn}".format(tn=table_name))
# Insert the rows
for row in story_co_corn_prod:
    cur.execute('INSERT INTO {tn} (year, bushels) VALUES ({year}, {bushels})'.format(tn=table_name, year=row['year'], bushels=row['bushels']))
cur.execute('commit')

cur.execute('Select Max(bushels), Min(bushels), Avg(bushels) from {tn}'.format(tn=table_name))
row = cur.fetchone()

print('Average Bushels: ', row[2])
print('Minimum Bushels: ', row[1])
print('Maximum Bushels: ', row[0])



conn.commit()
conn.close()




# Add the missing code to query and print the MIN(), AVG(), and MAX() bushels
# from the prod table.
...