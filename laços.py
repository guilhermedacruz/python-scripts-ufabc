# -*- coding: utf-8 -*-
"""laços.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1SZZ5j6uh5QhECkvwKVG4SWzAyBlSsCpv
"""

nota1 = float(input("Qual a nota 1? "))
nota2 = float(input("Qual a nota 2? "))
nota3 = float(input("Qual a nota 3? "))
soma = nota1+ nota2 + nota3
media = soma/3
print(media)

soma = 0.0
nn= int(input("Quantas notas? "))
for i in range(0,nn,1):
  nota = float(input("Qual a nota" + str(i) + "?"))
  soma = soma + nota
media = soma / nn
print(media)

n = 3
for i in range(0, n):
  temperatura = float(input("digite uma temperatura"))
  if temperatura < -273.15:
    print("Temperatura invalida")
    break
  elif temperatura < 0:
    print("Muito frio")

sum= 0
for i in range(0,10):
  val = int(input("Digite um valor"))
  if val < 0:
    print("erro")
    break
  sum += val
print(sum)

acertou= False
while not acertou:
  senha = input()
  if senha == "1234":
    acertou = True
  else:
    print("erro, try again")
print("sucess")

lista = ["ana", "b", "c"]
for i in range(0, len(lista)):
  print(lista[i])

sair = False
lista = []
while not sair:
  word = input()
  if word == "sair":
    sair = True
    print("EXIT")
  else:
    lista.append(word)
print(lista)

lista1= [1,2,3,4]
print(lista1)
lista2=[7,8]
print(lista2)
lista3= lista1+lista2
print(lista3)
lista3.append(20)
print(lista3)