def opt_meal():
    print("똥먹을까 방구먹을까")
    answer = input("똥/방구: ")
    while i == 0:
        if answer == "똥":
            return answer
        elif answer == "방구":
            return answer
        else:
            answer = input("똥이랑 방구중에 골라라 :")
            continue
        
def scn_meal():
    if answer == "똥":
        print("맛없어")
        return 0
    elif answer == "방구":
        print("냄새나")
        return 0

i = 0
while i == 0:
    answer = opt_meal()
    scn_meal()
    print("다른것도 먹어볼래?")
    answer = input("네/아니오 :")
    if answer == "네":
        continue
    else:
        break
    
    
