def bubble_sort(alist):
    for i in range(len(alist) - 1, 0, -1):
        no_swap = True
        for j in range(0,i):
            if alist[j + 1] < alist[j]:
                alist[j], alist[j+1] = alist[j+1], alist[j]
                no_swap = False
        if no_swap:
            return

alist = input("enter the list of number: ").split()
alist = [int(x) for x in alist]
bubble_sort(alist)
print('sorted list: ', end='')
print(alist)
