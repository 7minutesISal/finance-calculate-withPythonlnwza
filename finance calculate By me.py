
NPV_Data = []


def c_FV(PV,I,N) :
    K = I/100
    FV = PV * ((1+K)**N)
    return FV

def c_PV(FV,I,N) :
    K = I/100
    PV = FV * (1 / ((1+K)**N))
    return PV

def findFVlastbyPMT(PMT,I,N):
    K = I/100
    FVAl = PMT * ((((1+K)**N) - 1) / K)
    return FVAl
def findFVfirstbyPMT(PMT,I,N):
    K = I/100
    FVAf = PMT * (((((1+K)**N) - 1) / K) * (1+K))
    return FVAf
def findPVlastbyPMT(PMT,I,N):
    K  = I/100
    PVAl = PMT * ((1 - (1 / ((1+K)**N))) / K)
    return PVAl
def findPVfirstbyPMT(PMT,I,N):
    K = I/100
    PVAf = PMT * (((1 - (1 / ((1+K)**N))) / K) * (1+K))
    return PVAf
def findPMTbyPV(PV,I,N):
    K = I/100 #เขียนดัก 0 ด้วย
    PMT = PV * (K / (1 - ((1+K)**-N)))
    return PMT
def findPMTbyFV(FV,I,N):
    K = I/100
    PMT = FV * (K / (((1+K)**N) - 1))
    return PMT

import math
def NbyFVPV(FV,PV,I):
    if PV == 0:
        NOdata = print("อย่าใส่ 0")
        return NOdata
    K = I/100
    N = (math.log(FV/PV))/(math.log(1+K))
    return N
def NbyPMTandFV(PMT,FV,I):
    if PMT == 0:
        NOdata = print("อย่าใส่ 0")
        return NOdata
    K = I/100
    N = (math.log(((FV*K)/PMT)+1))/(math.log(1+K))
    return N
def NbyPMTandPV(PMT,PV,I):
    K = I/100
    top = (math.log(1 - ((PV*K)/PMT)))
    down = (math.log(1+K))
    N = -top / down
    return N


def IbyFVPV(FV,PV,N):
    I = ((FV/PV)**(1/N))-1
    return I
def IbyPMTandFV_end(PMT,FV,N):
    low = 0.0001
    high = 1.00
    for i in range(100):
        I = (low + high) / 2
        if I == 0:
            continue
        guess = PMT * ((((1+I)**N) - 1) / I)
        if guess > FV:
            high = I
        else:
            low = I
    I = I * 100
    return I
def IbyPMTandFV_AnnuityDue(PMT,FV,N):
    low = 0.0001
    high = 1.00
    for i in range(100):
        I = (low + high) / 2
        if I == 0:
            continue
        guess = PMT * (((((1+I)**N) - 1) / I) * (1+I))
        if guess > FV:
            high = I
        else:
            low = I
    I = I * 100
    return I
def IbyPMTandPV_end(PMT,PV,N):
    low = 0.0001
    high = 1.00
    for i in range(100):
        I = (low + high) / 2
        if I == 0:
            continue
        guess = PMT * ((1 - (1 / ((1+I)**N))) / I)
        if guess > PV:
            high = I
        else:
            low = I
    I = I * 100
    return I
def IbyPMTandPV_AnnuityDue(PMT,PV,N):
    low = 0.0001
    high = 1.00
    for i in range(100):
        I = (low + high) / 2
        if I == 0:
            continue
        guess = PMT * (((1 - (1 / ((1+I)**N))) / I) * (1+I))
        if guess > PV:
            high = I
        else:
            low = I
    I = I * 100
    return I

def NPV(NPV_Data,invest,I):
    K = I/100
    totalNPV = 0
    NPVcalculatereally = []
    NPVcalculatereally.clear()
    for i in range(len(NPV_Data)):
        PV = NPV_Data[i] * (1 / (1+K)**(i+1))
        NPVcalculatereally.append(PV)
        print(f"เท่ากับ{NPVcalculatereally[i]}")
        totalNPV = totalNPV + PV
    totalNPV = totalNPV - invest
    return totalNPV

def IRR(NPV_Data,invest,I):
    low = 0.0001
    high = 1.00
    for i in range(100):
        totalinvest = invest
        I = (low + high) / 2
        for t in range(len(NPV_Data)):
            guess = c_PV(NPV_Data[t],I,t+1)
            totalinvest = totalinvest + guess
        if totalinvest > 0:
            high = I
        else:
            low = I
    return I * 100

HowcalculateFVPV = [c_FV,c_PV]
HowcalculatePMT = [findFVfirstbyPMT,findFVlastbyPMT,findPVfirstbyPMT,findPVlastbyPMT,findPMTbyFV,findPMTbyPV]
HowcalculateN = [NbyFVPV,NbyPMTandFV,NbyPMTandPV]
HowcalculateI = [IbyFVPV,IbyPMTandFV_AnnuityDue,IbyPMTandFV_end,IbyPMTandPV_AnnuityDue,IbyPMTandPV_end]
HowcalculateNPV_IRR = [NPV,IRR]