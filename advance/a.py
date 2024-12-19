import pyodbc as p

try:
    con=p.connect(
        user='root',
        password='tiger',
        host='localhost'
    )
    cur=con.cursor()

    cur.execute("show databases")
    for db in cur:
        print(db)

except Exception as e:
    print(e)



