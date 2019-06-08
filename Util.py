# from math import *
class Util():
    @staticmethod

    def is_anagram(str1,str2):
        str1 = str1.replace(' ','').lower()
        str2 = str2.replace(' ','').lower()

        if sorted(str1) == sorted(str2):
            print('it is an anagram')
            return True
        else:
            return False
            # print('not an anagram')
        # _ANS = __is_anagram__.__func__()

    #-----------------------------------------------------------------------------------------------------------   
    @staticmethod

    def Is_prime_number(num):
        for i in range(2,num):
            if num %i == 0:
                print('it is not a prime number')
                return False
                break
            else:
                print('it is prime')
                return True
    #---------------------------------------------------------------------------------------------------------------            
    @staticmethod

    def Is_palindrome(str1):
        rev = str1[::-1]
        if rev == str1 :
            print('it is Palindrome')
            return True
        else:
            print('not a palindrome')
            return False
        #Is_palindrome('bob')
    # --------------------------------------------------------------------------------------------------------------
    @staticmethod

    def binary_search(l,r,val, arr):
        if l <= r:
            middle = (l+r)//2
            if arr[middle] == val:
                print('sss')
                return True
            elif arr[middle] < val:
                l = middle + 1
            else:
                r = middle - 1
        return False  
        #binary_search(1,4,3,[1,2,3,4,5,6])

    @staticmethod

    def to_decimal(number):

        while len(str(number)) < 8:
            number = number + str(0)
        s3 = number[4:8]
        s4 = number[0:4]
        swap = s3 + s4
        b = str(swap)
        return int(b)
        # to_decimal(4)

    #------------------------------------------------------------------------------------------------------------
    @staticmethod


    def sortArrList(arr):
        for i in range (len(arr)-1):
            for j in range(i+1,len(arr)):
                if arr[i] > arr[j]:
                    arr[i],arr[j] = arr[j],arr[i]

        return arr
        # sortArrList([9,3,5,2,1])
    #-------------------------------------------------------------------------------------------------------------

    # def sort_string(str1):
    #     ln = len(str1)
    #     for i in range(ln-1):
    #         for j in range(i+1,ln):
    #             if str1[i] > str1[j]:
    #                 str1[i],str1[j] = str1[j],str1[i]
    #         print(str1)
    #     return str1
    # sort_string('dba')

    #---------------------------------------------------------------------------------------------------------
    @staticmethod

    def bubble_sort(arr):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i] > arr[j]:
                    arr[i], arr[j] = arr[j] ,arr[i] 
        print(arr)            
        return arr
        # bubble_sort([7,1,8,2,3])

    #--------------------------------------------------------------------------------------------------------------
    @staticmethod

    def insertionSort(arr):
        for i in range(1,len(arr)):
            key = arr[i]
            j = i-1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j -= 1
            arr[j+1] = key
            print(arr)
        return arr
        # _ANS = __insertionSort__.__func__()

    @staticmethod

    def get_prime():
        count = 1
        number =2
        prime_arr = []
        while count <= 1000:
            res = Is_prime_number(number)
            if res :
                prime_arr.append(number)
            count += 1
            number += 1





