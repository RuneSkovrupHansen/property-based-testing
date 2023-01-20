#!/bin/python3

def bubble_sort(array: list):
    n = len(array)
    swapped = False
    for i in range(n-1):
        for j in range(n-i-2):
            if array[j] > array[j+1]:
                swapped = True
                array[j], array[j+1] = array[j+1], array[j]
        if not swapped:
            return

def main():
    array = [1,5,7,4,7]
    print(f"{array = }")
    bubble_sort(array)
    print(f"{array = }")

if __name__ == "__main__":
    main()