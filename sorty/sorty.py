#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Athul Vijayan
# @Date:   2015-08-30 00:07:36
# @Last Modified by:   athul
# @Last Modified time: 2015-10-12 18:43:25
import random

def greater(a, b):
    '''For numeric comparison, use it to sort ascending; returns a > b'''
    return a > b

def lesser(a, b):
    ''' For numeric comparison, use it to sort descending; returns a < b '''
    return a < b

def stringLen(a, b):
    ''' 
    For text comparison, use it to sort ascending in number of characters; return len(a) > len(b)
    '''
    return len(a) > len(b)

def _merge(L, R, compareFn):
    res = []
    while L or R:
        if L and R:
            if compareFn(R[0], L[0]):
                res.append(L[0])
                L = L[1:]
            else:
                res.append(R[0])
                R = R[1:]
        elif L:
            res.append(L[0])
            L = L[1:]
        elif R:
            res.append(R[0])
            R = R[1:]
    return res

def insertionSort(inArray, compareFn=greater):
    '''
    This function sorts the given array and returns the sorted array.
    Sorting is done by comparing elements in array using compareFn. The method of comparison can be changed too.
   'insertionSort' ---> O(n^2) complexity

    Usage:
    sortedArray = insertionSort(inArray, compareFn);

    Arguments
    inArray -----------------> Unsorted array
    compareFn (Opt) ---------> Function handle used for comparing elements (Default is numeric ascending)

    Output
    sortedArray -------------> Sorted output
    '''
    for i in range(1, len(inArray)):
        key = inArray[i]
        j = i-1;
        while(j >= 0 and compareFn(inArray[j], key)):
            inArray[j+1] = inArray[j]
            j = j-1
        inArray[j+1] = key
    return inArray

def selectionSort(inArray, compareFn=greater):
    '''
    This function sorts the given array and returns the sorted array.
    Sorting is done by comparing elements in array using compareFn. The method of comparison can be changed too.
   'selectionSort' ---> O(n^2) complexity

    Usage:
    sortedArray = selectionSort(inArray, compareFn);

    Arguments
    inArray -----------------> Unsorted array
    compareFn (Opt) ---------> Function handle used for comparing elements (Default is numeric ascending)
    
    Output
    sortedArray -------------> Sorted output
    '''
    for i in range(len(inArray)):
        minLoc = i;
        for j in range(i+1, len(inArray)):
            if compareFn(inArray[minLoc], inArray[j]):
                minLoc = j
        minElem = inArray[minLoc]
        inArray[minLoc] = inArray[i]
        inArray[i] = minElem 
    return inArray

def mergeSort(inArray, compareFn=greater):
    '''
    This function sorts the given array and returns the sorted array.
    Sorting is done by comparing elements in array using compareFn. The method of comparison can be changed too.
   'mergeSort'     ---> O(nlogn) complexity

    Usage:
    sortedArray = mergeSort(inArray, compareFn);

    Arguments
    inArray -----------------> Unsorted array
    compareFn (Opt) ---------> Function handle used for comparing elements (Default is numeric ascending)
    
    Output
    sortedArray -------------> Sorted output
    '''
    if len(inArray) <= 1:
        return inArray
    r = int(len(inArray)/2);
    # Divide
    L = inArray[0:r]
    R = inArray[r:len(inArray)]
    L = mergeSort(L, compareFn=compareFn)
    R = mergeSort(R, compareFn=compareFn)
    # and conquer
    return _merge(L, R, compareFn)

class heap:
    """implementation of heap data structure for an arbitrary compare function as the heap property"""

    def parent(self, i):
        '''Gets the value of the parent node'''
        try:
            return self.data[(i-1)/2]
        except IndexError:
            return None
        

    def left(self, i):
        '''Gets the value of the left child node'''
        try:
            return self.data[2*i+1]
        except IndexError:
            return None
        

    def right(self, i):
        '''Gets the value of the right child node'''
        try:
            return self.data[2*(i+1)]
        except IndexError:
            return None

    def heapify(self, i):
        '''Given a list and a pivot point, this function recursively rearranges such that pivot becomes the root of a valid sub heap'''
        l = 2*i + 1
        r = 2*(i + 1)
        if (l < self.heapSize) and self.compareFn(self.left(i), self.data[i]):
            largest = l
        else:
            largest = i
        if (r < self.heapSize) and self.compareFn(self.right(i), self.data[largest]):
            largest = r
        if largest != i:
            _temp = self.data[i]
            self.data[i] = self.data[largest]
            self.data[largest] = _temp
            self.heapify(largest)

    def checkHeapSanity(self):
        '''Checks if the heap obeys heap property. Checks for validity'''
        for i in xrange(1, len(self.data)):
            if self.compareFn(self.parent(i), self.data[i]) == False:
                return False
        return True

    def buildHeap(self):
        '''Builds a heap from an arbitrary array'''
        for i in reversed(xrange(int((len(self.data)-2)/2)+1)):
            self.heapify(i)

    def __init__(self, inArray, compareFn=greater):
        '''Builds a heap from an arbitrary array as soon as you make the data structure'''
        self.compareFn=compareFn
        self.data = inArray
        self.heapSize = len(self.data)
        self.buildHeap()

def heapSort(inArray, compareFn=greater):
    '''
    This function sorts the given array and returns the sorted array.
    Sorting is done by comparing elements in array using compareFn. The method of comparison can be changed too.
   'heapSort'     ---> O(nlogn) complexity

    Usage:
    sortedArray = heapSort(inArray, compareFn);

    Arguments
    inArray -----------------> Unsorted array
    compareFn (Opt) ---------> Function handle used for comparing elements (Default is numeric ascending)
    
    Output
    sortedArray -------------> Sorted output
    '''
    hp = heap(inArray, compareFn)
    for i in xrange(len(inArray)-1, 0, -1):
        _temp = hp.data[0]
        hp.data[0] = hp.data[i]
        hp.data[i] = _temp
        hp.heapSize = hp.heapSize -1
        hp.heapify(0)
    return hp.data

def _quickSort(inArray, p, r, compareFn=lesser):
    '''This function does the actual work in quickSort. main one is a wrapper'''
    if p < r-1:
        # Randomization
        k = random.randint(p, r-1)
        _temp = inArray[r-1]
        inArray[r-1] = inArray[k]
        inArray[k] = _temp
        
        x = inArray[r-1]
        j = p
        for i in xrange(r-p-1):
            i += p
            if compareFn(inArray[i], x):
                _temp = inArray[j]
                inArray[j] = inArray[i]
                inArray[i] = _temp
                j +=1
        inArray[r-1] = inArray[j]
        inArray[j] = x
        _quickSort(inArray, p, j, compareFn=compareFn)
        _quickSort(inArray, j + 1, r, compareFn=compareFn)
    return inArray

def quickSort(inArray, compareFn=lesser):
    '''
    This function sorts the given array and returns the sorted array.
    Sorting is done by comparing elements in array using compareFn. The method of comparison can be changed too.
   'heapSort'     ---> average running time O(nlogn) complexity

    Usage:
    sortedArray = quickSort(inArray, compareFn);

    Arguments
    inArray -----------------> Unsorted array
    compareFn (Opt) ---------> Function handle used for comparing elements (Default is numeric ascending)
    
    Output
    sortedArray -------------> Sorted output
    '''
    return _quickSort(inArray, 0, len(inArray), compareFn=compareFn)
        
        
if __name__=="__main__":
    print("use as this as a module.")

