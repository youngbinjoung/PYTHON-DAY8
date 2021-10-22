# 다국어인사에 매개변수로 1을 넘기면 안녕하세요. 2를 넘기면 하이!, 3을 넘기면 봉쥬르
# 다국어인사에 매개변수로 인사의 횟수와 언어를 넘겨서 해당 횟수만큼 해당 언어로 인사하게 해주세요.

def 다국어인사2(lang) :
    if lang==1:
        print("안녕하세요")
    elif lang==2:
        print("하이")
    elif lang==3:
        print("봉쥬르")

다국어인사2(3) # 봉쥬르 출력
다국어인사2(1) # 안녕하세요 출력
다국어인사2(2) # 하이 출력

def 다국어인사(lang, count) :
    if lang==1:
        for a in range(1,count+1):
            print("안녕하세요")
    elif lang==2:
        for b in range(1,count+1):
            print("하이")
    elif lang==3:
        for c in range(1,count+1):
            print("봉쥬르")


다국어인사(3, 3) # 봉쥬르 3번 출력
다국어인사(1, 5) # 안녕하세요 5번 출력
다국어인사(2, 1) # 하이 1번 출력
