def main():
    frac=input("enter the fraction : ")
    try:

        x,y = frac.split("/")
        x = int(x)
        y = int(y)
        result=int((x/y)*100)
        if result<=1:
            print("E")
        elif result>=99:
            print("F")
        else:
            print(f"{result}%")
        break    
main()           

