class Utility:
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

    @staticmethod
    def binary_search(l,r,val, arr):
        if l <= r:
            middle = (l+r)//2
            if arr[middle] == val:
                return True
            elif arr[middle] < val:
                l = middle + 1
            else:
                r = middle - 1
            return False  

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

    # @staticmethod
    # def sort_string(str1):
    #     ln = len(str1)
    #     for i in range(ln-1):
    #         for j in range(i+1,ln):
    #             if str1[i] > str1[j]:
    #                 str1[i],str1[j] = str1[j],str1[i]
    #     print(str1)
    #     return str1


    @staticmethod
    def bubble_sort_int(arr):
        for i in range(len(arr)):
            for j in range(len(arr)):
                if arr[i] < arr[j]:
                    arr[i], arr[j] = arr[j] ,arr[i] 
            print(arr)            
        return arr

    @staticmethod
    def bubble_sortArrList(arr):
        for i in range (len(arr)-1):
            for j in range(i+1,len(arr)):
                if arr[i] < arr[j]:
                    arr[i],arr[j] = arr[j],arr[i]
        return arr

        