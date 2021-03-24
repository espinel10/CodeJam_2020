from collections import deque
def solve(tasks):
  turno={'C':None , 'J':None}
  salida=[[] for i in range(len(tasks))]
  while len(tasks)!=0:
    task=tasks.pop()
    t=task[0]
    #desocupo
    for i in turno:
      interval=turno[i]
      if interval==None:
        continue
      if interval[1]<=t:
        turno[i]=None
    cont=0
    #ocupo al primero desocupado
    for i in turno:
      if turno[i]==None:
        turno[i]=task
        #salida=salida+i
        salida[task[2]].append(i)
        break
      else:
        cont=cont+1
    if cont==2:
      salida=[]
      break
  sol=''
  for i in salida:
    sol=sol+"".join(i)
  if sol=='':
    return 'IMPOSSIBLE'

  return sol

T=int(input().strip())
for i in range(1,T+1):
    N=int(input().strip())
    ent=[]
    for zetta in range(N):
        a,b=input().split(" ")
        ent.append((int(a),int(b),zetta))

    pot=sorted(ent,key=lambda x:x[0],reverse=True)
    e=deque(pot)
    sol=solve(e)
    print("Case #"+str(i)+": "+sol)








  