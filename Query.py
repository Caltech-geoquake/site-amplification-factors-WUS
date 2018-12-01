# -*- coding: utf-8 -*-

import os
import numpy as np
import matplotlib.pyplot as plt

def query(Vs30_in_m_per_sec, z1000_in_m, PGA_in_g, show_fig=True):
    PGA_levels = [0.01, 0.05, 0.1, 0.2, 0.3, 0.4, 0.5, 0.75, 1.0, 1.25, 1.5]

    Vs30 = int(Vs30_in_m_per_sec)
    z1000 = int(z1000_in_m)
    PGA = PGA_in_g

    if PGA not in PGA_levels:
        raise ValueError('PGA must be present in `PGA_levels`.')
    if not os.path.exists('./data/%03d_%03d_period.csv' % (Vs30, z1000)):
        raise IOError('(Vs30, z1000) combination not found among CSV files.')

    T = np.genfromtxt('./data/%03d_%03d_period.csv' % (Vs30, z1000))
    avg = np.genfromtxt('./data/%03d_%03d_af_rs_nl_hh_avg.csv' % (Vs30, z1000),
                        delimiter=',')[PGA_levels.index(PGA)]
    std = np.genfromtxt('./data/%03d_%03d_af_rs_nl_hh_std.csv' % (Vs30, z1000),
                        delimiter=',')[PGA_levels.index(PGA)]

    if show_fig:
        plt.figure()
        plt.fill_between(T, avg + std, avg - std, alpha=0.2, label='St. dev.')
        plt.semilogx(T, avg, label='Mean value')
        plt.grid(ls=':')
        plt.legend(loc='upper left')
        plt.xlabel('Period [sec]')
        plt.ylabel('Amplification')
        plt.title('Vs30 = %d m/s, z1000 = %d m, PGA = %.2fg' % (Vs30, z1000, PGA))

    return T, avg, std


Vs30 = 300  # unit: m/s
z1000 = 150  # unit: m
PGA = 0.5  # unit: g

T, amplif_avg, amplif_std = query(Vs30, z1000, PGA, show_fig=True)

