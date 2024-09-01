print("1 - add")
print("2 - subtract")
print("3- multiply")
print("4 - division")
option = (int(input("choose the operator to perform operation:")))

if(option in [1,2,3,4]):
      num1=int(input("entre first number"))
      num2=int(input("enter secound number"))
      if(option==1):
         result= num1+num2
      elif(option==2):
          result= num1-num2
      elif(option==3):
          result = num1*num2
      elif(option==4):
          result= num1/num2
      else:
          ("enter vaild option")
print("the result of the operation is {}".format(result))





