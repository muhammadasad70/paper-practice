# sum=0
# num=0
# while num<5:
#     num+=1
#     if num%3==0:
#         continue
#     sum+=num
# # print(sum)
# for i in range(5,0,-1):
#     for k in range(1,6-i):
#         print(" ",end="")
#     for j in range(1,i+1):
#         print(j,end="")
#     print("\n",end="")
i=5
while i>=1:
    num=1
    for j in range(1,i+1):
        print(num,end="***")
        num*=2
    print()
    i=i-1