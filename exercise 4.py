math = int(input("math: "))
eng = int(input("eng: "))
kisw = int(input("kisw: "))
chem = int(input("chem: "))
geo = int(input("geo: "))
sum = math + eng + kisw + chem + geo
average = sum/5

if 0 <= average <= 39:
    print("E")
elif 40 <= average <= 50:
    print("D")
elif 51 <= average <= 60:
    print("C")
elif 61 <= average <= 70:
    print("B")
elif 71 <= average <= 100:
    print("A")
else:
    print("invalid")


