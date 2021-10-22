
# num이 홀수인지 짝수인지 판별해주는 함수 완성
def is_even(num) :
    return num%2==0

def print_even(num) :

  if is_even(num) :
    print("짝수입니다.")
  else :
    print("홀수입니다.")



print_even(2) # 짝수입니다.
print_even(3) # 홀수입니다.
