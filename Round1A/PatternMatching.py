import re

def validar(arr,e):
  band=True
  S=''
  for j in arr:
    if j=='*':
      S=S+'[A-Z]*'
    else:
      S=S+j
  Regex_Pattern = r'^{}$'.format(S)
  Test_String=e
  match = re.findall(Regex_Pattern, Test_String)
  if len(match)==0:
    band=False
  return band

def f(arr):
  maxi=arr[0]
  for i in arr:
    if len(i)>len(maxi):
      maxi=i
  return maxi
      

def solve(arr,r):
    salida=''
    r.sort(key=len)
    rules=r[-1]
    band=0
    while band==0:
      opc=[]
      for i in range(len(arr)):
        if len(arr[i])!=0:
          opc.append(arr[i].pop(0))

      if len(opc)==0:
        band=1
      else:  
        salida=salida+f(opc)
        
    if validar(rules,salida):
        return salida
    else:
        return '*'




T=int(input().strip())
for t in range(1, T+1):
    N=int(input().strip())
    ar=[]
    rls=[]
    for j in range(N):
        ent=input().strip()
        rls.append(ent.split('*'))
        ar.append(ent)

    salida=solve(rls,ar)
    print("Case #"+str(t)+": "+salida)