class mat2by2:
    def __init__(self,a11=0, a12=0, a21=0, a22=0):
        self.setA11(a11)
        self.setA12(a12)
        self.setA21(a21)
        self.setA22(a22)
        return
    def setA11(self,d):
        self.__a11=d
        return
    def setA12(self,d):
        self.__a12=d
        return
    def setA21(self,d):
        self.__a21=d
        return
    def setA22(self,d):
        self.__a22=d
        return
    def getA11(self):
        return self.__a11
    def getA12(self):
        return self.__a12
    def getA21(self):
        return self.__a21
    def getA22(self):
        return self.__a22
    def __str__(self):
        return "(" + str(self.getA11()) + "," + str(self.getA12()) + "," + str(self.getA21())+ ","  +str(self.getA22()) + ")"
    def __add__(lhs, rhs):
        v = mat2by2()
        v.setA11(lhs.getA11() + rhs.getA11())
        v.setA12(lhs.getA12() + rhs.getA12())
        v.setA21(lhs.getA21() + rhs.getA21())
        v.setA22(lhs.getA22() + rhs.getA22())
        return v

    @staticmethod
    def subtract(lhs, rhs):
        v = mat2by2()
        v.setA11(lhs.getA11() - rhs.getA11())
        v.setA12(lhs.getA12() - rhs.getA12())
        v.setA21(lhs.getA21() - rhs.getA21())
        v.setA22(lhs.getA22() - rhs.getA22())
        return v

    @staticmethod
    def scalar_multiplication(lhs,s):
        v = mat2by2()
        v.setA11(lhs.getA11() * s)
        v.setA12(lhs.getA12() * s)
        v.setA21(lhs.getA21() * s)
        v.setA22(lhs.getA22() * s)
        return v
    def transpose(a):
        v = mat2by2()
        v.setA11(a.getA11())
        v.setA12(a.getA21())
        v.setA21(a.getA12())
        v.setA22(a.getA22())
        return v
    @staticmethod
    def determinant(m):
        v=(m.getA11()*m.getA22())-(m.getA12()*m.getA21())
        return v
    def singular(m):
        v = (m.getA11() * m.getA22()) - (m.getA12() * m.getA21())
        if v==0:
            return 'Matrix is singular'
        else:
            return 'Matrix is not singular'

    def inverse(m):
        det= mat2by2.determinant(m)
        v = mat2by2()
        v.setA11(m.getA11() * det)
        v.setA12(m.getA12() * det)
        v.setA21(m.getA21() * det)
        v.setA22(m.getA22() * det)
        return v

    def cofactor(m):
        v=mat2by2()
        v.setA11(m.getA22() * (-1)**2)
        v.setA12(m.getA21() * (-1)**3)
        v.setA21(m.getA12() * (-1)**3)
        v.setA22(m.getA11() * (-1)**4)
        return v

    def null(m):
        if m.getA11()==m.getA12()==m.getA21()==m.getA22()==0:
            return 'Matrix is Null Matrix.'
        return 'Matrix is not Null Matrix.'

    def identity(m):
        if m.getA21()==m.getA12()==0 and m.getA11()==m.getA22()==1:
            return 'Matrix is identity matrix.'
        return 'Matrix is not identity matrix'
    @staticmethod
    def multiply(lhs, rhs):
        x = mat2by2()
        x.setA11((lhs.getA11()*rhs.getA11())+(lhs.getA12()*rhs.getA21()))
        x.setA12((lhs.getA11() * rhs.getA12()) + (lhs.getA12() * rhs.getA22()))
        x.setA21((lhs.getA21() * rhs.getA11()) + (lhs.getA22() * rhs.getA21()))
        x.setA22((lhs.getA21() * rhs.getA12()) + (lhs.getA22() * rhs.getA22()))
        return x

    def division(a,b):
        m2 = mat2by2.inverse(b)
        m = mat2by2.multiply(a, m2)
        return m

def main():
    m1=mat2by2(2,1,5,2)
    m2=mat2by2(3,4,5,6)
    print('m1'+ str(m1))
    print('m2' + str(m2))
    print("ADD=M1+M2: " + str(m1 + m2))
    print("SUBTRACT=M1-M2: " + str(mat2by2.subtract(m1, m2)))
    print("SCALAR_MULTIPLICATION: " + str(mat2by2.scalar_multiplication(m1,4)))
    print('TRANSPOSE OF M1:' + str(m1.transpose()))
    print('DIVISION OF M1 AND M2:', mat2by2.division(m1, m2))
    print('DETERMINANT OF M1:'+str(mat2by2.determinant(m1)))
    print('M1 ',m1.singular())
    print('INVERSE OF M1:', m1.inverse())
    print('COFACTOR OF M1:',m1.cofactor())
    print('M1 ',m1.null())
    print('M1 ',m1.identity())
    print('MULTIPLICATION OF M1 AND M2:', mat2by2.multiply(m1,m2))

main()






