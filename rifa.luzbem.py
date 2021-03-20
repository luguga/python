#encoding=utf-8
import random

colunas = ['A','B','C','D','E']
linhas = 20
valores = 5
base = []
for a in colunas:
  for b in range(1,linhas):
    base.append(a+str(b))
    
sorteio=random.sample(base,valores)

print(sorteio)

['B10', 'B11', 'C19', 'D1', 'E10']
['','','','','']
['A0', 'A13', 'A4', 'C9', 'E1']
['','Mônica','','','Vilma']
