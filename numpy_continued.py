import numpy as np

x = 1.0
y = 2.0

#exponents and logarithms
print(np.exp(x))
print(np.log(x))
print(np.log10(x))
print(np.log2(x))

#main/max/misc
print(np.fabs(x))	#absolute val as a float
print(np.fmin(x,y))	#min of x and y
print(np.fmax(x,y))	#max of x and y

#populate arrays
n = 100								#define an int
z = np.arrange(n, dtype=float)		#get an array [0.0,n-1.]
z *= 2.0*np.pi /float(n-1)			#z = [0, 2*pi]
sin_z = np.sin(z)

#interpolation
print(np.interp(0.75,z,sin_z))		#interpolate sin(0.75)
print(np.sin(0.75))