# memo_manager.py
import datetime

def save_memo(content):
    # 현재 날짜와 시간을 가져옵니다.
    now = datetime.datetime.now()
    timestamp = now.strftime("%Y-%m-%d %H:%M:%S")
    
    # memo.txt 파일에 내용을 추가(append) 모드로 저장합니다.
    with open("memo.txt", "a", encoding="utf-8") as file:
        file.write(f"[{timestamp}] {content}\n")
    
    print("✅ 메모가 성공적으로 저장되었습니다!")

def read_memos():
    try:
        with open("memo.txt", "r", encoding="utf-8") as file:
            return file.readlines() # 파일의 모든 줄을 리스트로 반환합니다.
    except FileNotFoundError:
        return [] # 파일이 없으면 빈 리스트를 반환합니다.
    
def search_memo(keyword):
    memos = read_memos()
    # keyword가 포함된 메모만 리스트로 만듭니다.
    results = [memo for memo in memos if keyword in memo]
    return results