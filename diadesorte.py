#encoding=utf-8
import random
meses=['janeiro','fevereiro','março','abril','maio','junho','julho','agosto','setembro','outubro','novembro','dezembro']
dias=31
qtdNum=7
base=[0]*dias
for i in range(dias):
    base[i]=i+1
sorteio=random.sample(base[8:23],qtdNum)
mes=random.sample(meses[1:3],1)
sorteio.sort()
print(sorteio, mes, sep=' - ')
