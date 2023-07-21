num1 = input("x:")
num2 = input("y:")
X0 = float(input("X0:"))
x = num1.split( )
y = num2.split( )
i = 0
j = 0
k = 0
l = 0
m = 0
sumx = 0
sumy = 0
sumx2 = 0
sumy2 = 0
sumxy = 0 
while i < len(x) :
    sumx += int(x[i])
    i += 1
while j < len(y) :
    sumy += int(y[j])
    j += 1
while k < len(x) :
    sumx2 += int(x[k])**2
    k +=1
while l < len(y) :
    sumy2 += int(y[l])**2
    l +=1
while m < len(x) :
    sumxy += int(x[m])*int(y[m])
    m +=1
n = len(x)
xbar = sumx/len(x)
yber = sumy/len(y)
Sxx = sumx2 - sumx**2/len(x)
Syy = sumy2 - sumy**2/len(y)
Sxy = sumxy - (sumx*sumy)/len(x)
b1 = Sxy/Sxx
b0 = yber-(b1*xbar)
SyIx = ((Syy-(b1*Sxy))/(n-2))**(1/2)
S2yIx = SyIx**2
Sb0 = SyIx* ((1/n)+((xbar**2)/Sxx))**0.5
Sb1 = SyIx/ (Sxx**0.5)
T1 = (b1-0)/Sb1
T0 = (b0-0)/Sb0
SSR =b1*Sxy
SST = Syy
SSE = SST-SSR 
MSR = SSR 
MSE = SSE/(n-2)
F = MSR/MSE
Sy้ = SyIx*((1/n)+(((X0-xbar)**2)/Sxx))**0.5
r = Sxy/(Sxx*Syy)**0.5
Y0 = b0+(b1*X0)
Tend = r*((n-2)/(1-(r)**2))**0.5
print("sum x =",sumx)
print("sum y =",sumy)
print("Xbar =",xbar)
print("Ybar =",yber)
print("sum x**2 =", sumx2)
print("sum y**2 =", sumy2)
print("sum xy =", sumxy)
print("Sxx =", '%.3f'%Sxx) 
print("Syy =", '%.3f'%Syy)
print("Sxy =", '%.3f'%Sxy)
print("b1 =", '%.4f'%b1 )
print("b0 =", '%.4f'%b0)
print("Ans: y^ = bo + b1 คือ ","y^ =",'%.4f'%b0,"+",'%.4f'%b1,"x")
print("ค่า Y^0",'%.3f'%Y0)
print("________________________________________________________")
print("ค่าความคลาดเคลื่อนมาตรฐานของการประมาณ Sy|x =",'%.3f'%SyIx)
print("ค่าประมาณของความเเปรปรวนของความคลาดเคลื่อน S^2y|x =",'%.3f'%S2yIx)
print("________________________________________________________")
print("Sb0 ใช้ในการหาช่วงของค่าพารามิเตอร์ B0")
print("Sb0 =",'%.3f'%Sb0)
print("Sb1 ใช้ในการหาช่วงของค่าพารามิเตอร์ B1")
print("Sb1 =",'%.3f'%Sb1 )
print("________________________________________________________")
print("สถิติทดสอบทีของB0: t =",'%.3f'%T0)
print("สถิติทดสอบทีของB1: t =",'%.3f'%T1)
print("________________________________________________________")
print("สถิติทดสอบ F")
print("SSR =",'%.3f'%SSR)
print("SSE =",'%.3f'%SSE)
print("SST =",'%.3f'%SST)
print("MSR =",'%.3f'%MSR)
print("MSE =",'%.3f'%MSE)
print("F =" ,'%.3f'%F)
print("________________________________________________________")
print("ใช้ประมาณช่วงความเชื่อมั่นของตามเเปรตาม y")
print("Sy้ =",'%.3f'%Sy้)
print("________________________________________________________")
print("การวิเคราห์สหสัมพัน p=r")
print("r =",'%.3f'%r)
print("________________________________________________________")
print("การทดสอบสมมติฐาน ค่าสหสัมพัน")
print("t =",'%.3f'%Tend)