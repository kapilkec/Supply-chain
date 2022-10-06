from . import db

class erp15map(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    inOut=db.Column(db.String(20))
    Type = db.Column(db.String(10))
    Flag = db.Column(db.String(100))
    StockInQty=db.Column(db.String(10))
    ReExported=db.Column(db.String(10))
    ChangeUsage=db.Column(db.String(10))
    StockedOutFor=db.Column(db.String(10))
    otherPurpose=db.Column(db.String(10))
    def __init__(self,inOut,Type,Flag,StockInQty,ReExported,ChangeUsage,StockedOutFor,otherPurpose):
        self.inOut = inOut
        self.Type = Type
        self.Flag = Flag
        self.StockInQty = StockInQty
        self.ReExported = ReExported
        self.ChangeUsage = ChangeUsage
        self.StockedOutFor = StockedOutFor
        self.otherPurpose = otherPurpose


class erpecus(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    inOut=db.Column(db.String(20))
    Type = db.Column(db.String(10))
    Flag = db.Column(db.String(100))
    RequiredField=db.Column(db.String(10))
    EpeCode=db.Column(db.String(10))
    IfeCode=db.Column(db.String(10))
    FpCode=db.Column(db.String(10))
    def __init__(self,inOut,Type,Flag,RequiredField,EpeCode,IfeCode,FpCode):
        self.inOut = inOut
        self.Type = Type
        self.Flag = Flag
        self.RequiredField = RequiredField
        self.EpeCode =EpeCode
        self.IfeCode = IfeCode
        self.FpCode = FpCode
    
class erp15amap(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    inOut=db.Column(db.String(20))
    Type = db.Column(db.String(10))
    Flag = db.Column(db.String(100))
    StockInQty=db.Column(db.String(10))
    QtyOfProducts=db.Column(db.String(10))
    QtyOfExported=db.Column(db.String(10))
    otherPurpose=db.Column(db.String(10))
    def __init__(self,inOut,Type,Flag,StockInQty,QtyOfProducts,QtyOfExported ,otherPurpose):
        self.inOut = inOut
        self.Type = Type
        self.Flag = Flag
        self.StockInQty = StockInQty
        self.QtyOfProducts = QtyOfProducts
        self.QtyOfExported =QtyOfExported 
        self.otherPurpose = otherPurpose

