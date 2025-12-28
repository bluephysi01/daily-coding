# main.py
from memo_manager import save_memo, read_memos

def run():
    print("--- 📝 파이썬 메모장 ---")
    choice = input("1. 메모 쓰기 / 2. 메모 읽기: ")
    
    if choice == "1":
        content = input("내용: ")
        save_memo(content)
    elif choice == "2":
        memos = read_memos()
        if not memos:
            print("📭 저장된 메모가 없습니다.")
        else:
            print("\n--- 저장된 메모 목록 ---")
            # for 문을 사용하여 리스트의 각 항목을 출력합니다.
            for memo in memos:
                # .strip()은 문자열 끝의 줄바꿈(\n)을 제거해줍니다.
                print(memo.strip())

if __name__ == "__main__":
    run()