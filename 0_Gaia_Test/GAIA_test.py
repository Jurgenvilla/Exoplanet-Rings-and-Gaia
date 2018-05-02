#import numpy as np
from astropy.table import Table 
#from astropy import constants as const 
import matplotlib.pyplot as plt

DATA = Table.read('DR1_Mag_color.csv', format = 'csv', fast_reader = True)

Mag_G = DATA['g_mag_abs']
Color = DATA['b_min_v']
Vperp = DATA['vperp']

for i in range(len(Mag_G)):
	
	if Vperp[i] < 10:
		plt.scatter(Color[i], Mag_G[i], s = 2.0, c = 'indigo', edgecolors = 'none')	
		
	elif Vperp[i] >= 10 and Vperp[i] < 20:
		plt.scatter(Color[i], Mag_G[i], s = 2.4, c = 'cornflowerblue', edgecolors = 'none')
		
	elif Vperp[i] >= 20 and Vperp[i] < 50:
		plt.scatter(Color[i], Mag_G[i], s = 3.0, c = 'mediumseagreen', edgecolors = 'none')		
		
	elif Vperp[i] >= 50 and Vperp[i] < 100:
		plt.scatter(Color[i], Mag_G[i], s = 3.0, c = 'darkgreen', edgecolors = 'none')
		
	elif Vperp[i] >= 100 and Vperp[i] < 150:
		plt.scatter(Color[i], Mag_G[i], s = 3.5, c = 'gold', edgecolors = 'none')					
		
	elif Vperp[i] >= 150 and Vperp[i] < 200:
		plt.scatter(Color[i], Mag_G[i], s = 3.5, c = 'crimson', edgecolors = 'none')
		
	elif Vperp[i] > 200:
		plt.scatter(Color[i], Mag_G[i], s = 3.5, c = 'purple', edgecolors = 'none')	
	
Label  = [r'$v < 10$', r'$10 \leq v < 20$', r'$20 \leq v < 50$', r'$50 \leq v < 100$', r'$100 \leq v < 150$', r'$150 \leq v < 200$', r'$v \geq 200$']	
Colors = ['indigo', 'cornflowerblue', 'mediumseagreen', 'darkgreen', 'gold', 'crimson', 'purple']

for j in range(len(Label)):
	plt.plot(-10.0, -10.0, '.', ms = 9.0, c = Colors[j], label = Label [j])
		
plt.xlim(-0.3, 2.0)
plt.ylim(-4.0, 12.0)
plt.ylabel(r'$\mathrm{M_G}$')
plt.xlabel(r'$\mathrm{(B-V)}$')
plt.legend(frameon = False, loc = 'lower left', numpoints = 1)
plt.gca().invert_yaxis()
plt.savefig('GAIA_test.png')
#plt.show()
