from scipy import interpolate
import numpy as np

class Load:
  def __init__(self):
    self.data_cu = np.loadtxt("Rakic.dat");

    self.wl = self.data_cu[:,0];
    self.n = self.data_cu[:,1];
    self.k = self.data_cu[:,2];
    'print self.n, self.n/1.33'

    self.intpn = interpolate.interp1d(self.wl,self.n);
    self.intpk = interpolate.interp1d(self.wl,self.k);

    self.data_w = np.loadtxt("water.dat");

    self.wl_w = self.data_w[:,0];
    self.n_w = self.data_w[:, 3];
    self.k_w = self.data_w[:, 4];

    self.intpn_w = interpolate.interp1d(self.wl_w, self.n_w);
    self.intpk_w = interpolate.interp1d(self.wl_w, self.k_w);
    
  def intpdata(self, x):
    return self.intpn(x), self.intpk(x), self.intpn_w(x), self.intpk_w(x);
if __name__ == '__main__':
  print '''
This is a class to interpolate the data in a file
that gives the output in a desired position.
''' 

