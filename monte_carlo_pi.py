import random

def generate_xy():
    square=circle=0
    for i in xrange(100000):
        x=random.random()
        y=random.random()
        square=square+1
        k=x*x+y*y
        if k<1:
            circle=circle+1

    pi=4*(float(circle)/float(square))
    print "value of PI:",pi

if __name__=="__main__":
    generate_xy()

