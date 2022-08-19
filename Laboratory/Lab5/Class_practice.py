list = ['a','b','c','d','e','f']
i = 0
var =''
while True:
    var = list[i]
    i +=1
    if var == 'd':
        break
    print (var)

list = ['a','b','c','d','e','f']
for i in list:
  if i == 'd':
    break
  print (i)

lst = [4, 2, 1, 6, 7]
new_lst = []
while lst:
  if lst[0]%2==0:
    new_lst += [lst[0]]
  lst = lst[1:]

print(new_lst)

lst = [4,2,1,6,7]
new_lst = []
for i in lst:
    if i%2==0:
        new_lst.append(i)

print (new_lst)

def sq(x):
  return x**2
print (sq(2))

lambda_sq = (lambda x : x**2)
print (lambda_sq(2))
print ((lambda x : x**2) (2))
print ((lambda x,y,z : x**2 + 2*y - z) (5,6,7))