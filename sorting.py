#!/usr/bin/env python
# -*- coding: utf-8 -*-

import random

random.seed(1)
# randomList = [random.randint(0,100) for rnd in range(10) ]
# randomList = [77, 37, 13, 48, 76, 71, 16, 75, 41, 29]
# randomList = [77, 37, 13, 48, 77, 71, 16, 75, 41, 16] #com  numeros repetidos
#randomList = [random.randint(100,999) for _ in range(10)]
# randomList = [952, 933, 483, 383, 489, 308, 807, 671, 747, 292]
randomList = [random.randint(100,999) for _ in range(50)]
print("random input" + str(randomList))

########UTILS############
count =0
def c():#contador
    global count
    count += 1 # count comparison
def c_0():#reset contador
    global count
    count = 0
def get_c():#obtem contador
    global count
    return count

# função de analisar algortimo de ordenação
def analize(algorithm, tam=100, len=50, limit=100):
    result = 0
    errors = []
    for i in range(0,tam):
        c_0()
        v = [random.randint(0,limit) for _ in range(len) ]
        v = algorithm(v)
        if(not tester_result(v)):
            errors.append(v)
        result+= get_c()
        #print(result)
    print("média: " + str(result/tam))
    print("errors: ")
    for i in errors:
        print(i)

def tester_result(v):
    for i,j in zip(v, v[1:]):
        if(i >j):
            return False
    return True
########FIM UTILS############    


######## ALGORITMOS ############    
def bublesort(v):
    for i in range(len(v)):
        for j in range(0,len(v)-1):
            c()
            if(v[j]>v[j+1]):
                v[j],v[j+1] = v[j+1],v[j]
            
    #print(v, count)
    return v
    
def min(v):
    inx = 0
    for i in range(len(v)):
        c()
        if(v[i] < v[inx]):
                inx = i
    return inx

    
def selectionsort(v):    
    for i in range(len(v)):
        #por eu estar passando menos elementos e depois receber o index, 
        #eu preciso dizer a relacao entre os elementos que retirei e que estou colocando
        relative_min_inx = min(v[i:]) + i 
        v[i],v[relative_min_inx] = v[relative_min_inx], v[i]
#    print(v, count)
    return v


def insertionsort(v):
    for i in range(1,len(v)):
        j = i
        while j>0 and v[j-1] > v[j]:
            c()
            v[j-1],v[j] = v[j],v[j-1]
            j-=1
    #print(v, count)
    return v

"""
CARALHO QUE PÉROLA, COMPARANDO COM O REAL, QUE MERDA EU TAVA TENTANDO FAZER E CHAMAR DE INSERTION SORT?
a ideia é fazer tipo isso, mas sem o swap, eu iria passar todos para a direita e depois iria colocar o cara
além disso, a ideia era basicamente a mesma, vendo de trás pra frente, mas 1 por vez,
obviamente o algoritmo real é bem mais esperto!! ele parece um buble sort de tras pra frente

def insertioMerdasort(v):
    inx =0
    pivot = inx + 1
    for _ in range(1,len(v)):
        eleito = v[pivot]
        for i in range(pivot)[::-1]: # falta ver o caso base rsrsrssrs, então falta tudo
            if(v[pivot] < v[i]):
            # MEU MAIOR PROBLEMA ESTÁ AQUI AHHAHAHA, ao achar o primeiro maior eu já paro e faço a troca eu não continuo vendo pra frente, no insertion sort  A TROCA É FEITA E A BUSCA CONTINUA
            
                inx = i
                curr = v[i]
                for j in range(i, pivot):
                    temp = v[j+1]
                    v[j+1] = curr
                    curr = temp
                v[i] = eleito
        pivot +=1
    print(v)
""" 
def insertionBrazilSort(v):
    for i in range(1,len(v)):
        j = i - 1
        eleito = v[i]
        while j>=0 and eleito < v[j]:
            c()
            v[j+1] = v[j]
            j -=1
        v[j+1] = eleito
    #print(v, count)
    return v

def mergesort(v):
    if(len(v)!=1):
        div = int(len(v)/2)
        v1 = mergesort(v[:div])
        v2 = mergesort(v[div:])
        c()
        v =  merge2(v1,v2) if sum(v1) < sum(v2) else merge2(v2,v1)
        #print(v, count)
        return v
    else:
        c()
        return v

def merge(v1,v2):
    i1 = 0 
    i2 = 0
    ret =[]
    i=0

    while i1 < len(v1) and i2 < len(v2):
        c()
        if(v1[i1] > v2[i2]):
            ret.insert(i, v2[i2])
            i2+=1
        else:
            ret.insert(i, v1[i1])
            i1+=1
        i +=1
    resto, resto_inx = (v2, i2) if i1 == len(v1) else (v1,i1)
    for i in range(i, len(v1) +len(v2)):
        c()
        # print(i ,v2, ret)
        ret.insert(i, resto[resto_inx])
        resto_inx+=1
    #print(ret)    
    return ret

