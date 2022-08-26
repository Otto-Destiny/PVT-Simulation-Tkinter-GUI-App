#!/usr/bin/env python
# coding: utf-8

# In[30]:


import math


# In[31]:


#API Gravity Formula
def api_gravity(Yo):
    API = float((141.5 / Yo) - 131.5)
    return API

#Gas Oil Ratio Formula
def gasoil_ratio(P, T, Yg, API):
    X = float(0.0125 * API - 0.00091 * (T - 460))
    Rs = float(Yg * (((P / 18.2) + 1.4) * (10 ** X)) ** 1.2048)
    return Rs

#Bubble-point Pressure Formula
def bubble_pressure(T, Yg, Rs, API):
    A = float(0.00091 * (T - 460) - 0.0125 * API)
    Pb = float(18.2 * (((Rs / Yg) ** 0.83) * (10**A) - 1.4))
    return Pb

#Oil Formation Volume Factor Formula
def oil_fvf(T, Yo, Yg, Rs):
    A = float(Rs * pow((Yg / Yo), 0.5))
    Bo = float(0.9759 + 0.00012 * pow((A + 1.25 * (T - 460)), 1.2))
    return Bo

#Gas Formation Volume Factor Formula
def gas_fvf(P, T, z):
    Bg = float(0.00502 * z * T / P)
    return Bg

#Gas Density Formula
def gas_density(P, T, z, Yg):
    pg = float(Yg * 28.96 * P / (z * 10.732 * T))
    return pg


# In[ ]:




