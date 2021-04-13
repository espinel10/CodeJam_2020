import sys
class DB:
    def __init__(self,B):
        self.data=['*']*B
        self.B=B
        self.i_comp=None
        self.i_rever=None
        self.contador=0

        self.solve()

    def query(self, i):
        self.contador=self.contador+1
        print(str(i + 1), flush=True)
        response = input()
        if response == 'N':
            sys.exit()
        return response

    def complement(self):
        if self.i_comp is None:
            _ = self.query(0)
        else:
            if self.data[self.i_comp]!=self.query(self.i_comp):
                flip = {'0': '1', '1': '0'}
                self.data = [flip[c] if c in flip else c for c in self.data]
            

    def revers(self):
        if self.i_rever is None:
            _= self.query(0)
        else:
            if self.data[self.i_rever]!=self.query(self.i_rever):
                self.data=self.data[::-1]
            

    def first_last(self,i):
        j= self.B - i - 1
        self.data[i]=self.query(i)
        self.data[j]=self.query(j)

        if self.i_comp is None and  self.data[i] == self.data[j]:
            self.i_comp=i
        if self.i_rever is None  and self.data[i]!=self.data[j]:
            self.i_rever=i

    def quantum_fluctuation(self):
        self.complement()
        self.revers()
        

    def solve(self):
        posix=0
        for i in range(5):
            self.first_last(i)
            posix=posix+1


        while '*' in self.data and posix <self.B//2:
            if posix%4==1:
                self.quantum_fluctuation()
            self.first_last(posix)
            posix=posix+1

        print("".join(self.data),flush=True)
        if input()=='N':
            sys.exit()


# I/O
num_cases, num_bits = map(int, input().split())
for _ in range(1, num_cases + 1):
    obj=DB(num_bits)

sys.exit()