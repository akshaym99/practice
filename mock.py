class CC_Transaction:

    def __init__(self):
        self.tran_time={}

    def insert_tran(self, Tid):
        if Tid in self.tran_time:
            self.tran_time[Tid]=0
            return "DUPLICATE"
        self.tran_time[Tid]=0
        return "UNIQUE"
        
    def purge(self):
        for t in self.tran_time:
            d[t]+=1
            if d[t]==60:
                del d[t]
        return
