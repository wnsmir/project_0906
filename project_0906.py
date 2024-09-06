class phoneBook:
    def __init__(self):  
        self.contacts = {}  # 전화번호부를 저장할 딕셔너리 생성, 키는 ID, 값은 연락처 정보(이름, 전화번호, 이메일)로 관리

    def create(self, id, name, phone_number, email): # 연락처 추가
        self.contacts[id] = {'이름': name, '전화번호': phone_number, '이메일': email}
        print(f"ID {id}의 연락처가 추가되었습니다.")