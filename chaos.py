# File: chaos.py
# Created 2/12/15 by Kevin Grimsley
# A simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic function")
    n = eval(input(“How many numbers should I print? ”))
    x = eval(input("Enter a number between 0 and 1: "))
    for i in range(n) :
        x = 2.0 * x * (1 - x)
        print(x)
main()

