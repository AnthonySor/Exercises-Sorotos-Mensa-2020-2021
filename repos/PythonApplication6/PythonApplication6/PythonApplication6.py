class train:
    startstation = ''
    finishstation = ''
    voyageduration =0.0
    totalcapacity =1000
    seatcapacity =500
    bedcapacity =300
    currentcapacity =0.0
    cbedcapacity =0.0
    cseatcapacity =0.0

    def __init__(self,start,finish,stt,vd,tc,bc,sc):
        self.startstation = start
        self.finishstation = finish
        self.voyageduration = vd
        self.totalcapacity = tc
        self.seatcapacity = sc
        self.bedcapacity = bc

    def embark (self,seatpass,bedpass):
        tempcapacity = self.currentcapacity + seatpass + bedpass
        if tempcapacity > self.totalcapacity:
            raise Exception("Overpopulation")
        self.cseatcapacity += seatpass
        self.cbedcapacity += bedpass
    except:
        print()
    

    def disembark (self,seatpass,bedpass):
        self.currentcapacity = self.currentcapacity - seatpass - bedpass
        self.cseatcapacity -= seatpass
        self.cbedcapacity -= bedpass