# forma aprendida na internet
def merge2(v1,v2):
    ret = []
    while v1 or v2:
        c()
        if len(v1) and len(v2):
            if v1[0] < v2[0]:
                ret.append(v1.pop(0))
            else:
                ret.append(v2.pop(0))
        
        ret.append(v2.pop(0)) if (not len(v1)) and len(v2) else None
        ret.append(v1.pop(0)) if not len(v2) and len(v1) else None
    return ret
            


def quicksort(v):
    if(len(v)>1):
        p = len(v)/2
        pivot = v[p]
        low, high =[], []
        i = 0 
        while i < len(v):
            c()
            if v[i] < pivot:
                low.append(v[i])
            elif v[i] > pivot:
                high.append(v[i])
            i+=1
        v = quicksort(low) + [pivot] +  quicksort(high)
        print(v, count)
        return v
    else:
        return v

# https://www.youtube.com/watch?v=ywWBy6J5gz8
def quicksort_dance(v):
    if(len(v)>1):
        blackhat =0
        redhat = len(v)-1
        swap = 1
        while  redhat != blackhat:
            if(swap*v[blackhat] > swap*v[redhat]):
                v[blackhat], v[redhat] = v[redhat], v[blackhat]
                blackhat,redhat =  redhat,blackhat
                swap *= -1
                redhat-=swap
            else:
                redhat-=swap
        v = quicksort_dance(v[:redhat]) + [v[blackhat]] + quicksort_dance(v[redhat+1:]) 
        print(v)
        return v
    else:
        return v
        
def bublesort_recursive(v):
    j =0 
    if(len(v)==1):
        return v
    else:
        for i in range(len(v)):
            c()
            if( v[j] > v[i]):
                v[j],v[i] = v[i],v[j]
                j+=1
            else:
                j = i
        # print(v)
        v =   bublesort_recursive(v[:j]) #+ bublesort_recursive(v[j:])
        #print(v, count)
        return v

def heapfy(v,i):
    #print(v)
    LSon = i*2 +1 # filho esquerdo
    RSon = i*2 +2 # filho direito
    if(RSon < len(v)):
        if v[i] > v[LSon] and \
            v[i] > v[RSon]:
            return v
        if v[LSon] > v[RSon]:
            v[i],v[LSon]=v[LSon],v[i]
            return heapfy(v, LSon)
        v[i],v[RSon]=v[RSon],v[i]
        return heapfy(v, RSon)
    elif LSon<len(v):
        if v[i] < v[LSon]:
            v[i],v[LSon]=v[LSon],v[i]
            return heapfy(v, LSon)
    return v
    
def createHeap(v):
    for i in range(int(len(v)/2))[::-1]:
        v = heapfy(v, i)
        
    #print(v)
    return v

def heapsort(v):
    v=createHeap(v)
    #print(v)
    for i in range(int(len(v)))[::-1]:
        v[0],v[i] = v[i],v[0]
        v = heapfy(v[:i],0) + v[i:]
    print(v)
    return v


def countingsort(v):
    max_num = max(v)
    c =[0]*(max_num+1)
    for i in range(len(v)):
        c[v[i]]+=1
        
    ret = []
    for i in range(len(c)):
        ret += [i]*c[i] 
    # print(ret)
    return ret

# considerando inteiros >0
def countingsort2(v):
    max_num = max(v)
    c = [0]*(max_num+1)
    
    #forma borra usando countingsortAux
    #for i in range(len(v)):
    #    c = countingsortAux(v[i], c)
    
    for i in range(len(v)):
        c[v[i]]+=1
    # forma mais certa, usando a segunda função: countingsortAux2
    c = countingsortAux2(c)
    ret = [None]*len(v)
    for i in v:
        ret[c[i]-1] = i
        
    print(ret)
    return ret
    
def countingsortAux(inx, c):
    for i in range(inx, len(c)):
        c[i]+=1
    return c

    
def countingsortAux2(c):
    for i in range(1,len(c)):
        c[i]+=c[i-1]
    return c

# com objetos , isto é, guarda a referencia 
# ao invés de só contar, como é o caso dos outros
# bom testar com o array de elemento repetido
def countingsort3(v):
    max_num = max(v)
    #c =[list()]*(max_num+1) 
    #c =[[]]*(max_num+1) HHAHAHAHAHH NAOOOOOOOOO USAAAAAAAAAAAR
    c = [ list() for _ in range(max_num+1)] # pode usar [] instead de list()
    # print(c)
    for i in range(len(v)):
        # print(v[i],c[v[i]], i)
        if(i in [8,9]):
            print(type(c[v[i]]), c[v[i]], c)
        """if type(c[v[i]]) is not  list:
            c[v[i]] = []

        c[v[i]] += [v[i]]"""
        c[v[i]].append(v[i])
        if(i in [9]):
            print(type(c[v[i]]), c[v[i]], c)
        # print(v[i],c[v[i]], i)
    #print(c)
    ret = []
    for i in range(len(c)):
        if(c[i]):
            ret += c[i]
    print(ret)
    return ret

