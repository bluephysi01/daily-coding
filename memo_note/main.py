# main.py
from memo_manager import save_memo, read_memos, search_memo

def run():
    print("\n--- 📝 파이썬 메모장 ---")
    print("1. 쓰기 / 2. 읽기 / 3. 검색 / 4. 종료")
    choice = input("원하는 메뉴를 선택하세요: ")
    
    if choice == "1":
        content = input("기록할 내용: ")
        save_memo(content)
        
    elif choice == "2":
        memos = read_memos()
        if not memos:
            print("📭 저장된 메모가 없습니다.")
        else:
            print("\n--- 전체 메모 목록 ---")
            for memo in memos:
                print(memo.strip())
                
    elif choice == "3":
        keyword = input("검색할 단어를 입력하세요: ")
        results = search_memo(keyword)
        if not results:
            print(f"🔍 '{keyword}'(이)가 포함된 메모가 없습니다.")
        else:
            print(f"\n--- '{keyword}' 검색 결과 ({len(results)}건) ---")
            for result in results:
                print(result.strip())
                
    elif choice == "4":
        print("프로그램을 종료합니다. 👋")
        return
    
    else:
        print("❌ 잘못된 선택입니다.")

if __name__ == "__main__":
    # 처음 한 번만 실행되는 게 아니라 반복해서 메뉴가 나오게 하려면 
    # while True: 구문을 사용할 수 있습니다.
    while True:
        run()
        if input("\n계속하시겠습니까? (y/n): ").lower() != 'y':
            break