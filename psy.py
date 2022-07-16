import psycopg2
con=psycopg2.connect(host='localhost',dbname='psydb',user='postgres',password='postgres',port=5433)

con.execute('create schema common')
con.commit()

con.close()