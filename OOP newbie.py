
MYlist = []
class calculateFun :
    def __init__(self,FV=0,PV=0,PMT=0,I=0,N=0):
        self.fv = FV
        self.pv = PV
        self.pmt = PMT
        self.i = I/100
        self.n = N

    def calculatePV(self):
        pv = self.fv * (1 / ((1 + self.i) ** self.n))
        return pv

    def calculateFV(self):
        fv = self.pv * ((1+self.i)**self.n)
        return fv

class taxcalculate:
    def calculate_tax(self,datavalue):
        return datavalue * 0.07

tax = taxcalculate()
calculate = calculateFun(FV=1000,I=5,N=4,PMT=2500,PV=500)
data = calculate.calculateFV()
MYlist.append(data)
data = calculate.calculatePV()
MYlist.append(data)
for i in range(len(MYlist)):
    print(f"ได้เท่ากับ{MYlist[i]:.2f}")
print(f"หลังคำนวณภาษีFVเท่ากับ: {tax.calculate_tax(calculate.calculateFV()):.2f}")