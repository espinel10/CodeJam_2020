
def solve(arr,N):
  prefix,sufix = '', ''
  for i in range(N):
    if len(prefix)< len(arr[i][0]):
      prefix=arr[i][0]
    if len(sufix)< len(arr[i][-1]):
      sufix=arr[i][-1]

  print(prefix)
  print(sufix)
  for i in range(N):
    if not prefix.startswith(arr[i][0]):
      return '*'
    if not sufix.endswith(arr[i][-1]):
      return '*'
  salida= [prefix]
  for i in range(N):
    print("-----------------")
    print(salida)
    salida.extend(arr[i][1:-1])
  salida.append(sufix)
  return "".join(salida)

  


T=int(input().strip())
for t in range(1, T+1):
    N=int(input().strip())
    arr=[]
    for j in range(N):
        ent=input().strip()
        arr.append(ent.split('*'))
    
    salida=solve(arr,N)
    print("Case #"+str(t)+": "+salida)