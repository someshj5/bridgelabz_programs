# from math import *
class Utilities():
    @staticmethod
    def is_anagram(str1,str2):

        str1 = str1.replace(' ','').lower()
        str2 = str2.replace(' ','').lower()

        if sorted(str1) == sorted(str2):
            print('True')
            return True
        else:
            return False
            # print('not an anagram')


    #------------------------------------------------------------------   
    @staticmethod
    def Is_prime_number(num):
        for i in range(2,num):
            if num %i == 0:
                print('it is not a prime number')
                return False
                # break
            else:
                print('it is prime')
                return True
    #-------------------------------------------------------------------            
    @staticmethod
    def Is_palindrome(str1):
        rev = str1[::-1]
        if rev == str1:
            print('it is Palindrome')
            return True
        else:
            print('not a palindrome')
            return False
        
    # -------------------------------------------------------------------
    @staticmethod
    # def binary_search(l, r, val, arr):
    #     if l <= r:
    #         middle = (l + r) // 2
    #         if arr[middle] == val:
    #             print('Present')
    #             return True
    #         elif arr[middle] < val:
    #             l = middle + 1
    #         else:
    #             r = middle - 1
    #         print('Absent')
    #         return False 
    # binary_search(1,4,3,[1,2,3,4,5,6])
    #----------------------------------------------------------------------
    @staticmethod
    def searchword(list,word):
        l = 0
        r = len(list)-1
        while l <= r:
            mid = (l+r)//2
            if list[mid].lower() == word.lower():
                return 1
            elif list[mid].lower() < word.lower():
                l = mid+1
            else:
                r = mid-1
        else:
            return 0
#-------------------------------------------------------------------
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

    #--------------------------------------------------------------------
    @staticmethod
    def sortArrList(arr):
        for i in range (len(arr)-1):
            for j in range(i+1,len(arr)):
                if arr[i] > arr[j]:
                    arr[i],arr[j] = arr[j],arr[i]

        return arr
    #     # sortArrList([9,3,5,2,1])

    #-----------------------------------------------------------------------
    @staticmethod
    def sort_string(str1):
        ln = len(str1)
        for i in range(ln-1):
            for j in range(i+1,ln):
                if str1[i] > str1[j]:
                    str1[i],str1[j] = str1[j],str1[i]
        print(str1)
        return str1
    # sort_string('dba')

    #---------------------------------------------------------------------------
    @staticmethod
    def bubble_sort(arr):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j] ,arr[i] 
            print(arr)            
        return arr
    #     # bubble_sort([7,1,8,2,3])
#---------------------------------------------------------------------------------------
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
    #     # _ANS = __insertionSort__.__func__()


#-------------------------------------------------------------------------------------
    @staticmethod
    def getprime(N,primeArr):
        for num in range(0,N+1):
            if num > 1 :
                for i in range(2,num):
                    if num % i == 0:
                        break
                else:
                    print(num),
                    primeArr.append(num)
        print('The total prime number are:',len(primeArr))
    
#------------------------------------------------------------------------------------   
    @staticmethod
    def Palindrome_num(N1):
        for i in (N1):
            temp = i
            rev = 0
            while temp > 0:
                digit = temp % 10
                rev = rev * 10 + digit
                temp = temp/10
            if i == rev:
                print(i),
    #---------------------------------------------------------------------------------        

    @staticmethod
    def Prime_anagram(primearr):
        
        for i in primearr:
            for j in primearr:
                i = str(i)
                j = str(j)
                if sorted(i) == sorted(j):
                    print(i,'and', j)
    #----------------------------------------------------------------------------------
    @staticmethod
    def Temp_conversion(temp,n):
        if n == 0:

            F = temp 
            Celcius = (F - 32) * 5/9
            print(Celcius)
            print('the conversion of temperature Fahrenhiet To Celsius =  ', Celcius,'C')
        elif n == 1:

            C = temp 
            Fahrenhiet = (C * 9/5) + 32
            print('the conversion of temperature Celcius to Fahrenhiet = ',Fahrenhiet,'F',)
    

    # Temp_conversion(100,1)
    #----------------------------------------------------------------------------------------

    @staticmethod
    def calculatePayment(P,Y,R):
        n = 12 * Y
        r = R / (12 * 100)
        payment = (P * r)/(1 - (1 + r) ** (-n))
        print('Payment:', payment)
        return payment
    # calculatePayment(1200,1,13)

    #-----------------------------------------------------------------------------------------
    @staticmethod
    def dayofWeek(day,month,year):
        lists = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']
        y0 = year - (14 - month) // 12
        x = y0 + y0 // 4 - y0 // 100 + y0 // 400
        m0 = month + 12 * ((14 - month) // 12) - 12
        d0 = (day + x + 31 * m0 // 12) % 7
        print('Day of week:', lists[d0])
    # dayofWeek(5,6,2019)

    #-----------------------------------------------------------------------------------------

        
