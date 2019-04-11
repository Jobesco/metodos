import mpmath
from sympy import *
x, y, z, t = symbols('x y z t')

def _euler(y0,t0,h,passos,funcao,escreve):
    y_ant = y0
    t_ant = t0
    y_n = 0
    for passo in range(passos+1):
        if passo == 0:
            if escreve: saida.write(str(passo) + ' ' + str(y0) + '\n')
        else:
            y_n = y_ant + funcao.evalf(subs={y: y_ant, t: t_ant})*h
            y_ant = y_n
            t_ant = passo*h
            if escreve: saida.write(str(passo) + ' ' + str(y_n) + '\n')
    return y_n

def euler_inverso(y0,t0,h,passos,funcao):
    y_ant = y0
    t_ant = t0
    for passo in range(passos+1):
        if passo == 0:
            saida.write(str(passo) + ' ' + str(y0) + '\n')
        else:
            y_n = y_ant + h*funcao.evalf(subs={t: t_ant + h, y: _euler(y_ant,t_ant,h,1,funcao,false)})
            y_ant = y_n
            t_ant = passo*h
            saida.write(str(passo) + ' ' + str(y_n) + '\n')

def euler_aprimorado(y0,t0,h,passos,funcao):
    y_ant = y0
    t_ant = t0
    for passo in range(passos+1):
        if passo == 0:
            saida.write(str(passo) + ' ' + str(y0) + '\n')
        else:
            y_n = y_ant + (funcao.evalf(subs={y: _euler(y_ant,t_ant,h,1,funcao,false), t: t_ant + h}) + funcao.evalf(subs={y: y_ant, t: t_ant}))*h/2
            y_ant = y_n
            t_ant = passo*h
            saida.write(str(passo) + ' ' + str(y_n) + '\n')

def runge_kutta(y0,t0,h,passos,funcao):
    y_ant = y0
    t_ant = t0
    for passo in range(passos+1):
        if passo == 0:
            saida.write(str(passo) + ' ' + str(y0) + '\n')
        else:
            k1 = funcao.evalf(subs={t: t_ant, y: y_ant})
            k2 = funcao.evalf(subs={t: t_ant + h/2, y: y_ant + h*k1/2})
            k3 = funcao.evalf(subs={t: t_ant + h/2, y: y_ant + h*k2/2})
            k4 = funcao.evalf(subs={t: t_ant + h, y: y_ant + h*k3})
            y_n = y_ant + (k1+2*k2+2*k3+k4)*h/6
            y_ant = y_n
            t_ant = passo*h
            saida.write(str(passo) + ' ' + str(y_n) + '\n')

def adam_bashforth(funcao,): #[1] = y(0) , [2] = t(0) , [3] = h , [4] = qtd de passos , [5] = funcao, [6] = ordem
    t_atual = float(linha[-5])
    t_inicial = float(linha[-5])
    h = float(linha[-4])
    saida.write('Metodo de Adam-Bashforth\ny( ' + linha[-5] + ' ) = ' + linha[1] + '\nh = ' + linha[-4] + '\n')
    if int(linha[-1]) == 2: lista_y = [float(linha[1]),float(linha[2])] #[0] = yn , [1] = yn-1...
    elif int(linha[-1]) == 3: lista_y = [float(linha[1]),float(linha[2]),float(linha[3])]
    elif int(linha[-1]) == 4: lista_y = [float(linha[1]),float(linha[2]),float(linha[3]),float(linha[4])]
    elif int(linha[-1]) == 5: lista_y = [float(linha[1]),float(linha[2]),float(linha[3]),float(linha[4]),float(linha[5])]
    elif int(linha[-1]) == 6: lista_y = [float(linha[1]),float(linha[2]),float(linha[3]),float(linha[4]),float(linha[5]),float(linha[6])]
    elif int(linha[-1]) == 7: lista_y = [float(linha[1]),float(linha[2]),float(linha[3]),float(linha[4]),float(linha[5]),float(linha[6]),float(linha[7])]
    elif int(linha[-1]) == 8: lista_y = [float(linha[1]),float(linha[2]),float(linha[3]),float(linha[4]),float(linha[5]),float(linha[6]),float(linha[7]),float(linha[8])]
    print(lista_y)
    for passo in range(int(linha[-3])+1):
        if passo == 0:
            saida.write(str(passo) + ' ' + str(lista_y[0]) + '\n')
        else:
            if int(linha[-1]) == 2: equacao = bashforth(lista_y[0],funcao,float(linha[-4]),t_atual,int(linha[-1]),lista_y[0],lista_y[1])
            elif int(linha[-1]) == 3: equacao = bashforth(lista_y[0],funcao,float(linha[-4]),t_atual,int(linha[-1]),lista_y[0],lista_y[1],lista_y[2])
            elif int(linha[-1]) == 4: equacao = bashforth(lista_y[0],funcao,float(linha[-4]),t_atual,int(linha[-1]),lista_y[0],lista_y[1],lista_y[2],lista_y[3])
            elif int(linha[-1]) == 5: equacao = bashforth(lista_y[0],funcao,float(linha[-4]),t_atual,int(linha[-1]),lista_y[0],lista_y[1],lista_y[2],lista_y[3],lista_y[4])
            elif int(linha[-1]) == 6: equacao = bashforth(lista_y[0],funcao,float(linha[-4]),t_atual,int(linha[-1]),lista_y[0],lista_y[1],lista_y[2],lista_y[3],lista_y[4],lista_y[5])
            elif int(linha[-1]) == 7: equacao = bashforth(lista_y[0],funcao,float(linha[-4]),t_atual,int(linha[-1]),lista_y[0],lista_y[1],lista_y[2],lista_y[3],lista_y[4],lista_y[5],lista_y[6])
            elif int(linha[-1]) == 8: equacao = bashforth(lista_y[0],funcao,float(linha[-4]),t_atual,int(linha[-1]),lista_y[0],lista_y[1],lista_y[2],lista_y[3],lista_y[4],lista_y[5],lista_y[6],lista_y[7])
            saida.write(str(passo) + ' ' + str(equacao) + '\n')
            lista_y.pop()
            lista_y.insert(0,equacao)
            t_atual = h*passo + t_inicial

            print(h)
            print(t_atual)
            

    
