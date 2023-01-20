#!/bin/python3

def add(a: int, b: int):
    if a > 100 and a < 500:
        return 100
    return a+b

def main():
    print(add(10, 20))
    print(add(-100, 50))

if __name__ == "__main__":
    main()