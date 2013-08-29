import random
import time

def swap(lyst, i, j):
        temp = lyst[i]
        lyst[i] = lyst[j]
        lyst[j] = temp

def bubbleSort(lyst):
        start = time.time()
        n = len(lyst)
        while n > 1:
                i = 1
                while i < n:
                        if lyst[i]<lyst[i-1]:
                                swap(lyst, i, i-1)
                        i += 1
                n-=1
        end = round((time.time() - start),3)
        print "A list of size", list,"took", end,"seconds for Bubble to execute"
        return lyst
    
def insertionSort(lyst):
    start = time.time()
    i = 1
    while i < len(lyst):
        itemToInsert = lyst[i]
        j = i - 1
        while j >= 0:
            if itemToInsert < lyst[j]:
                lyst[j + 1] = lyst[j]
                j-= 1
            else:
                break
        lyst[j+1] = itemToInsert
        i += 1
    end = round((time.time() - start),3)
    print "A list of size", list,"took", end,"seconds for Insertion to execute"
    return lyst

def selectionSort(lyst):
    start = time.time()
    i = 0
    while i < len(lyst) - 1:
        minIndex = i
        j = i + 1
        while j < len(lyst):
            if lyst [j] < lyst[minIndex]:
                minIndex = j
            j += 1
        if minIndex != i:
            swap (lyst, minIndex, i)
        i += 1
    end = round((time.time() - start),3)
    print "A list of size", list,"took", end,"seconds for Selection to execute"
    return lyst

print "This program allows bubblesort, selection sort, and insertion sort"
print "algorithms race so that a user can see the effectiveness of the methods"
print "used"

lyst = []
qty = input("Please give us the number of integers you want in the list: ")
x = input("starting range: ")
y = input("ending range: ")
for i in xrange(qty):
        poly = random.randint(x, y)
        lyst.append(poly)
list = len(lyst)
print bubbleSort(lyst)
print insertionSort(lyst)
print selectionSort(lyst)