def bashforth(y0,funcao,h,t0,ordem, y1 = 0, y2 = 0, y3 = 0, y4 = 0, y5 = 0, y6 = 0, y7 = 0, y8 = 0):
    # print( (1901/720)*h*funcao.evalf(subs={t:t0,y:y1}) + (-1387/360)*h*funcao.evalf(subs={t:t0-h,y:y2}) 
    # + (109/30)*h*funcao.evalf(subs={t:t0-h*2,y:y3}) + (-637/360)*h*funcao.evalf(subs={t:t0-h*3,y:y4}) 
    # + (251/720)*h*funcao.evalf(subs={t:t0-h*4,y:y5}) )
    return (y0 + ordem_bashforth[ordem][0]*h*funcao.evalf(subs={t:t0,y:y1}) + ordem_bashforth[ordem][1]*h*funcao.evalf(subs={t:t0-h,y:y2}) 
    + ordem_bashforth[ordem][2]*h*funcao.evalf(subs={t:t0-h*2,y:y3}) + ordem_bashforth[ordem][3]*h*funcao.evalf(subs={t:t0-h*3,y:y4}) 
    + ordem_bashforth[ordem][4]*h*funcao.evalf(subs={t:t0-h*4,y:y5}) + ordem_bashforth[ordem][5]*h*funcao.evalf(subs={t:t0-h*5,y:y6}) 
    + ordem_bashforth[ordem][6]*h*funcao.evalf(subs={t:t0-h*6,y:y7}) + ordem_bashforth[ordem][7]*h*funcao.evalf(subs={t:t0-h*7,y:y8}))

