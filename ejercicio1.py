







 



def  calcularsueldo(salario, diastrabajados):
    sueldopagar=salario/30* diastrabajados
    return sueldopagar 

    
def main():
    SALARIO_MIN=1000000
    SUB_ALIM=1200000
    SUB_TRANSP=80000
    BONO=50000
    nombre = input ("digite su nombre ==>") 
    salario= int (input ("digite su salario ==>"))
    diastrabajados= int (input ("digite los dias trabajados ==> "))
    sueldopagar = calcularsueldo(salario, diastrabajados)
   
    
    if salario < (SALARIO_MIN * 2):
        sueldopagar= sueldopagar+SUB_ALIM+SUB_TRANSP
    else:
         sueldopagar = sueldopagar + BONO
     print(f"Mi nombre es: {nombre}y mi sueldo a pagar  es:{sueldopagar:.0f}")

if __name__=="__main__":
    main()
