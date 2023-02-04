print('hello, python!')

num1 = int(input('Plz input num1:'))
num2 = int(input('Plz input num2:'))
def subtract(n1,n2):
    if num1 >= num2:
        for i in range(num1):
            if num2+i == num1:
                print(i)
                break
    else :
        for i in range(num2):
            if num1+i==num2:
                print("-"+str(i))
                break
subtract(num1,num2)