def adam_moulton(funcao): #use bashforth p prever
    t_atual = float(linha[-5])
    saida.write('Metodo de Adam-Moulton\ny( ' + linha[-5] + ' ) = ' + linha[1] + '\nh = ' + linha[-4] + '\n')#[0] = yn , [1] = yn-1...
    if int(linha[-1]) == 2: lista_y = [float(linha[1]),float(linha[2])] 
    elif int(linha[-1]) == 3: lista_y = [float(linha[1]),float(linha[2]),float(linha[3])]
    elif int(linha[-1]) == 4: lista_y = [float(linha[1]),float(linha[2]),float(linha[3]),float(linha[4])]
    elif int(linha[-1]) == 5: lista_y = [float(linha[1]),float(linha[2]),float(linha[3]),float(linha[4]),float(linha[5])]
    elif int(linha[-1]) == 6: lista_y = [float(linha[1]),float(linha[2]),float(linha[3]),float(linha[4]),float(linha[5]),float(linha[6])]
    elif int(linha[-1]) == 7: lista_y = [float(linha[1]),float(linha[2]),float(linha[3]),float(linha[4]),float(linha[5]),float(linha[6]),float(linha[7])]
    elif int(linha[-1]) == 8: lista_y = [float(linha[1]),float(linha[2]),float(linha[3]),float(linha[4]),float(linha[5]),float(linha[6]),float(linha[7]),float(linha[8])]
    print(lista_y)

    for passo in range(int(linha[-3])+1):
        if passo == 0:
            saida.write(str(passo) + ' ' + str(lista_y[0]) + '\n')
        else:
            if int(linha[-1]) == 2:
                equacao = lista_y[0] + moulton(funcao,float(linha[-4]),t_atual,int(linha[-1]),lista_y[0]) + ordem_moulton[int(linha[-1])][1]*float(linha[-4])*funcao.evalf(subs={t: t_atual + float(linha[-4]) , y: bashforth(lista_y[0],funcao,float(linha[-4]),t_atual+float(linha[-4]),int(linha[-1]),lista_y[1],lista_y[2])})
            elif int(linha[-1]) == 3:
                equacao = lista_y[0] + moulton(funcao,float(linha[-4]),t_atual,int(linha[-1]),lista_y[0],lista_y[1]) + ordem_moulton[int(linha[-1])][2]*funcao.evalf(subs={t: t_atual+float(linha[-4]), y: bashforth(lista_y[0],funcao,float(linha[-4]),t_atual+float(linha[-4]),int(linha[-1]),lista_y[1],lista_y[2]),lista_y[3]})
            elif int(linha[-1]) == 4:
                equacao = lista_y[0] + moulton(funcao,float(linha[-4]),t_atual,int(linha[-1]),lista_y[0],lista_y[1],lista_y[2]) + ordem_moulton[int(linha[-1])][3]*(funcao.evalf(subs={t: t_atual+float(linha[-4]), y: bashforth(lista_y[0],funcao,float(linha[-4]),t_atual+float(linha[-4]),int(linha[-1]),lista_y[1],lista_y[2]),lista_y[3],lista_y[4]}))
            elif int(linha[-1]) == 5:
                equacao = lista_y[0] + moulton(funcao,float(linha[-4]),t_atual,int(linha[-1]),lista_y[0],lista_y[1],lista_y[2],lista_y[3]) + ordem_moulton[int(linha[-1])][4]*(funcao.evalf(subs={t: t_atual+float(linha[-4]), y: bashforth(lista_y[0],funcao,float(linha[-4]),t_atual+float(linha[-4]),int(linha[-1]),lista_y[1],lista_y[2]),lista_y[3],lista_y[4],lista_y[5]}))
            elif int(linha[-1]) == 6:
                equacao = lista_y[0] + moulton(funcao,float(linha[-4]),t_atual,int(linha[-1]),lista_y[0],lista_y[1],lista_y[2],lista_y[3],lista_y[4]) + ordem_moulton[int(linha[-1])][5]*(funcao.evalf(subs={t: t_atual+float(linha[-4]), y: bashforth(lista_y[0],funcao,float(linha[-4]),t_atual+float(linha[-4]),int(linha[-1]),lista_y[1],lista_y[2]),lista_y[3],lista_y[4],lista_y[5],lista_y[6]}))
            elif int(linha[-1]) == 7:
                equacao = lista_y[0] + moulton(funcao,float(linha[-4]),t_atual,int(linha[-1]),lista_y[0],lista_y[1],lista_y[2],lista_y[3],lista_y[4],lista_y[5]) + ordem_moulton[int(linha[-1])][6]*(funcao.evalf(subs={t: t_atual+float(linha[-4]), y: bashforth(lista_y[0],funcao,float(linha[-4]),t_atual+float(linha[-4]),int(linha[-1]),lista_y[1],lista_y[2]),lista_y[3],lista_y[4],lista_y[5],lista_y[6],lista_y[7]}))
            elif int(linha[-1]) == 8:
                equacao = lista_y[0] + moulton(funcao,float(linha[-4]),t_atual,int(linha[-1]),lista_y[0],lista_y[1],lista_y[2],lista_y[3],lista_y[4],lista_y[5],lista_y[6]) + ordem_moulton[int(linha[-1])][7]*(funcao.evalf(subs={t: t_atual+float(linha[-4]), y: bashforth(lista_y[0],funcao,float(linha[-4]),t_atual+float(linha[-4]),int(linha[-1]),lista_y[1],lista_y[2]),lista_y[3],lista_y[4],lista_y[5],lista_y[6],lista_y[7],lista_y[8]}))
            saida.write(str(passo) + ' ' + str(equacao) + '\n')
            lista_y.pop()
            lista_y.insert(0,equacao)
            t_atual += float(linha[-5])

