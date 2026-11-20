# Week 1.3, Session 1: Task 1b

fruit = ['apple','pear','banana','orange']

# loop through the list
while fruit:
	print(fruit.pop())


# Why does this work?

#The while loop works because Python treats a non-empty list as True and an empty list as False. Each time the loop runs, pop() removes and returns the last item in the list, which is then printed. Once all items have been removed, the list becomes empty, evaluates to False, and the while loop stops.

# What features of Python does it rely on?

#It relies on Boolean evaluation, while loops, and the pop() list method.
