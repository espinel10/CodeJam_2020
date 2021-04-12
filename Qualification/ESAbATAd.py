import sys



def get_indices(B):
  if B==100:
    aux=[]
    B=100
    for i in range(0,46,4):
      auxi=[i,i+1,i+2,i+3,i+4,B-(i+4),B-(i+3),B-(i+2),B-(i+1),B-i]
      aux.append(auxi)
    aux.append([44, 45, 46, 47, 48, 49, 50, 51, 52, 53])
    return aux[:]
  elif B==20:
    aux=[]
    B=19
    for i in range(0,6):
      auxi=[i,i+1,i+2,i+3,i+4,B-(i+4),B-(i+3),B-(i+2),B-(i+1),B-i]
      aux.append(auxi)
    return aux
  else:
    return [[0,1,2,3,4,5,6,7,8,9],[0,1,2,3,4,5,6,7,8,9]]

def trasnformar(t,arr):
    if t==4:
        return arr[:]
    if t==1:
        flip = {'0': '1', '1': '0'}
        new = [flip[c] if c in flip else c for c in arr]
        return new[:]
    if t==2:
        new=arr[:]
        new.reverse()
        return new[:]
    if t==3:
        flip = {'0': '1', '1': '0'}
        new = [flip[c] if c in flip else c for c in arr]
        new.reverse()
        return new[:]



def iguales(arr1,arr2):
    band=True
    for i in range(len(arr1)):
        if arr1[i]=='.':
            continue
        else:
            if arr1[i]!=arr2[i]:
                band=False
                break
    return band



def query(ii):
    print(str(ii+1),flush=True)
    response=input()
    if response=='N':
        sys.exit()
    return response

def solve(B):
    bandera=0
    solucion=['.'] * B
    mov=get_indices(B)
    for i in mov:
      
      examin=[]
      xxx=[]
      for kk in i:
          xxx.append(solucion[kk])
          response=query(kk)
          examin.append(response)
      resp=4
      if bandera==1:
        if iguales(trasnformar(1,xxx),examin):
            resp=1
            solucion=trasnformar(resp,solucion)[:]
        elif iguales(trasnformar(2,xxx),examin):
            resp=2
            solucion=trasnformar(resp,solucion)[:]
        elif iguales(trasnformar(3,xxx),examin):
            resp=3
            solucion=trasnformar(resp,solucion)[:]
     

      
      dicc=dict(zip(i[:],examin))
      for key in dicc:
          if solucion[key]=='.':
            solucion[key]=dicc[key]
      bandera=1 

    print("".join(solucion),flush=True)
    if input()=='N':
        sys.exit()
    
# I/O
num_cases, num_bits = map(int, input().split())
for _ in range(1, num_cases + 1):
    solve(num_bits)

sys.exit()