"""
 radix sort LSD começa do dígito menos significativo até o mais significativo, ordenando tipicamente da seguinte forma: chaves curtas vem antes de chaves longas, e chaves de mesmo tamanho são ordenadas lexicograficamente. Isso coincide com a ordem normal de representação dos inteiros, como a seqüência "1, 2, 3, 4, 5, 6, 7, 8, 9, 10".
o radix sort MSD trabalha no sentido contrário, usando sempre a ordem lexicográfica, que é adequada para ordenação de strings, como palavras, ou representações de inteiros com tamanho fixo. A seqüência "b, c, d, e, f, g, h, i, j, ba" será ordenada lexicograficamente como "b, ba, c, d, e, f, g, h, i, j".
"""
#o algoritmo assume valores maiores que zero
def radix_base10(v):
    e = 1

    maior =max(v)
    while(maior/e>0):
        c = [0]*10
        temp = [None]*len(v)
        for i in range(len(v)):
            # print((v[i]/e)%10)
            c[(v[i]/e)%10]+=1
        for i in range(0,len(v)-1):
            c[i+1]+=c[i]
        for i in range(len(v))[::-1]:
            temp[c[(v[i]/e)%10]-1] = v[i]
            """linha abaixo, coloca o cara na posição anterior,
             por isso tem que vir de trás pra frente,
              por isso tem que contar não só o seu mais os anteriores também, 
              dessa forma o index em c dá o index que será o de v
            """
            c[(v[i]/e)%10]-=1
            
        v = list(temp) 
        # v = temp[:] # outra forma de copiar lista sem passar referencia da lista
        e=e*10   
    print(v)

    
def selectKth(v, k):
    i = 0
    low = []
    high = []
    medians = []
    print("entrada", v)
    if(len(v)<=5):
        v = insertionsort(v[i:i+5])
        print( k, v[k-1])
        return v[k-1]
    while i + 5 <= len(v):
        # incrivel, se vc fazer slice da lista com o limite 
        # superior ao tamanho da lista, ela só pega até o tamanho dela
        temp = insertionsort(v[i:i+5])
        medians += [temp[2]]
        i+=5
    
    medians = insertionsort(medians)
    median= medians[len(medians)/2]
    
    #partition inline
    for i in v:
        if i < median:
            low += [i]
        elif i>median:
            high += [i]
            
    if len(low) == k -1: # k-1 pq o quarto é o elemento 3 da lista
        print(median)
        return median
    elif len(low) > k-1:
        # low+=medians
        return selectKth(low, k)
    else:
        # A = input("break press number",  )
        return selectKth(high, k- len(low)-1)
        
def partition(v, val):
    low = []
    high = []
    # pivot = v[inx]
    for i in v:
        if i < val:
            low += [i]
        elif i>val:
            high += [i]
            
    return low +[val] + high
#bublesort(randomList)
#selectionsort(randomList)
#insertionsort(randomList)
#insertioMerdasort(randomList)
#insertionBrazilSort(randomList)
#mergesort(randomList)
#createHeap(randomList)
#heapsort(randomList)
#countingsort(randomList)
#countingsort2(randomList)
#countingsort3(randomList)
# VERFIICAR QUAL TEMPO QUE É FEITO ORDENAÇÃO USANDO MERGESORT E INSERTION SORT(PARA ARRAYS MENORES DO MERGE)
#radix_base10(randomList)
# quicksort_dance(randomList)

# K = input("qual elemento de" + str(len(randomList)) + " elementos voce quer?") 
# s = selectKth(randomList,K)
# m = mergesort(randomList)[K-1]
# isCorret = s == m
# interessante, essa linha na verdade imprime uma tupla, 
#achava que não podia fazer print arg em python3 deveria fazer python(arg)
# print ("select sort:",s, "\n mergesort: ", m, "\nesta certo?", isCorret)
# print "select sort:",s, "\nmergesort: ", m, "\nesta certo?", isCorret


#shellsort(randomList)
#bucketsort(randomList)
#cocktail(randomList) #melhorar???????
#rsacode()

# algthms = [bublesort, selectionsort, insertionsort, insertionBrazilSort, mergesort, bublesort_recursive, quicksort]
# for i in algthms:
    # print(i)
    # analize(i)

# v = selectionsort(randomList)
# print(tester_result(v), v)
# tester_result(bublesort(randomList))
