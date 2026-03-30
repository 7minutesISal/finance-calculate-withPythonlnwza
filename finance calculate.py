calculate = ["PV","FV","PMT","I","N","IRR","NPV"]
labels = ["มูลค่า :","I อัตราดอกเบี้ย :","N จน.ปี :"]
Cal_I = ["จากPV,FV","จากPMT"]
choicePMT = ["PMTหาFV(ฝากท้ายปี)","PMTหาFV(ฝากต้นปี)","PMTหาPV(ฝากท้ายปี)","PMTหาPV(ฝากต้นปี)","FVหาPMT","PVหาPMT"]
test = ["test"]
dataprint = ["\n----- กำลังคำนวณ -----"]
AllPMT = ["PMT","PMT","FV","PV"]
datacalculate = []
FVforNPV = []
cash_flows = []
WhatY = []
datacalculate.clear()

def PVfind_PMT(PV,I,N):
    K = I/100
    down = (1+K)**N
    findPMT = PV*(K / (1 - ((1+K)**-N)))
    return findPMT

def PMT_PVfirst(PMT,I,N):
    K = I/100
    down = (1+K)**N
    PMT_PVfi = PMT*(((1-(1 / down)) / K)*(1+K))
    return PMT_PVfi
def PMT_PVlast(PMT,I,N):
    K = I/100
    down = (1+K)**N
    PMT_PVla = PMT*((1-(1 / down)) / K)
    return PMT_PVla
def PMT_FVfirst(PMT,I,N):
    PMT_FVfi = (PMT*((((1+(I/100))**N) - 1) / (I/100)))*(1+I/100)
    return PMT_FVfi
    
def inputdata():
    while True:
        try:
            invest = int(input("ปีที่0ลงทุนเท่าไหร่(ติดลบ):"))
            Y = int(input("กี่ปี:"))
            break
        except ValueError:
            print("ใส่แค่เลขโว้ย")
    NPV_1 = []
    for i in range(Y):
        NPV_1.append(float(input(f"ปีที่{i+1}.เท่ากับ:")))
    return invest,NPV_1
def NPV():
    FVforNPV.clear()
    while True:
        try:
            invest = int(input("ปีที่0ลงทุนเท่าไหร่:"))
            Y = int(input("กี่ปี:"))
            break
        except ValueError:
            print("ใส่แค่เลขโว้ย")
    Ydata = int(Y)
    for i in range(Ydata):
        NPV_1 = float(input(f"ปีที่{i+1}.เท่ากับ:"))
        FVforNPV.append(NPV_1)
    while True:
        try:
            DataI = float(input("อัตราดอกเบี้ย:"))
            I = int(DataI)
            break
        except ValueError:
            print("ใส่แค่เลขโว้ย")
    print("ข้อมูลที่กรอก",FVforNPV)
    totalPV = 0
    for i in range(len(FVforNPV)):
        PVreal = calculatePV(FVforNPV[i],I,i+1)
        totalPV = totalPV + PVreal
        print(f"PV ปีที่{i+1}เท่ากับ {PVreal:.2f}")
    print(f"NPV รวมเท่ากับ: {totalPV:.2f}")
    return totalPV,PVreal,invest
def printcalculatedata(dataprint,datacalculate):
    print(dataprint[0])
    print(f"ได้เท่ากับ :{datacalculate[0]:.2f}")
def calculatePV(FV,I,N):
    PV = FV * (1 / (1+(I/100))**N)
    return PV

def calculateFV(PV,I,N):
    FV = PV * (1 + (I/100))** N
    return FV

def calculatePMTfindFVlast(PMT,I,N):
    PMTfindFV = PMT*((((1+(I/100))**N) - 1) / (I/100) )
    return PMTfindFV
import math

def calculatelastFVfindPMT(FV,I ,N):
    rate = I / 100
    FVfindPMT = FV * (rate / ((1+rate)**N - 1))
    return FVfindPMT

def calculateN(PV,FV,I):
    if PV <= 0 or FV <= 0:
        print("หาค่าไม่ได้")
        return 0.0
    rate = I / 100
    n = math.log(FV/PV) / math.log(1 + rate)
    return n

def calculateIforFVPV(PV,FV,N):
    I = ((FV/PV)**(1 / N)) - 1
    I = I * 100
    return I

def calculateIforPMT(PMT,FV,N) :
    if FV == PMT * N :
        return 0.0
    low = 0.00001
    high = 1.0
    for i in range(100):
        rateI = (low + high) / 2
        calculatefinal = calculatelastFVfindPMT(FV,rateI * 100,N)
        if calculatefinal > PMT:
            low = rateI
        else:
            high = rateI
    return rateI * 100

def get_input(labels):
    values = []
    for label in labels:
        while True:
            try:
                val = float(input(f"{label}"))
                values.append(val)
                break
            except ValueError:
                print("ใส่ตัวเลขโว้ย")
    return values

PMT_Howcal = [calculatePMTfindFVlast,
              PMT_FVfirst,
              PMT_PVlast,
              PMT_PVfirst,
              calculatelastFVfindPMT,
              PVfind_PMT]
for i in range(7) :
    print(i+1,".",f"{calculate[i]}")
while True:
    try:
        choice = int(input("ต้องการหาอะไร: ")) - 1
        if -1 <= choice <= 7 :
            print()
            break
        else:
            print("ไม่มีเว้ย")
    except ValueError:
        print("ใส่แค่เลขที่มีสิวะะ")
        
