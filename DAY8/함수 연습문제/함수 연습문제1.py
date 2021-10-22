# # 구구단 7단을 출력해주는 함수를 만들어주세요.
def gugu7():
    for a in range(1,10):
        print("7 x {} = {}".format(a,7*a))
gugu7() # 출력 : 7단



# # 원하는 이름을 출력해주는 함수를 만들어주세요(매개변수)
def print_name(name):
    print(name)
    
print_name("홍길동") # 출력 : 홍길동




# # 구구단 원하는 단을 출력해주는 함수를 만들어주세요.(매개변수)
def my_gugu(gugu):
    for a in range(1,10):
        print("{} x {} = {}".format(gugu,a,gugu*a))
    
my_gugu(8)
# 출력 : 8단

my_gugu(5)
# 출력 : 5단



# # 구구단을 1단부터 원하는 단까지 출력해주는 함수를 만들어주세요.(매개변수)
def one_to_n_gugu(want):
    for a in range(1,want+1):
        for b in range(1,10):
            print("{} x {} = {}".format(a,b,a*b))
    
one_to_n_gugu(11) # 출력 1 ~ 11단까지 출력
one_to_n_gugu(20) # 출력 1 ~ 20단까지 출력

# True를 리턴하는 함수를 만들어주세요. 그리고 my_bool 변수에 저장해주세요. 그리고 my_bool을 출력해주세요.(리턴)
def get_true():
    return True
myBool = get_true()
print(myBool) # 출력 : True



# 자신의 이름을 리턴하는 함수를 만들고 변수 my_name에 저장해주세요. 그리고 my_name을 출력해주세요.(리턴)
def get_my_name():
    return "자신의 이름"
my_name = get_my_name()
print(my_name) # 출력 : 자신의 이름



# 원하는 수를 제곱해서 리턴해주는 함수를 만들어주세요, 그리고 num1 변수에 저장해주세요. num1을 출력해주세요.(매개변수, 리턴)
def square(num):
    num=num**2
    return num

num1 = square(4)
print(num1) # 출력 : 16

num2 = square(10)
print(num2) # 출력 : 100



# 원하는 수를 제곱한 후 2로 나눈 값을 리턴해주는 함수를 만들어주세요. 단, 제곱은 이미 만들어진 함수를 이용해야만 합니다. 제곱해주는 코드를 중복해서 사용하지 말아주세요. 변수에 저장해주세요. 그리고 변수를 출력해주세요.(매개변수, 리턴)
def my_calc(num2):
    return square(num2)/2

num3 = my_calc(10)
print(num3) # 출력 : 50

num4 = my_calc(20)
print(num4) # 출력 : 200



# 1부터 임의의 수까지 사이에 있는 짝수들의 합을 리턴하는 함수를 만들어주세요. 마찬가지로 짝수 판벼 코드를 중복해서 작성하지 말고 이미 만들어진 짝수판별 함수를 이용해주세요. 그리고 변수에 저장해주세요. 변수를 출력해주세요.(매개변수, 리턴)


# step 1. 1 ~ 10까지 출력
# step 2. 1 ~ 10까지의 합 출력
# step 3. 1 ~ 10까지의 짝수의 합 출력

def is_even(n) :
  if n % 2 == 0 :
    return True
  return False

def get_sum_of_even(a):
    total=0
    for b in range(1,a+1):
        total+=b
    return total


    
    


num5 = get_sum_of_even(10)

print(num5) # 출력 :30 

num6 = get_sum_of_even(100)

print(num6) # 출력 :2550


