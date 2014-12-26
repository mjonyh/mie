import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

class Load:
  def __init__(self):
    self.data = np.loadtxt("Rakic.dat");

    self.wl = self.data[:,0];
    self.n = self.data[:,1];
    self.k = self.data[:,2];

    self.intpn = interpolate.interp1d(self.wl,self.n);
    self.intpk = interpolate.interp1d(self.wl,self.k);

  def intpdata(self, x):
    return self.intpn(x), self.intpk(x);
if __name__ == '__main__':
  int_data = Load();
 
  new = np.arange(0.21, 1.3, 0.01);
  n, k = int_data.intpdata(new);

  plt.plot(new, n,'go')

  plt.show()

