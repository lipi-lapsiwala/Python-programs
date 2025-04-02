#Addition of all elements of a list and sublists

given_list = [1,2,3,[10,20],45,[50,50],100]

def listadder(mylist):
  newlist = mylist
  sum = 0
  for i in newlist:
    if isinstance(i,int):
      sum = sum+i
    else:
      #listadder(i)
      for j in i:
        sum = sum+j
  return sum

sum = listadder(given_list)
print(sum)
