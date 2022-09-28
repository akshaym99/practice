'''
------------------------ Problem 1 Start ---------------------------
Input:
- Credit card transactions data with possible duplicates
- System is getting one transaction record at a time, unordered
- TransactionID, TransactionTime, <other transactional information>

Output:
- Print whether UNIQUE or DUPLICATE record.

Purge policy:
- To reduce memory requirements, you need to purge data older than 1 hour.
- The purge function would be invoked once a  minute.
- Purge is based on transactionTime

Guidelines:
- For simplicity, use in-memory data structures to solve this problem, no need to use external system 
- Use programming language and editor of your choice
- You can browse the web if you need any help

------------------------ Problem 1 End ---------------------------
'''

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
