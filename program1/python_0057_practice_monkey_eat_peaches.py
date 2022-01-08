'''
Requirement:
There is a group of monkeys who eat a pile of peaches.
On Day 1, they eat half plus 1
On Day 2, they eat half plus 1 again
...
On Day 10, they notice there is only 1 peach left before they eat.

Question:
1) How many peaches in total in Day 1?
2) Print out from Day 1, how many peaches in total? How many peaches they eat? How many peaches are left. Till last day.
'''



































'''

Code Logic is always the most important! When code logic is clear, then we can quickly convert the logic to code.

-----------------
analysis
-----------------

1) To calculate the 1st day, we have to calculate the 9th day, 8th day, ...till 1st day.
   -> I should use for loop, loop in range(9,0,-1)
   
2) On each day, there are 3 numbers
   a) How many peaches in total at first?      -> define a new variable peach_total
   b) How many peaches the monkey eat today?   -> define a new variable peach_eaten
   c) How many peaches are left?               -> define a new variable peach_left
   
   -> peach_total = peach_eaten + peach_left  

------------
IMPORTANCE!
------------
1st step, figure out the variables required in your program!

3) On 10th day, before the monkey eat, they notice there is only 1 peach left

 ->  
 Day 9:
 peach_left = 1
 peach_total = (peach_left + 1) * 2
 
 Day 8:
 peach_left (day 8) = peach_total (day 9)
 peach_total = (peach_left + 1) * 2
 
 Day 7:
 peach_left (day 7) = peach_total (day 8)
 peach_total = (peach_left + 1) * 2

 ... ...
 

'''

peach_total = 1
print(f'On day 10, there are {peach_total} peaches before they eat.')

for day in range(9,0,-1):
    peach_left = peach_total                # We are looping backwards. Day 10's peach_total is Day 9's peach_left
    peach_total = (peach_left + 1) * 2      # Calculate Day 9's peach_total from Day 9's peach_left
    # print(f"On day {day}, there are {peach_total} peaches before they eat.")

print(f"On day 1, there are {peach_total} peaches before they eat.") # Question 1 is done.

print('--------------------------------------')

# Question 2) 

for day in range(1, 10):
    peach_eaten = (peach_total // 2) + 1
    peach_left = peach_total - peach_eaten
    print(f"On day {day}, there are {peach_total} initially. They each {peach_eaten} peaches, and there are {peach_left} peaches left.")
    peach_total = peach_left
    
print(f"On day 10, there are {peach_total} left.")