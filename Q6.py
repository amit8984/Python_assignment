#program to check number is divisble by 5 and 7 

l=0
def Gen(max):
    for num in range(1,max+1):
        
        if (num%35==0):
            yield num


if __name__=='__main__':
    print("enter the maximum range of input:")
    n=int(input())
    
    list1=[]
    for item in Gen(n):
        #print(item)
        list1.append(item)
    print(*list1,sep=", ")    
    

            
