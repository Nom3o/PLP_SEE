"""
Week 2 assignment
"""
#1.Create an empty list called my_list.
my_list = []

#2.Append the following elements to my_list: 10, 20, 30, 40.
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

#3.Insert the value 15 at the second position in the list.
my_list.insert(1,15)

#4.Extend my_list with another list: [50, 60, 70].
my_list.append(50)
my_list.append(60)
my_list.append(70)

#5.Remove the last element from my_list.
my_list.pop()

#6.Sort my_list in ascending order
my_list.sort()

#7.Find and print the index of the value 30 in my_list.
index_of_30 = my_list.index(30)
print('The index of 30 is: ',index_of_30)

 
                        #By Abel Mekuriya