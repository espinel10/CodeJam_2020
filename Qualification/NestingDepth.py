def solve(torr):
  tor=torr[:]
  if sum(tor)<1:
    return "".join(list(map(str,tor)))
  f=lambda x:x-1
  salida=[]
  aux=[]
  for i in tor:
    if i==0:
      if len(aux)>0:
        salida.append(aux[:])
      salida.append([i])
      aux.clear()
    else:
      aux.append(i)
  if len(aux)>0:
    salida.append(aux)
  output=""
  for i in salida:
    ult=i[:]
    ult=list(map(f,ult))
    if len(ult)==1 and i[0]==0:
      output=output+str(i[0])
    else:
      output=output+"("+solve(ult)+")"
  return output
  
def devol(entrada,output):
  sal=output[:]
  cont=0
  for i in range(0,len(sal)):
      if sal[i]=='(' or sal[i]==')':
          continue
      else:
          sal[i]=str(entrada[cont])
          cont=cont+1    

  return "".join(sal)

T=int(input().strip())
for i in range(T):
    ent=list(map(int,list(input())))
    resp=devol(ent,list(solve(ent)))
    print("Case #"+str(i+1)+": "+resp)
