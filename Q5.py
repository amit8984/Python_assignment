#Binary search which return index of element to be searched in the list


def binarySearchIndex(inputList,searchElement,startIndex,finalIndex):
    if(finalIndex>=startIndex):
        midIndex=int(startIndex+(finalIndex-1)/2)
        if(inputList[midIndex]==searchElement):
            return midIndex
        elif(inputList[midIndex]>searchElement):
            return binarySearchIndex(inputList,searchElement,startIndex,midIndex-1)
        elif(inputList[midIndex]<searchElement):
            return binarySearchIndex(inputList,searchElement,midIndex+1,finalIndex)
        else:
            return -1
        

if __name__=='__main__':
    n=int(input("enter number of elements:"))
    inputList=[]
    print("Enter elements of list with sorted:")
    for index in range(n):
        ele=int(input())
       # print(ele)
        inputList.append(ele)
    
    print("Enter an element to be searched")
    searchElement=int(input())
    length=len(inputList)
    startIndex=0
    finalIndex=length-1
    print(binarySearchIndex(inputList,searchElement,startIndex,finalIndex))
    
            
        
        
    

