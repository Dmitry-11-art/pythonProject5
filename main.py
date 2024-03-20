# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def fib(n):
   if n <= 2:
       return 1
   return fib(n-1)+fib(n-2)
print(fib(10))