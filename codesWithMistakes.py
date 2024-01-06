#Prepared Slawomir Meczynski
#bubble_sort with a mistake
def bubble_sort(arr):
    swapped = False
    for i in range(len(arr)-1):
        for j in range(len(arr)-i):
            if arr[j] < arr[j-1]:
                swapped = True
                arr[j-1], arr[j] = arr[j], arr[j-1]
        if not(swapped):
            return
        
#selection_sort with a mistake
def selection_sort(arr):
    for ind in range(len(arr)-1):
        min = ind
        for y in range(ind+1, len(arr)):
            if arr[y] < arr[min]:
                arr[min] = arr[y]
        arr[ind], arr[min] = arr[min], arr[ind]

#merge_sort with a mistake
def merge(arr, l, m, r):
    n1 = m-l+1
    n2 = r-m

    left = [0]*n1
    right = [0]*n2

    for x in range(n1):
        left[x] = arr[l+x]

    for x in range(n2):
        right[x] = arr[m+x]

    i, j = 0, 0
    k = l
    while i < n1 and j < n2:
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i <n1:
        arr[k] = left[i]
        i += 1
        k +=1
    
    while j <n2:
        arr[k] = right[j]
        j += 1
        k += 1

def merge_sort(arr, l, r):
    if l < r:
        mid = (l+r)//2
        merge_sort(arr, l, mid)
        merge_sort(arr, mid+1, r)
        merge(arr, l, mid, r)


#quick_sort with a mistake
def partition(arr, l, h):
    pivot = arr[l]
    k = l +1
    for ind in range(l, h):
        if arr[ind] < pivot:
            k += 1
            arr[ind], arr[k] = arr[k], arr[ind]
    arr[k-1], arr[l] = arr[l], arr[k-1]
    return k-1

def quick_sort(arr, l, h):
    if l < h:
        pivot_loc = partition(arr, l, h)
        quick_sort(arr, l, pivot_loc-1)
        quick_sort(arr, pivot_loc+1, h)

#binary_search with a mistake
def binary_search(arr, x):
    low = 0
    mid = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            high = mid-1
        else:
            low = mid+1
    else:
       return "Not found"

array = [1,2,3,4,5,6,7,8,9]
x = binary_search(array, 1)
print(x)

#minHeap with mistakes
class MinHeap:
    def __init__(self):
        self.current_size = 0
        self.heap_list = [0]

    def up(self, i):
        stop = False
        while stop == False and i//2*1 > 0:
            if self.heap_list[i] > self.heap_list[i//2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            else:
                stop = True
            i //= 2
    
    def insert(self, x):
        self.heap_list.append(x)
        self.current_size -= 1
        self.up(self.current_size)

    def down(self, i):
        while i*2 < self.current_size:
            min_child = self.min_child(i)
            if self.heap_list[min_child] <self.heap_list[i]:
                self.heap_list[i], self.heap_list[min_child] = self.heap_list[min_child], self.heap_list[i]
            i = min_child
    
    def min_child(self, i):
        if i*2+1 > self.current_size:
            return i*2
        else:
            if self.heap_list[i*2] > self.heap_list[i*2+1]:
                return i*2+1
            else:
                return i*2
            
    def delete(self):
        if len(self.heap_list) == 1:
            return 'Empty heap'
        root = self.heap_list[self.current_size]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.heap_list.pop()
        self.current_size -= 1
        self.down(1)
        return root



'''
------------CORRECT CODES---------------

'''
#bubble_sort correct
def bubble_sort(arr):
    swapped = False
    for i in range(len(arr)-1):
        for j in range(1, len(arr) -i): #here must be from 1 because we check if arr[j] < arr[j-1] 
            if arr[j] < arr[j-1]:
                swapped = True
                arr[j-1], arr[j] = arr[j], arr[j-1]
        if not(swapped):
            return

#selection_sort correct
def selection_sort(arr):
    for ind in range(len(arr)-1):
        min = ind
        for y in range(ind+1, len(arr)):
            if arr[y] < arr[min]:
                arr[min] = arr[y]         # here we want to overwrite the indexes, not the actual values
        arr[ind], arr[min] = arr[min], arr[ind]

#merge_sort correct
def merge(arr, l, m, r):
    n1 = m-l+1
    n2 = r-m

    left = [0]*n1
    right = [0]*n2

    for x in range(n1):
        left[x] = arr[l+x]

    for x in range(n2):
        right[x] = arr[m+x+1] # it must be +1 

    i, j = 0, 0
    k = l
    while i < n1 and j < n2:
        if left[i] < right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    while i <n1:
        arr[k] = left[i]
        i += 1
        k +=1
    
    while j <n2:
        arr[k] = right[j]
        j += 1
        k += 1

def merge_sort(arr, l, r):
    if l < r:
        mid = (l+r)//2
        merge_sort(arr, l, mid)
        merge_sort(arr, mid+1, r)
        merge(arr, l, mid, r)


#quick_sort correct
def partition(arr, l, h):
    pivot = arr[l]
    k = l +1
    for ind in range(l, h):
        if arr[ind] < pivot:
            arr[ind], arr[k] = arr[k], arr[ind] # those lines must be switched because then it would switch with
            k += 1                              # the value from index above without considering if it is bigger or smaller
    arr[k-1], arr[l] = arr[l], arr[k-1]
    return k-1

def quick_sort(arr, l, h):
    if l < h:
        pivot_loc = partition(arr, l, h)
        quick_sort(arr, l, pivot_loc-1)
        quick_sort(arr, pivot_loc+1, h)


#binary_search correct - there were actually no mistakes:)
def binary_search(arr, x):
    low = 0
    mid = 0
    high = len(arr)-1
    while low <= high:
        mid = (low+high)//2
        if arr[mid] == x:
            return mid
        elif arr[mid] > x:
            high = mid-1
        else:
            low = mid+1
    else:
       return "Not found"
    


#minHeap correct
class MinHeap:
    def __init__(self):
        self.current_size = 0
        self.heap_list = [0]

    def up(self, i):
        stop = False
        while stop == False and i//2 > 0:   #the parent is i//2, not i//2+1
            if self.heap_list[i] > self.heap_list[i//2]:
                self.heap_list[i], self.heap_list[i // 2] = self.heap_list[i // 2], self.heap_list[i]
            else:
                stop = True
            i //= 2
    
    def insert(self, x):
        self.heap_list.append(x)
        self.current_size += 1  #we insert, not delete
        self.up(self.current_size)

    def down(self, i):
        while i*2 <= self.current_size: #it's ok when i*2 = the size
            min_child = self.min_child(i)
            if self.heap_list[min_child] <self.heap_list[i]:
                self.heap_list[i], self.heap_list[min_child] = self.heap_list[min_child], self.heap_list[i]
            i = min_child
    
    def min_child(self, i):
        if i*2+1 > self.current_size:
            return i*2
        else:
            if self.heap_list[i*2] > self.heap_list[i*2+1]:
                return i*2+1
            else:
                return i*2
            
    def delete(self):
        if len(self.heap_list) == 1:
            return 'Empty heap'
        root = self.heap_list[1]    #the root is the first element, not the last one
        self.heap_list[1] = self.heap_list[self.current_size]
        self.heap_list.pop()
        self.current_size -= 1
        self.down(1)
        return root
