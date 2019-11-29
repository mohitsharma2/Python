'''
n=int(input('please enter the number of rows'))
for i in range(1,n+1):
    for j in range(1,n+1):
        print('*',end=' ')
    print()

please enter the number of rows4
* * * * 
* * * * 
* * * * 
* * * * 
    
please enter the number of rows5
* * * * * 
* * * * * 
* * * * * 
* * * * * 
* * * * *
         '''



'''
n=int(input('please enter the number of rows'))
for i in range(1,n+1):
    print(i) 
            
please enter the number of rows5
1
2
3
4
5
 '''



'''
n=int(input('please enter the number of rows'))
for i in range(1,n+1):
    print(i,end=' ')
    
please enter the number of rows5
1 2 3 4 5
         '''



'''
n=int(input('please enter the number of rows'))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(i,end=' ')
    print()

please enter the number of rows5
1 1 1 1 1 
2 2 2 2 2 
3 3 3 3 3 
4 4 4 4 4 
5 5 5 5 5
         '''



'''
n=int(input('please enter the number of rows'))
for i in range(1,n+1):
    for j in range(1,n+1):
        print(j,end=' ')
    print()

please enter the number of rows5
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5 
1 2 3 4 5
         '''



'''
n=int(input('please enter the number of rows'))
for i in range(n):
    for j in range(n):
        print(chr(65+i),end=' ')
    print()

please enter the number of rows5
A A A A A 
B B B B B 
C C C C C 
D D D D D 
E E E E E 
         '''




'''
n=int(input('please enter the number of rows'))
for i in range(n):
    for j in range(n):
        print(chr(65+j),end=' ')
    print()

please enter the number of rows5
A B C D E 
A B C D E 
A B C D E 
A B C D E 
A B C D E
         '''



'''
n=int(input('please enter the number of rows'))
for i in range(n):
    for j in range(n):
        print(n-i,end=' ')
    print()

please enter the number of rows5
5 5 5 5 5 
4 4 4 4 4 
3 3 3 3 3 
2 2 2 2 2 
1 1 1 1 1
         '''



'''
n=int(input('please enter the number of rows'))
for i in range(n):
    for j in range(n):
        print(n-j,end=' ')
    print()

please enter the number of rows5
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1 
5 4 3 2 1
         '''


'''
n=int(input('please enter the number of rows'))
for i in range(n+1):
    for j in range(n+1):
        print(chr(65+(n-i)),end=' ')
    print()

please enter the number of rows 4
E E E E E 
D D D D D 
C C C C C 
B B B B B 
A A A A A
         '''




'''
n=int(input('please enter the number of rows'))
for i in range(n+1):
    for j in range(n+1):
        print(chr(65+(n-j)),end=' ')
    print()

please enter the number of rows 4
E D C B A 
E D C B A 
E D C B A 
E D C B A 
E D C B A 
         '''



'''
n=int(input('please enter the number of rows'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end='')
    print()

please enter the number of rows 5
*
**
***
****
*****
     '''



'''
n=int(input('please enter the number of rows'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print('*',end=' ')
    print()

please enter the number of rows 5
* 
* * 
* * * 
* * * * 
* * * * *
         '''




'''
n=int(input('please enter the number of rows'))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(i,end='')
    print()

please enter the number of rows5
1
22
333
4444
55555
     '''



'''

    
please enter the number of rows 5
1
12
123
1234
12345
     '''


'''


please enter the number of rows4
A
BB
CCC
DDDD
EEEEE
     '''



'''
n=int(input('please enter the number of rows'))
for i in range(n+1):
    for j in range(i+1):
        print(chr(65+j),end='')
    print()

    
please enter the number of rows4
A
AB
ABC
ABCD
ABCDE
     '''




'''


please enter the number of rows5
*****
****
***
**
*
 '''




'''


please enter the number of rows5
11111
2222
333
44
5
 '''




'''
n=int(input('please enter the number of rows'))
for i in range(n+1):
    for j in range(1,6-i):
        print(j,end='')
    print()

please enter the number of rows5
12345
1234
123
12
1
 '''




'''
n=int(input('please enter the number of rows'))
for i in range(n+1):
    for j in range(1,6-i):
        print(chr(65+i),end='')
    print()

           
please enter the number of rows5
AAAAA
BBBB
CCC
DD
E
 '''




'''
n=int(input('please enter the number of rows'))
for i in range(n):
    for j in range(n-i):
        print(chr(65+i),end='')
    print()

        
please enter the number of rows5
AAAAA
BBBB
CCC
DD
E
 '''



'''
n=int(input('please enter the number of rows'))
for i in range(n+1):
    for j in range(5-i):
        print(chr(65+j),end='')
    print()
             
please enter the number of rows5
ABCDE
ABCD
ABC
AB
A
 '''



'''
n=int(input('please enter the number of rows'))
for i in range(n):
    for j in range(5-i):
        print(5-i,end='')
    print()

please enter the number of rows5
55555
4444
333
22
1
 '''




'''
n=int(input('please enter the number of rows'))
for i in range(n):
    for j in range(n-i):
        print(n-i,end='')
    print()


please enter the number of rows5
55555
4444
333
22
1
 '''




'''
n=int(input('please enter the number of rows'))
for i in range(n+1):
    for j in range(1,(n+1)-i):
        print(j,end='')
    print()

please enter the number of rows5
12345
1234
123
12
1
 '''



'''
n=int(input('please enter the number of rows'))
for i in range(n+1):
    for j in range(n-i):
        print(chr(69-i),end=' ')
    print()


n=int(input('please enter the number of rows'))
for i in range(n):
    for j in range(n-i):
        print(chr(69-i),end=' ')
    print()

    

please enter the number of rows5
E E E E E 
D D D D 
C C C 
B B 
A
 '''


