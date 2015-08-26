#encoding=utf-8

class C(object):
    def __init__(self, a, b=1):
        self.a = a;
        self.b = b;

    def p(self):
        print self.a
        print self.b

c1 = C(1,2);
c1.p()
c1 = C(1);
c1.p()
