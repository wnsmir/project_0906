import mysql.connector

def update_customer(id, name=None, phone_number=None, email=None):
    conn = mysql.connector.connect(
        host='192.168.0.92',
        user='test',
        password='88Einstein$',
        database='pub'
    )
    cursor = conn.cursor()

    # 업데이트할 필드 설정
    updates = []
    values = []
    
    if name:
        updates.append("name = %s")
        values.append(name)
    if phone_number:
        updates.append("phone_number = %s")
        values.append(phone_number)
    if email:
        updates.append("email = %s")
        values.append(email)
        
    if not updates:
        print("업데이트할 내용이 없습니다.")
        return

    # SQL 쿼리 구성
    update_str = ", ".join(updates)
    sql = f"UPDATE customers SET {update_str} WHERE id = %s"
    values.append(id)

    try:
        cursor.execute(sql, values)
        conn.commit()
        print(f"ID {id}의 연락처가 업데이트되었습니다.")
    except mysql.connector.Error as e:
        print(f"Error: {e}")
    finally:
        cursor.close()
        conn.close()
