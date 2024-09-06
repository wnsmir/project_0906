def read(self): # 전화번호부 출력
        if not self.contacts:
            print("전화번호부가 비어있습니다.") # 전화번호부에 조회할 전화번호가 없을때
        else:
            for id, info in self.contacts.items():
                print(f"ID: {id}, 이름: {info['이름']}, 전화번호: {info['전화번호']}, 이메일: {info['이메일']}")
