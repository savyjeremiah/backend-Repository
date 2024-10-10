                            #                 # DATA STRUCTURE
                            #    they are four types of data structure



my_list =['temi','saviour','sekinat' ,'gozie','temi',1,2,3,4,5,6,7,8,9,0,True,False,]
                     # anyway to create list
my_list2 =list(range(5))

print(my_list)
print(my_list2)
                # how to accees a data
temi_name =my_list[1]

print(f'helle {temi_name[-6] }   and i am {my_list[5]}')
print (my_list[-6])
print(my_list [2:5])
my_list[6] ='joy'
print(my_list)
my_list.append(2)
print(my_list)
my_list.insert(5,"joel")
print(my_list)
my_list.pop(3)
print(my_list)
my_list.remove(4)
print(my_list)
my_list.append('saviour')
print(my_list)
my_list.count('saviour')
print(my_list
      )


num = ['apple','mango','organ','lemon','goa']
print(num[2])
num.append('dog')
print(num)
num.insert(3,'saviour')
print(num)
num.pop(2)
print(num)


                      # TURPLE 
         # this is the collection of item
my_turple =() # empty turple
single_turple =("saviour",) #  a single turple
name =('html','css','js','py''apple','mango',['organ','lemon','goat'],1,2,3,4,5,6,7,8,True,False)
name1 =('[1,3,5,7,9]')
print(name[3:7])
print(name)
print(name [2:5])


shool =('1,2,3,4,5,6,7,8')
food = ('apple','mango','organ','lemon','goat')
print(shool)
print(food)
school =list(food)
print(school)
food =list(school)
print(food)
school =tuple(food)
print(school*8)