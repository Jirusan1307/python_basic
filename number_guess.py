import random
number = random.randint(0,10)
T=None
cout=0

while T != number:
    T=int(input("number this right"))
    cout+=1
    if T>number:
        print("มากกว่า")
    elif T<number:
        print("น้อยกว่า")
    else:
        print(f"right! เดาไปทั้งหมด {cout} ครั้ง")

