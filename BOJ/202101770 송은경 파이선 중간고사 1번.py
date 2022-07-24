kg=float(input("체중>"))
cm=float(input("신장>"))


def bmif(kk,cc):
    
    bmi= kg /((cm * 0.01)**2)
    print("BMI = ", bmi)
    
    if bmi < 18.5:
    
        print("마른 체형입니다.")
        

    elif 18.5<= bmi < 25.0:
    
        print("표준 체형입니다.")
        

    elif 25.0 <= bmi < 30.0:
    
        print("비만 입니다.")
        x= kg-25*((cm*0.01)**2)
    
        print(x,"kg를 초과해 감량해야 표준체형입니다.")

    
    elif bmi >=30.0:
    
        print("고도 비만입니다.")
        n=kg-25*((cm*0.01)**2)
    
        print(n,"kg를 초과해 감량해야 표준체형입니다.")


bmif(kg,cm)
