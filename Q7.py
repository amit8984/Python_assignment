#fetching company name from employee email

def fectCompany(email):
    index=email.index('@')
    compName=""+email[index+1:-4]
    return compName

my_input=input()
while(len(my_input)>0):
    print("Company name is :",fectCompany(my_input))
                  #Do whatever you want
    print("Enter email id:")
    my_input=input()  #take next input
    


                
