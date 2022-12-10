import time, numpy as np, matplotlib.pyplot as plt 
i, lista,t, tt = 0, [], [], []

def Finaliza(_):
    t2 = time.perf_counter_ns()
    tt.append(t2 - t1)
    print(f"\nO Determinante da Matriz {_}x{_} é: {resultado: 2.2f}")
#F Conta sem Numpy
def Y2():
    resultado = lista[0]*lista[3] - lista[1]*lista[2]
    return resultado

def Y3():
    resultado = (lista[0]*lista[4]*lista[8]
                 + lista[1]*lista[5]*lista[6] 
                 + lista[2]*lista[3]*lista[7]) - (lista[2]*lista[4]*lista[6] 
                                                  + lista[0]*lista[5]*lista[7] 
                                                  + lista[1]*lista[3]*lista[8])
    return resultado

def Y4():
    resultado = (lista[0]*lista[5]*lista[10]*lista[15]) - (lista[0]*lista[5]*lista[11]*lista[14]) - (lista[0]*lista[6]*lista[9]*lista[15]) 
    + (lista[0]*lista[6]*lista[11]*lista[13]) 
    + (lista[0]*lista[7]*lista[9]*lista[14]) - (lista[0]*lista[7]*lista[10]*lista[13]) - (lista[1]*lista[4]*lista[10]*lista[15]) 
    + (lista[1]*lista[4]*lista[11]*lista[14]) 
    + (lista[1]*lista[6]*lista[8]*lista[15]) - (lista[1]*lista[6]*lista[11]*lista[12]) - (lista[1]*lista[7]*lista[8]*lista[14]) 
    + (lista[1]*lista[7]*lista[10]*lista[12]) 
    + (lista[2]*lista[4]*lista[9]*lista[15]) - (lista[2]*lista[4]*lista[11]*lista[13]) - (lista[2]*lista[5]*lista[8]*lista[15]) 
    + (lista[2]*lista[5]*lista[11]*lista[12]) 
    + (lista[2]*lista[7]*lista[8]*lista[13]) - (lista[2]*lista[7]*lista[9]*lista[12]) - (lista[3]*lista[4]*lista[9]*lista[14]) 
    + (lista[3]*lista[4]*lista[10]*lista[13]) 
    + (lista[3]*lista[5]*lista[8]*lista[14]) - (lista[3]*lista[5]*lista[10]*lista[12]) - (lista[3]*lista[6]*lista[8]*lista[13]) 
    + (lista[3]*lista[6]*lista[9]*lista[12])
    return resultado
#F Exibir visualmente
def X2():
    return print(f"\nSua Matriz 2x2 ficou assim: \n|{lista[0]}  {lista[1]}|",
                  f"\n|{lista[2]}  {lista[3]}|")

def X3():
    return print(f"\nSua Matriz 3x3 ficou assim: \n|{lista[0]}  {lista[1]}  {lista[2]}  |{lista[0]}  {lista[1]}|",
          f"\n|{lista[3]}  {lista[4]}  {lista[5]}  |{lista[3]}  {lista[4]}|",
          f"\n|{lista[6]}  {lista[7]}  {lista[8]}  |{lista[6]}  {lista[7]}|")

def X4():
    return print(f"\nSua Matriz 4x4 ficou assim: \n|{lista[0]}  {lista[1]}  {lista[2]}  {lista[3]}|",
          f"\n|{lista[4]}  {lista[5]}  {lista[6]}  {lista[7]}|",
          f"\n|{lista[8]}  {lista[9]}  {lista[10]}  {lista[11]}|",
          f"\n|{lista[12]}  {lista[13]}  {lista[14]}  {lista[15]}|")