def moulton(funcao,h,t0,ordem, y1 = 0, y2 = 0, y3 = 0, y4 = 0, y5 = 0, y6 = 0, y7 = 0, y8 = 0):
    return (ordem_moulton[ordem][0]*h*funcao.evalf(subs={t:t0,y:y1}) + ordem_moulton[ordem][1]*h*funcao.evalf(subs={t:t0-h,y:y2}) 
    + ordem_moulton[ordem][2]*h*funcao.evalf(subs={t:t0-h*2,y:y3}) + ordem_moulton[ordem][3]*h*funcao.evalf(subs={t:t0-h*3,y:y4}) 
    + ordem_moulton[ordem][4]*h*funcao.evalf(subs={t:t0-h*4,y:y5}) + ordem_moulton[ordem][5]*h*funcao.evalf(subs={t:t0-h*5,y:y6}) 
    + ordem_moulton[ordem][6]*h*funcao.evalf(subs={t:t0-h*6,y:y7}) + ordem_moulton[ordem][7]*h*funcao.evalf(subs={t:t0-h*7,y:y8}))

def formula_inversa():
    return 0


entrada = open('entrada.txt','r')
saida = open('saida.txt','w+')
ordem_bashforth = {
    2: [3/2,-1/2,0,0,0,0,0,0],
    3: [23/12,-4/3,5/12,0,0,0,0,0],
    4: [55/24,-59/24,37/24,-3/8,0,0,0,0],
    5: [1901/720,-1387/360,109/30,-637/360,251/720,0,0,0],
    6: [4277/1440,-2641/480,4991/720,-3649/720,959/480,-95/288,0,0],
    7: [198721/60480,-18637/2520,235183/20160,-10754/945,135713/20160,-5603/2520,19087/60480,0],
    8: [16083/4480,-1152169/120960,242653/13440,-296053/13440,2102243/120960,-115747/13440,32863/13440,-5257/17280]
}
ordem_moulton = {
    2: [1/2,1/2],
    3: [5/12,2/3,-1/12],
    4: [3/8,19/24,-5/24,1/24],
    5: [251/720,323/360,-11/30,53/360,-19/720],
    6: [95/288,1427/1440,-133/240,241/720,-173/1440,3/160],
    7: [19087/60480,2713/2520,-15487/20160,586/945,-6737/20160,263/2520,-863/60840],
    8: [5257/17280,139849/120960,-4511/4480,123133/120960,-88547/120960,1537/4480,-11351/120960,257/24192],
}
if entrada.mode == 'r':
    linhas_entrada = entrada.readlines()
for linha_toda in linhas_entrada:
    # fim = linha.index(' ')
    linha = linha_toda.split(' ')
    # print(linha)
    if linha[0] == 'euler': #[1] = y(0) , [2] = t(0) , [3] = h , [4] = qtd de passos , [5] = funcao
        saida.write('Metodo de Euler\ny( ' + linha[2] + ' ) = ' + linha[1] + '\nh = ' + linha[3] + '\n')
        _euler(float(linha[1]),float(linha[2]),float(linha[3]),int(linha[4]),sympify(linha[5]),true)
    
    elif linha[0] == 'euler_inverso':
        saida.write('Metodo de Euler Inverso\ny( ' + linha[2] + ' ) = ' + linha[1] + '\nh = ' + linha[3] + '\n')
        euler_inverso(float(linha[1]),float(linha[2]),float(linha[3]),int(linha[4]),sympify(linha[5]))
    
    elif linha[0] == 'euler_aprimorado':
        saida.write('Metodo de Euler Aprimorado\ny( ' + linha[2] + ' ) = ' + linha[1] + '\nh = ' + linha[3] + '\n')
        euler_aprimorado(float(linha[1]),float(linha[2]),float(linha[3]),int(linha[4]),sympify(linha[5]))
    
    elif linha[0] == 'runge_kutta':
        saida.write('Metodo de Runge-Kutta\ny( ' + linha[2] + ' ) = ' + linha[1] + '\nh = ' + linha[3] + '\n')
        runge_kutta(float(linha[1]),float(linha[2]),float(linha[3]),int(linha[4]),sympify(linha[5])) #4a ordem
    
    elif linha[0] == 'adam_bashforth': #[6] = ordem
        adam_bashforth(sympify(linha[-2]))
        
    # elif linha[0] == 'adam_moulton':

    # elif linha[0] == 'formula_inversa':