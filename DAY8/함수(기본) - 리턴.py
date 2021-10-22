def func1():
    num=10
    return num

# 10을 리턴해주는 함수 완성


a = func1();
print(a);

#출력 : 10

b = func1();
print(b);

#출력 : 10

def func2(num2):
    return num2
    
# 매개변수 값을 그대로 리턴해주는 함수 완성

c = func2(22);
print(c);
# 출력 : 22
  
d=func2(55);
print(d);
# 출력 : 55


def func3(num3):
    num3=num3**2
    return num3
# 매개변수 값을 제곱해서 리턴해주는 함수 완성

e = func3(10);
print(e);
# 출력 : 100

f = func3(5);
print(f);
# 출력 : 25


def func4(num4,num5):
    num4=num4+num5
    return num4
    
# 매개변수를 더해서 리턴해주는 함수 완성

g = func4(10, 30);
print(g);
# 출력 : 40

h = func4(20, 50);
print(h);
# 출력 : 70
