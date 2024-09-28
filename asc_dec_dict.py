import operator
d={1:10,2:12,3:50,4:65,5:55}
print('Original Dictionary',d)
sorted_d=sorted(d.items(),key=operator.itemgetter(1))
print('Ascending Order:',sorted_d)
sorted_d=dict(sorted(d.items(),key=operator.itemgetter(1),reverse=True))
print('decending Order:',sorted_d)
     
