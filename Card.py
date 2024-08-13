class CardItem:
    discountRate=0.8
    itemCount=0
    def displayItemCount(cls):
        return f"{cls.itemCount} item created"
    def createItem(cls, dataStr):
        name,price,quantity=dataStr.split(',')
        return cls(name,price,quantity)
    
    def __init__(self,name,price,quantity):
        self.name=name
        self.price=price
        self.quantity=quantity
        CardItem.itemCount += 1
        
    def calculateTotal(self):
        return self.price * self.quantity
    
    def applyDiscount(self):
        self.price = self.price * CardItem.discountRate

class Coupon:
    def __init__(self,code,discount):
        self.code=code
        self.discount=discount
        
c1=Coupon("code1",0.8)
c2=Coupon("code2",0.7)
c3=Coupon("code3",0.9)
    
item1=CardItem("Tel",5000,2)
item2=CardItem("Pc",7000,1)
item3=CardItem("Book",200,2)
    
class ShoppingCart:
    couponList=[c1,c2,c3]
    def __init__(self,liste):
        self.liste=liste
        
    def addItem(self,item):
        self.liste.append(item)
        for k in self.liste:
            if(k==item):
                print(f"{item.name} is added succesfully")
        
    def displayItems(self):
        for i in self.liste:
            print(f"{i.name} {i.price}")
            
    def calculateTotals(self):
        return sum([item.calculateTotal() for item in self.liste])
    
    def removeItem(self,cartItem):
        self.liste=[item for item in self.liste if item != cartItem]
    
    def clear(self):
        self.liste=[]
        
    @classmethod
    def getCoupons(cls):
        return [coupon.code for coupon in cls.couponList]
    
    @classmethod
    def getCoupon(cls,code):
        return next(filter(lambda c: c.code == code, ShoppingCart.couponList))
    
    def apply_coupon(self,code):
        if code not in ShoppingCart.getCoupons():
            raise ValueError(f"coupon code is not true: {code}")

        coupon= ShoppingCart.getCoupon(code)
        
        for index in range(0,len(self.liste)):
            self.liste[index].price=self.liste[index].price * coupon.discount
        
sc=ShoppingCart([item1,item2])
sc.addItem(item3)
#sc.displayItems()
print(f"Total price is {sc.calculateTotals()}")
#sc.removeItem(item1)
#sc.displayItems()
sc.apply_coupon("code2")
print(f"The price with discount {sc.calculateTotals()}")