choicecalculate = calculate[choice]
print(f"คุณเลือก:{choicecalculate}")

        
if choice == 0 :
    values = []
    print("ใส่ข้อมูล")

    for label in labels :
        while True :
            try:
                val = float(input(f"{label}"))
                values.append(val)
                break
            except (ValueError, ZeroDivisionError):
                print("ใส่แค่เลขโว้ย")
    FV, I, N = values
    datacalculate.clear()
    datacalculate.append(calculatePV(FV,I,N))
    printcalculatedata(dataprint,datacalculate)
if choice == 1 :
    PV, I, N = get_input(["PVมูลค่า :","I อัตราดอกเบี้ย :","N จน.ปี :"])
    datacalculate.append(calculateFV(PV,I,N))
    printcalculatedata(dataprint,datacalculate)
elif choice == 2 :
    for i in range(6):
        print(i+1,".",f"{choicePMT[i]}")
    while True:
        try:
            CalPMT = int(input("คุณต้องการหาจากอะไร :")) - 1
            if -1 < CalPMT < 6 :
                break
            else:
                print("ไม่มี")
        except ValueError:
            print("ใส่แค่เลข")
    if CalPMT == 0:
        while True:
            PMT, I, N = get_input(["PMTมูลค่า :","I อัตราดอกเบี้ย :","N จน.ปี :"])
            if N > 0 or N < 0 :
                break
            print("ใส่ 0 ไม่ได้มันหาไม่ได่้")
        datacalculate.append(calculatePMTfindFVlast(PMT,I,N))
        printcalculatedata(dataprint,datacalculate)
    if CalPMT == 1:
        while True:
            PMT, I, N = get_input(["PMTมูลค่า :","I อัตราดอกเบี้ย :","N จน.ปี :"])
            if N > 0 or N < 0 :
                break
            print("ใส่ 0 ไม่ได้มันหาไม่ได่้")
        datacalculate.append(PMT_Howcal[1](PMT,I,N))
        printcalculatedata(dataprint,datacalculate)
    if CalPMT == 2:
        while True:
            PMT, I, N = get_input(["PMTมูลค่า :","I อัตราดอกเบี้ย :","N จน.ปี :"])
            if N > 0 or N < 0 :
                break
        datacalculate.append(PMT_Howcal[2](PMT,I,N))
        printcalculatedata(dataprint,datacalculate)
    if CalPMT == 3:
        while True:
            PMT, I, N = get_input(["PMTมูลค่า :","I อัตราดอกเบี้ย :","N จน.ปี :"])
            if N > 0 or N < 0 :
                break
        datacalculate.append(PMT_Howcal[3](PMT,I,N))
        printcalculatedata(dataprint,datacalculate)
    if CalPMT == 4:
        while True:
            FV, I, N = get_input(["FVมูลค่า :","I อัตราดอกเบี้ย :","N จน.ปี :"])
            if N > 0 or N < 0 :
                break
        datacalculate.append(PMT_Howcal[4](FV,I,N))
        printcalculatedata(dataprint,datacalculate)
    if CalPMT == 5:
        while True:
            PV, I, N = get_input(["PVมูลค่า :","I อัตราดอกเบี้ย :","N จน.ปี :"])
            if N > 0 or N < 0 :
                break
        datacalculate.append(PMT_Howcal[5](PV,I,N))
        printcalculatedata(dataprint,datacalculate)
elif choice == 3:
    for i in range(2):
        print(i+1,".",f"{Cal_I[i]} :")
    while True:
        try:
            CalI = int(input("คุณต้องการหาจากอะไร :")) - 1
            if -1 < CalI < 2 :
                break
            else:
                print("ไม่มี")
        except ValueError:
            print("ใส่แค่เลข")
    if CalI == 0:
        while True:
            PV, FV, N = get_input(["มูลค่าปัจจุบัน :","มูลค่าอนาคต :","N จน.ป :"])
            if N > 0 or N < 0:
                break
            print("ใส่ 0 ไม่ได้มันหาไม่ได่้")
        datacalculate.append(calculateIforFVPV(PV,FV,N))
        printcalculatedata(dataprint,datacalculate)
    elif CalI == 1:
        while True:
            PMT, FV, N = get_input(["PMT :","FVมูลค่าอนาคต :","N จน.ป :"])
            if N > 0 or N < 0:
                break
            print("ใส่ 0 ไม่ได้มันหาไม่ได่้") 
        datacalculate.append(calculateIforPMT(PMT,FV,N))
        printcalculatedata(dataprint,datacalculate)    
elif choice == 4 :
    while True:
        PV, FV, I = get_input(["มูลค่าปัจจุบัน :","มูลค่าอนาคต :","I อัตราดอกเบี้ยี :"])
        if I > 0 or I < 0:
            break
        print("ใส่ 0 ไม่ได้")
    datacalculate.append(calculateN(PV,FV,I))
    printcalculatedata(dataprint,datacalculate)
elif choice == 5 :
    invest,NPV_1 = inputdata()
    low = 0.00001
    high = 1.00
    for t in range(100):
        totalPV = invest
        I = (low + high) / 2
        for i in range(len(NPV_1)):
                PVreal = calculatePV(NPV_1[i],I*100,i+1)
                totalPV = totalPV + PVreal
        if totalPV > 0:
            low = I
        else:
            high = I
    print(f"ได้เท่ากับ{I*100:.2f}")
elif choice == 6 :
    FVforNPV.clear()
    NPV()
    
