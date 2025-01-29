import random
'''sanke for 1
    water for -1
    gun for 0 '''
com=random.choice([1,-1,0])
youdict={"sanke":1, "water":-1, "gun":0}
revdict={1:"sanke", -1:"water", 0:"gun"}
you =input("Enter your choise :")
youch = youdict[you]
print(f"You chose {revdict[youch]}\nComputer chose {revdict[com]}")
if com==youch:
    print("Its a draw")
else:
    if com==1 and youch==-1 :
        print("You loose.")
    elif com==1 and youch==0:
        print("You win.")
    elif com==-1 and youch==1:
        print("You win.")
    elif com==-1 and youch==0:
        print("You loose.")
    elif com==0 and youch==1:
        print("You loose.")
    elif com==0 and youch==-1:
        print("You win.")
    else:
        print("Something went worng.")