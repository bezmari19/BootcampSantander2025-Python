#estruturas de dados set:
#não possui objetos repetidos, usamos sets para representar conjuntos matemáticos ou eliminar itens duplicados de um iterável

#usar set não garante a ordem da lista e conjuntos em python não suportam indexação, portanto você precisa converter o set para uma lista
#métodos da classe set: {}union:
conjunto_a = {1,2}
conjunto_b = {3,4}
conjunto_a.union(conjunto_b)
print(conjunto_a.union(conjunto_b))

#classe {}intersection:
conjunto_1 = {1,2,3}
conjunto_2 = {2,3,4}
conjunto_1.intersection(conjunto_2)
print(conjunto_1.intersection(conjunto_2))
conjunto_1.difference(conjunto_2)
conjunto_2.difference(conjunto_1)
print(conjunto_1.difference(conjunto_2))
print(conjunto_2.difference(conjunto_1))

#{}.issubset
conjunto_um = {1,2,3}
conjunto_dois = {4,1,2,5,6,3}
conjunto_um.issubset(conjunto_dois)
conjunto_dois.issubset(conjunto_um)
print(conjunto_um.issubset(conjunto_dois))
print(conjunto_dois.issubset(conjunto_um))

#{}.isdisjoint
conjuntoA = {1,2,3,4,5}
conjuntoB = {6,7,8,9}
conjuntoC = {1,0}
conjuntoA.isdisjoint(conjuntoB)
conjuntoA.isdisjoint(conjuntoC)
print(conjuntoA.isdisjoint(conjuntoB))
print(conjuntoA.isdisjoint(conjuntoC))

#{}.add
sorteio = {1,23}
sorteio.add(25)
sorteio.add(42)
sorteio.add(25)
print(sorteio)

#.{}clear
sorteio = {1,23}
sorteio
sorteio.clear()
sorteio
print(sorteio)

#{}.copy
#{}.discard
#{}.pop
#{}.remove

