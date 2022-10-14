"""
3. Provide a program to calculate the time and distance based on
below problem.
• We have a 100-meter rod.
• At both ends, 1-1 cockroach is place.
• The left cockroach moves at 1 meter per second forward, and every 10 seconds moves 2
meters backward.
• The right cockroach moves at 2 meters per second forward, and every 5 seconds moves 1
meter backward.
• When both cockroaches meet, we have to calculate the time and distance. Calculate the total
time to complete the 100 meter rod
"""
"""
Have two values start at 0 for each cockroach, have an infinite loop where each iteration represents a second.
Every second add 1 to cockroach 1 if the time is divisible by 10 then also subtract 2. Every second add 2 to cockroach 2
if the time is divisible by 5 also subtract 1. Then check at every second if the values are equal, if they’re equal then
print the distance, the number of iterations and then break

break the problem down into what information you have and what information must you provide as output, then identify
information you must create/manipulate, then provide a logical set of steps to achieve the objective.

Do it in steps. Take 1 cockroach at first. If you can calculate the time for 1 then repeat the process for the other.
Hint: If you use a class, you prevent having a lot of duplicated code.

My code says it takes 38 seconds and they meet at meter 32.
"""
