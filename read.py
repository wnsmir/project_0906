import mysql.connector

class PhoneBook:
    def __init__(self, db_config):
        # 데이터베이스 연결 초기화
        self.db_config = db_config
        self.connection = mysql.connector.connect(**db_config)
        self.cursor = self.connection.cursor(dictionary=True)
    
    def read(self):
        # 연락처 정보를 가져오는 SQL 쿼리
        query = "SELECT id, name, phone_number, email FROM contacts"
        
        # 쿼리 실행
        self.cursor.execute(query)
        
        # 모든 행을 가져옴
        contacts = self.cursor.fetchall()
        
        if not contacts:
            print("전화번호부가 비어있습니다.")
        else:
            for contact in contacts:
                print(f"ID: {contact['id']}, 이름: {contact['name']}, 전화번호: {contact['phone_number']}, 이메일: {contact['email']}")
