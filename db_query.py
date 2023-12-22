import sqlite3

conn = sqlite3.connect('bd.db')
cursor = conn.cursor()

def query(data):
    lst = []
    cursor.execute("""SELECT * FROM stations""")
    res1 = cursor.fetchall()
    for i in res1:
        lst.append(i[-2])
    minn = min(lst)

    cursor.execute(
        """SELECT * FROM stations
            WHERE year=? and month=? and day=?;""",
        data
    )
    # res = cursor.fetchone()
    # res = cursor.fetchmany()
    res = cursor.fetchall()
    print(*res, sep="\n")
    print(len(res))