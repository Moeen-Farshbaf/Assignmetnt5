
n=int(input())
kh_pa_t= [[[] for j in range(n)] for i in range(n)]

for i in range(n):
    for j in range(n):
        kh_pa_t[i][0]=1
        kh_pa_t[i][i]=1
for i in range(2,n):
    for j in range(1,i):
        kh_pa_t[i][j]=kh_pa_t[i-1][j]+kh_pa_t[i-1][j-1]

for i in range(n):
    for j in range(i+1):
        print(kh_pa_t[i][j],end='\t')
    print()