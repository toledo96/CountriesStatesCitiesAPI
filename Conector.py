
import pymysql

def create_connection():
    print("entre")
    db = pymysql.connect("localhost", "root", "", "upch")
    return  db

if __name__ == '__main__':
    cursor = create_connection().cursor()
    cursor.execute("SELECT id,name from countries")
    data = cursor.fetchall()
    print(data)
