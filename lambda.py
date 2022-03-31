x=lambda x,y:x+y
print(x(3,4))
def product(N):
   return lambda a:a*N

result=product(5)
print(result(4))

