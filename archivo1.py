import numpy as np
import pylab as pl
#Make an array for x values
x = [5000,6000,7000,8000,9000]
#Make an array of y values for each x value
y = [65,78,88,89,93]
#Use pylab to plot x and y 
pl.plot(x,y)

#Make an array for x values
x1 = [7000,8000,9000,10000,11000]
#Make an array of y values for each x value
y2 = [65,75,85,86,90]
#Use pylab to plot x and y
pl.plot(x1,y2)

pl.xlabel('Voltaje[V]')
pl.ylabel('Eficiencia[%]')
#Save fig as png
pl.savefig('archivo1.png')
