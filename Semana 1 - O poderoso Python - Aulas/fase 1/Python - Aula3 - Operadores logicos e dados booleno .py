#dados boleano e operadores logicos 
var_verdadeiro = True
var_falsa = False

if var_verdadeiro == True:
    print("var_verdadeiro é verdade")
if var_falsa == False:
    print("var_falsa é falso")
    
#quadrante no plano cartesiano
x, y = map(float, input().split())

if x > 0 and y > 0:
    print ('primeiro')
elif x < 0 and y > 0:
    print ('segundo')
elif x < 0 and y < 0:
    print ('terceiro')
elif x > 0 and y < 0:
    print ('quarto')
elif x <0 and y ==0 :
    print('eixo x')
elif x >0 and y ==0 :
    print('eixo x')
elif x==0 and y >0 :
    print ('eixo y')
elif x==0 and y <0 :
    print ('eixo y')
elif x==0 and y ==0 :
    print ('origem')

