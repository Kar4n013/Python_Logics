#Replace 0's in integer with 1# 
n1 = 8010420
print("Before Operations: ",n1)

#Method1#
n2 = n1
result = " "
while(n2 > 0):
    if(n2 % 10 == 0):
        result = "1" + result
    else:
        result = str(n2%10) + result
    n2 = n2 // 10

print("After Operations: ",result)

#Method2 the int will be converted to string and then 0's will be replaced#
print("Integer is first converted to string then values are changed")
result = str(n1).replace('0','1')
print("After Operations: ",result)
  