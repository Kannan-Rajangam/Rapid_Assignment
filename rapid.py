#----------------------------------------------- PROGRAM ----> 1 ----------------------------------------------

N = 17
list =[]
for i in range(1,N+1):
    if(i%5==0) and (i%3==0):
        list.append('FizzBuzz')
    elif(i%5==0):
        list.append('Buzz')
    elif(i%3==0):
        list.append('Fizz')
    else:
        list.append(i)     
print (str(list)[1:-1].replace('\'','').replace(' ',''))

# 1,2,Fizz,4,Buzz,Fizz,7,8,Fizz,Buzz,11,Fizz,13,14,FizzBuzz,16,17


#----------------------------------------------- PROGRAM ----> 2 ----------------------------------------------


repeat_list = [1, 2, 3, 5, 8, 4, 7, 9, 1, 4, 12, 5, 6, 5, 2, 1, 0, 8, 1]
unique_list = set(repeat_list)
for i in unique_list:
    temp = 0
    for j in repeat_list:
        if i == j:
            temp+=1
    if temp>1:
        print(str(i)+' - '+str(temp))

#	1 - 4
#	2 - 2
#	4 - 2
#	5 - 3
#	8 - 2

#----------------------------------------------- PROGRAM ----> 3 ----------------------------------------------# PROGRAM ----> 3

dictionary = {"Rick": 85, "Amit": 42, "George": 53, "Tanya": 60, "Linda": 35}
sum = 0
for i,j in dictionary.items():
    sum +=j
print(sum)

#	275

#----------------------------------------------- PROGRAM ----> 4 ----------------------------------------------
 

batsman1,batsman2 = 0, 0
score = [1,2,0,0,4,1,6,2,1,3]
batsman11, batsman21 = [], []
batsman,batsman1,batsman2,total = 1,0,0,0
for i in range(1, len(score) + 1):
    if i % 7 == 0:
        if batsman % 2 == 0:
            batsman = 1
        else:
            batsman = 2
    if batsman == 2:
        batsman21.append(score[i - 1])
        batsman2 += score[i - 1]
        if (score[i-1]%2!=0):
            batsman = 1
    else:
        batsman11.append(score[i - 1])
        batsman1 = int(batsman1) + int(score[i - 1])
        if (int(score[i-1])%2!=0):
            batsman=2
    total+=score[i - 1]
print('Total Score: '+str(total))
print('Batsman 1 Score : '+str(batsman1)+' ('+str(batsman11)[1:-1].replace(',',' +')+')' )
print('Batsman 2 Score : '+str(batsman2)+' ('+str(batsman21)[1:-1].replace(',',' +')+')' )

#	Total Score: 20
#	Batsman 1 Score : 4 (1 + 3)
#	Batsman 2 Score : 16 (2 + 0 + 0 + 4 + 1 + 6 + 2 + 1)
