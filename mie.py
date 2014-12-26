from pymiecoated import Mie
from numpy import pi
import matplotlib.pyplot as plt
from load import Load

intp_data = Load();
'print intpdata(0.3)'

a = 0.8;
wl = [];
qsca = [];
mie = Mie();

for i in range(210, 1200):
  wave_length = i*0.01;
  mie.x = a * 2*pi/wave_length;
  n, k = intp_data.intpdata(0.01*i);
  mie.m = complex(n, k);

  wl.append(i);
  qsca.append(mie.qext());

plt.plot(wl, qsca)
plt.show()
