import random
class CouponNumber:
   
        
    @staticmethod
    def coupon_number():
        number = int(input('Enter a value  : ')) 
        result = []
        for num in range(number) :
            ran = random.randint(0,number)
            if ran not in result:
                result.append(ran)
       
            
        print('the distinct coupon numbers are:',result)
            
        
c = CouponNumber()
c.coupon_number()