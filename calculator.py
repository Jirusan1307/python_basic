data1 = int (input("number "))
data2 = int (input("number "))

Q = int (input ("""1 = +
2 = -
3 = x
4 = /
chose """))
match Q:
    case 1 :
        print(data1,"+",data2," = ",data1+data2)
    case 2 :
        print(data1,"-",data2," = ",data1-data2) 
    case 3 :
        print(data1,"x",data2," = ",data1*data2)
    case 4 :
        print(data1,"/",data2," = ",data1/data2)   

