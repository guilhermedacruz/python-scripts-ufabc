# -*- coding: utf-8 -*-
"""compare-the-triplets.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1IOlLTVf23iZByQoaJhy_iG8Pp3Y0wxBQ
"""

a = [5 , 6, 7]
b = [3, 6, 10]
pointsA= 0
pointsB= 0  
for i in a:
  for j in b:
    if i > j:
      pointsA += 1
    elif i < j:
      pointsB += 1
      print("[", pointsA ,",", pointsB ,"]")