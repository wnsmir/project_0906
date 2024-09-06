import mysql.connector

def delete_customer(id):
    conn = mysql.connector.connect(
        host='192.168.0.92',
        user='test',
        password='88Einstein$',
        database='pub'
    )
    cursor = conn.cursor()

    sql = "DELETE FROM customers WHERE id = %s"
    values = (id,)

    try:
        cursor.execute(sql, values)
        conn.commit()
        if cursor.rowcount > 0:
            print(f"ID {id}의 연락처가 삭제되었습니다.")
        else:
            print(f"ID {id}에 해당하는 연락처가 존재하지 않습니다.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()