#F Exibir Grafico
def Grafico(t):
        if i == -1:
            for _ in range (0,3):
                plt.bar(f"{_+2}x{_+2}*",tt,fc = "royalblue", ec = "royalblue")
            for _ in range(0,8):
                plt.bar(f"{_+2}x{_+2}",t,fc = "navy", ec = "navy")
            plt.title('Tempo de execução Vs Tamanho da Matriz')
            plt.xlabel("Matrizes (* = Manual)")
            plt.ylabel("Tempo")
            plt.show() 
        else:
            for x in range(0,len(t)):
                plt.bar(f"{x+escolha}x{x+escolha}",t[x],fc = "darkslateblue", ec = "black")
            plt.title('Tempo de execução Vs Tamanho da Matriz')
            plt.xlabel("Matrizes")
            plt.ylabel("Tempo")
            plt.show() 
#F Matriz
def Matriz(lista):
    for _ in range(0,i):
       try:
           lista.append(input(f"Digito de número {_+1} da Matriz: "))
           lista = [float(_) for _ in lista]
       except ValueError:
           print("\nEu avisei que era apenas números!\n")  
           break
    return lista
#F Determinante
def Deter():
    print(f"\nO Determinante da sua matriz é: {resultado: 2.2f}")
    t2 = time.perf_counter_ns()
    t.append(t2 - t1) 
    print(f"\nO código demorou: \n{t[0]}ms") 
    return t
#Menu
print("\n1 - Matrizes 2x2 até 9x9 (Automatico com e sem Numpy)",
      "\n2 - Matriz 2x2 (Manual e sem Numpy)",
      "\n3 - Matriz 3x3 (Manual e sem Numpy)",
      "\n4 - Matriz 4x4 (Manual e sem Numpy)")
#Escolha
while i == 0:
    try:
        escolha = int(input("Escolha o tipo de matriz que iremos calcular: ")) 
#Escolha 2 - 2X2
        if escolha == 2 :
            print("\nVocê escolheu 2x2 \n(1  2)\n(3  4)")
            i = 4
            lista = Matriz(lista)
            X2()
            t1 = time.perf_counter_ns()
            resultado = Y2()
            t = Deter()
            Grafico(t)
#Escolha 3 - 3X3
        elif escolha == 3:
            print("\nVocê escolheu 3x3 \n(1  2  3)\n(4  5  6)\n(7  8  9)")
            i = 9
            lista = Matriz(lista)
            X3()
            t1 = time.perf_counter_ns()
            resultado = Y3()
            t = Deter()
            Grafico(t)
#Escolha 4 - 4X4
        elif escolha == 4:
            print("\nVocê escolheu 4x4 \n(1   2   3   4)\n(5   6   7   8)\n(9  10  11  12)\n(13 14  15  16)")
            i = 16
            lista = Matriz(lista)
            X4()
            t1 = time.perf_counter_ns()
            resultado = Y4()
            t = Deter()
            Grafico(t)
#Escolha 1 - Automatico -2x2 a 9x9)
        elif escolha == 1: 
            i = -1  
            for _ in range(0,16):
                lista.append(np.random.randint(1,9))        
            #2x2-4x4
            X2()
            t1 = time.perf_counter_ns()
            resultado = Y2()
            Finaliza(_ = 2)
            
            X3()
            t1 = time.perf_counter_ns()
            resultado = Y3()
            Finaliza(_ = 3)
            
            X4()
            t1 = time.perf_counter_ns()
            resultado = Y4()
            Finaliza(_ = 4)
            #2x2-9x9
            for _ in range(0,8):
                print(f"\n Matriz {_+2}x{_+2}: ")
                matrix = np.random.randint(-10,10,size=(_+2,_+2))
                print(matrix) 
                t1 = time.perf_counter_ns()
                print(f"\nO Determinante da sua matriz {_+2}x{_+2} é: {(np.linalg.det(matrix)): 2.2f}")   
                t2 = time.perf_counter_ns()
                t.append(t2 - t1)
            print(f"\nO código demorou:\nManual: {tt}ms\nAutomatico: {t}ms") 
            Grafico(t)
#Erro < 0 ou >= 5
        elif escolha <= 0 or escolha >= 5: 
            print("Apenas números entre 1 a 4!") 
            continue
#Erro Letras
    except ValueError:
            print("Apenas números inteiros!")
            continue