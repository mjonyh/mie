from scipy import interpolate
import numpy as np

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
  print '''
This is a class to interpolate the data in a file
that gives the output in a desired position.
''' 

