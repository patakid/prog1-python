import math
# EX1
# a = int(input('Give a number: '))
# while a !=0:
#     if a % 2 == 0:
#         print('{} is even'.format(a))
#     else:
#         print('{} is odd'.format(a))
#     a=int(input('Give a number: '))

#EX2
# def GCD(n1,n2):
#     if n2>n1:
#         n1,n2=n2,n1
#     div=1
#     for n in range(1,n1+1): #range(0,5) 0,1,2,3,4
#         if n1%n==0 and n2%n==0:
#             div=n
#     return div
#
# str=input("Give two number and separate with coma: ")
# a,b=str.split(',')
# print(a,b)
# print(GCD(int(a),int(b)))

#EX3
# def dist(x1,x2,y1,y2):
#     return math.sqrt((x1-x2)**2 + (y1-y2)**2)
# s1=input('Give the (x,y) coordinate of the first point: ')
# s2=input('Give the (x,y) coordinate of the second point: ')
#
# x1,y1=s1.split(' ')
# x2,y2=s2.split(' ')
#
# print(dist(int(x1),int(x2),int(x1),int(y2)))
#EX6
def GCD(n1,n2):
    if n2>n1:
        n1,n2=n2,n1
    div=1
    for n in range(1,n1+1): #range(0,5) 0,1,2,3,4
        if n1%n==0 and n2%n==0:
            div=n
    return div


