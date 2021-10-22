# 문제 : 입력받은 2가지 정수 사이에 존재하는 3의 배수 중에서 홀수의 합을 리턴하는 함수 구현

# 어떤수가 홀수인지 아닌지 체크하는 함수
def is_odd(num) :
    if num%2==1:
        return True
    else:
        return False


# # 어떤수가 3의 배수인지 아닌지 체크하는 함수
def is_three_multiple(num) :
    if num%3==0:
        return True
    else:
        return False


# is_odd와 is_three_multiple 이용해서 완성해주세요.
def get_sum(n, m) :
    total=0
    for a in range(n,m+1):
        if is_odd(a):
            if is_three_multiple(a):
                total+=a
    return total
                


result = get_sum(50, 100)
print("결과 : {}".format(result));
# 출력 => 675
