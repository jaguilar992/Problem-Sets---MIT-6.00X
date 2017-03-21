

```python
from ARBOL import *
```

![ARBOL][img]
[img]:https://ajedrez92.files.wordpress.com/2017/03/diburrrjo1.png


```python
k=ARBOL()
k.CREAi(1,[
    k.CREAi(2,[
        k.CREA0(4),
        k.CREA0(5)
    ]),
    k.CREA0(3)
])
```




    4




```python
print "i\thijo\tdata\thermano"
for i in range(0,len(k.data)):
    print str(i)+"\t"+str(k.hijo_mas_izq[i])+"\t"+str(k.data[i])+"\t"+str(k.hermano_dere[i])
```

    i	hijo	data	hermano
    0	-1	4	1
    1	-1	5	-1
    2	0	2	3
    3	-1	3	-1
    4	2	1	-1
    

![Arbol][imagen]
[imagen]:https://ajedrez92.files.wordpress.com/2017/03/dibujo21.png


```python
A=ARBOL()
A.CREAi(1,[
    A.CREAi(2,[
        A.CREAi(5,[
            A.CREA0(8)
        ]),
        A.CREA0(6)
    ]),
    A.CREA0(3),
    A.CREAi(4,[
        A.CREA0(7),
        A.CREA0(9)
    ])
])
```




    8




```python
print "i\thijo\tdata\thermano"
for i in range(0,len(A.data)):
    print str(i)+"\t"+str(A.hijo_mas_izq[i])+"\t"+str(A.data[i])+"\t"+str(A.hermano_dere[i])
```

    i	hijo	data	hermano
    0	-1	8	-1
    1	0	5	2
    2	-1	6	-1
    3	1	2	4
    4	-1	3	7
    5	-1	7	6
    6	-1	9	-1
    7	5	4	-1
    8	3	1	-1
    


```python
print A.PADRE(8)
print A.PADRE(6)
print A.HERMANO_DER(6)
print A.PADRE(6)
print A.HERMANO_IZQ(6)
print A.HIJO_MAS_DER(5)
```

    5
    2
    None
    2
    5
    None
    


```python

```
