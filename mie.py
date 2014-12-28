from pymiecoated import Mie
import numpy as np
import matplotlib.pyplot as plt
from load import Load

class Mie_class:
  def __init__(self):
    self.intp_data = Load();

  def mie(self, a = 0.3):
    qsca = [];
    qabs = [];
    qext = [];
    mie = Mie();

    wl = np.arange(0.21, 1.2, .001);

    n_cu, k_cu, n_w, k_w = self.intp_data.intpdata(wl);

    for i in range(len(wl)):
      mie.x = a * 2*np.pi/wl[i];
      mie.m = complex(n_cu[i], k_cu[i]);
      mie.y = 3 * a * 2*np.pi/wl[i];
      mie.m2 = complex(n_w[i], k_w[i]);
      qsca.append(mie.qsca());
      qabs.append(mie.qabs());
      qext.append(mie.qb());

    return wl, qsca, qabs, qext;
