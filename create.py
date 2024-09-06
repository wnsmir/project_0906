import mysql.connector

# PhoneBook 클래스 정의
class phoneBook:
    def __init__(self):
        # 전화번호부를 저장할 딕셔너리 생성, 키는 ID, 값은 연락처 정보(이름, 전화번호, 이메일)로 관리
        self.contacts = {}

    def create(self, id, name, phone_number, email):
        # 연락처 추가
        self.contacts[id] = {'이름': name, '전화번호': phone_number, '이메일': email}
        print(f"ID {id}의 연락처가 추가되었습니다.")

# MySQL에 연결
db_connection = mysql.connector.connect(
    host="localhost",  # MySQL이 설치된 서버 주소 (로컬일 경우 localhost)
    user="test",       # MySQL 사용자 이름
    password="password",  # MySQL 사용자 비밀번호
    database="pub"     # 사용할 데이터베이스 이름
)

# 커서 생성
cursor = db_connection.cursor()

# SQL 쿼리 실행 (예시: authors 테이블에서 데이터 조회)
cursor.execute("SELECT id, first_name, last_name, photo FROM authors")

# 결과 가져오기
rows = cursor.fetchall()

# phoneBook 클래스의 인스턴스 생성
my_phone_book = phoneBook()

# MySQL 데이터에서 연락처 생성
for row in rows:
    id = row[0]  # authors 테이블의 ID
    name = f"{row[1]} {row[2]}"  # first_name과 last_name 결합
    phone_number = "010-1234-5678"  # 가상의 전화번호, 실제로는 데이터베이스에 있지 않음
    email = f"{row[1].lower()}.{row[2].lower()}@example.com"  # 가상의 이메일 생성, 실제로는 데이터베이스에 있지 않음

    # phoneBook의 create 메서드로 연락처 추가
    my_phone_book.create(id, name, phone_number, email)

# 커서 및 연결 종료
cursor.close()
db_connection.close()
