import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as p
import numpy as n

DATA = n.loadtxt('../data/ssp_M11_MILES_UVextended_revisednearIRslope_nearIRextended.ssz002', unpack=True)

ages = n.array(list(set(DATA[0])))

p.figure(0, (12,5))
p.axes([0.1,0.15,0.85,0.8])
for age in ages:
	sel = (DATA[0]==age)
	p.plot(DATA[1][sel], DATA[2][sel],label=str(int(age))+" Gyr",rasterized=True)

p.xlabel(r'$\lambda$ Angstrom')
p.ylabel(r'Flux for $M_\odot$ $[f_{\lambda},\; erg s^{-1} A^{-1}]$')
p.xscale('log')
p.yscale('log')
p.ylim((1e20,1e30))
p.xlim((900,200000))
p.grid()
p.title('Solar metallicity')
p.legend(frameon=False, loc=0)
p.savefig('../images/galaxy_models.png')
p.clf()

