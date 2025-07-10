#metodo [].append
lista = []
lista.append(1)
lista.append('Python')
lista.append([40, 30, 20])

print(lista)  #[1, 'Python', [40, 30, 20]]

#metodo [].copy
lista = (1, 'Python', [40, 30, 20])
l2 = lista.copy()
print(lista)
print(id(l2), id(lista))

#metodo [].count
cores = ['vermelho', 'azul', 'verde', 'azul']
cores.count('vermelho') #1
cores.count('azul') #2
cores.count('verde') #1

#metodo [].extend
linguagens = ['python', 'js', 'c']
print(linguagens)
linguagens.extend(['java', 'csharp'])
print(linguagens)

#metodo [].index
linguas = ['java', 'csharp', 'python', 'js', 'c']
linguas.index('python') #3
linguas.index('java') #1

#metodo [].pop
linguagem = ['python', 'js', 'c', 'java', 'csharp']
linguagem.pop() #csharp
linguagem.pop() #java
linguagem.pop() #c
linguagem.pop(0) #python

#metodo [].remove
linguagem1 = ['python', 'js', 'c', 'java', 'csharp']
linguagem1.remove('python')

#metodo [].reverse
linguagem2 = ['python', 'js', 'c', 'java', 'csharp']
linguagem2.reverse()
print(linguagem2)

#metodo [].sort
linguagem3 = ['python', 'js', 'c', 'java', 'csharp']
linguagem3.sort(reverse=True)
linguagem3.sort(key=lambda x: len(x))

#metodo len()
len(linguagem3)

#metodo sorted()
sorted(linguagem3, key=lambda x: len(x))
print(sorted(linguagem3))







