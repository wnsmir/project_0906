def main():
    manager = UserManager()

    while True:
        print("\n--- 사용자 관리 프로그램 ---")
        print("1. 사용자 추가")
        print("2. 사용자 조회")
        print("3. 사용자 수정")
        print("4. 사용자 삭제")
        print("5. 종료")
        
        choice = input("원하는 작업을 선택하세요 (1-6): ")

        if choice == '1':
            # 사용자 추가
            name = input("이름: ")
            email = input("이메일: ")
            phone = input("전화번호: ")
            manager.create_user(name, email, phone)

        elif choice == '2':
            # 사용자 조회
            user_id = int(input("조회할 사용자 ID를 입력하세요: "))
            manager.read_user(user_id)

        elif choice == '3':
            # 사용자 수정
            user_id = int(input("수정할 사용자 ID를 입력하세요: "))
            name = input("새 이름 (변경하지 않으려면 빈칸으로 두세요): ")
            email = input("새 이메일 (변경하지 않으려면 빈칸으로 두세요): ")
            phone = input("새 전화번호 (변경하지 않으려면 빈칸으로 두세요): ")
            
            # 빈 입력 처리
            name = name if name else None
            email = email if email else None
            phone = phone if phone else None
            
            manager.update_user(user_id, name, email, phone)

        elif choice == '4':
            # 사용자 삭제
            user_id = int(input("삭제할 사용자 ID를 입력하세요: "))
            manager.delete_user(user_id)

        elif choice == '5':
            # 프로그램 종료
            print("프로그램을 종료합니다.")
            break

        else:
            print("잘못된 입력입니다. 다시 시도하세요.")

# 프로그램 실행
if __name__ == "__main__":
    main()