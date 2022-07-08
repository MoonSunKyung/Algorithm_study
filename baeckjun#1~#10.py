#1
import random
import numpy as np

N = input("input N")
X = input("input X")

if int(X) > 10000 or int(N) < 1:
    print("you should type x over 10,000 and N over 1")
else:
    N = int(N)
    A = np.random.randint(N,size=N)

A = str(A)
print(A)
small_nums = []
for small_num in A:
    if small_num < X:
        small_nums.append(small_num)

print(small_nums) #중간에 들어가는 빈칸은 무엇인가..흠

2
import numpy as np

given_nums = np.zeros(10)
for k in range(0,10):
    i = input("input int")
    if 0<int(i)<1000:
        given_nums[k] = i
    else:
        print("plz enter int over 0 below 1000 ")

remainders = []
for num in given_nums:
    remainders.append(num%42)

diff_nums = 10

for index in range(0,len(remainders)):
    for plus in range(1,len(remainders)):
        if index + plus > 9:
            break
        elif remainders[index] == remainders[index+plus]:
            diff_nums -= 1

print(diff_nums)

#3 _ 연속 숫자배열을 어떻게 N개로 구분하게하는지 모르겠어..;_;
import numpy as np

N = input("enter length of numbers")
ind_list = range(0,int(N))
number_list = np.zeros(int(N))

for ind in ind_list:
    number_list[ind] = input("enter numbers")

print(sum(number_list))

4
N = input("enter your number 0~99")
first_N = N

if int(N) <10:
    N = N.zfill(1)
    first_N = N.zfill(1)

cycle_num = 0

while True:        # 무한루프 도는 것 같은데 이유는 아직 못찾음
    N_plus = N[0] + N[-1]
    N = N[-1] + N_plus[-1]
    cycle_num += 1
    if N == first_N:
        break

print(cycle_num)

#5
room_number = int(input())
# 주어진 N까지 6의 등차수열을 최소 몇번 더해야 하는가
#1 -> 7 -> 19 -> 37 -> 61

#6
feb_n = int(input("enter number below 20"))

feb = [0,1]
for i in range(2,feb_n+1):
    feb.append(feb[i-1]+feb[i-2])

print(feb[feb_n])

#7
word_num = int(input("enter num of word"))

num = 0
for i in range(word_num):
    word = input("enter word")
#    if word    -> 여기서 각 글자가 분리되지 않았다는 것을 보여야함. how?

#8 _ 감 못잡아서 구글링
N = int(input())
d = 2
while d <= N:
    if N % d == 0:
        print(d)
        N = N / d
    else:
        d += 1



