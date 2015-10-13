#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Author: Athul Vijayan
# @Date:   2015-08-30 02:00:35
# @Last Modified by:   Athul Vijayan
# @Last Modified time: 2015-08-30 03:29:56
''' Implements divide and conquer aproach for finding a subarray of an array which has highest sum'''

def crossingArray(inArray):
    '''
    Finds the sub array which contains the middle element of the array and has highest sum. 
    '''
    mid = len(inArray)//2
    leftSum = float('-inf')
    s = 0
    for i in xrange(0, mid):
        s += inArray[mid-i]
        if s > leftSum:
            leftSum = s
            leftIndex = i
    rightSum = float('-inf')
    s = 0
    for i in xrange(mid,len(inArray)):
        s += inArray[i]
        if s > rightSum:
            rightSum = s
            rightIndex = i
    return [leftIndex, rightIndex, leftSum+rightSum]

def maxSubArray(inArray):
    if len(inArray)==1:
        # Base case
        return [0, 0, inArray[0]]
    else:
        mid = len(inArray)//2
        # find Highest sum in left sub problem
        [leftLowIndex, leftHighIndex, leftSum] = maxSubArray(inArray[0:mid])
        # find Highest sum in right sub problem
        [rightLowIndex, rightHighIndex, rightSum] = maxSubArray(inArray[mid:])
        # find Highest sum in sub arrays that contain midpoint as an element
        [crossLowIndex, crossHighIndex, crossSum] = crossingArray(inArray)

        # Choose the maximum of the three cases 
        if ((leftSum >= rightSum) and (leftSum >= crossSum)):
            return [leftLowIndex, leftHighIndex, leftSum]
        elif ((rightSum >= leftSum) and (rightSum >= crossSum)):
            return [rightLowIndex, rightHighIndex, rightSum]
        else:
            return [crossLowIndex, crossHighIndex, crossSum]



