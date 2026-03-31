def bubble_sort(arr):
    n = len(arr)
    total = 0
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                total += 1
    print(f"Terjadi {total}x Swap")
    return arr

def swap_bubble_sort(mylist):
    n = len(mylist)
    for i in range(n-1):
        swapped = False
        for j in range(n-i-1):
            if mylist[j] > mylist[j+1]:
                mylist[j], mylist[j+1] = mylist[j+1], mylist[j]
                swapped = True
        if not swapped:
            break
    return mylist

def reverse_selection_sort(arr):
    n = len(arr)
    total = 0
    for i in range(n-1):
        min_index = i

        for j in range(i+1, n):
            if arr[j] > arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr

def selection_sort(arr):
    n = len(arr)
    total = 0
    for i in range(n-1):
        min_index = i
        swapped = False
        for j in range(i+1, n):
            if arr[j] < arr[min_index]:
                min_index = j
                swapped = True
        arr[i], arr[min_index] = arr[min_index], arr[i]
        if swapped:
            total += 1
    print(f"Terjadi {total}x Swap")
    return arr

data1 = [305, 340, 816, 478, 390, 777, 265, 298, 131, 783, 339, 567, 521, 431, 605, 678, 817, 716, 490, 915, 829, 315, 555, 205, 691, 254, 502, 226, 796, 300, 831, 706, 338, 829, 54, 89, 448, 517, 750, 373, 608, 32, 465, 241, 719, 866, 786, 597, 351, 289, 9, 148, 862, 229, 340, 71, 434, 475, 722, 270, 226, 165, 152, 303, 58, 607, 338, 127, 881, 810, 661, 575, 65, 436, 526, 811, 765, 979, 235, 240, 442, 930, 909, 263, 61, 51, 318, 364, 723, 208, 159, 353, 857, 724, 798, 770, 79, 380, 197, 299, 853, 431, 150, 919, 201, 489, 926, 504, 400, 504, 933, 296, 517, 899, 903, 672, 340, 819, 867, 425, 414, 642, 507, 172, 350, 853, 593, 912, 53, 132, 437, 955, 697, 660, 881, 692, 904, 414, 900, 920, 261, 154, 104, 625, 790, 562, 641, 336, 217, 720]
data2 = data1.copy()
data3 = data2.copy()
data4 = data1.copy()


# Soal 1
print(swap_bubble_sort(data4))

# Soal 2
print(reverse_selection_sort(data1))

#Soal 3 dan 4
print(bubble_sort(data2))
print(selection_sort(data3))




