# -*- coding: utf-8 -*-
"""
Created on Thu Aug 18 12:13:47 2022

@author: 05709
"""
import numpy as np
from math import sqrt, exp, log, erf
from scipy.stats import norm 
from decimal import *

spot=float(input("donnez le spot:  " ))
strike=float(input("donnez le strike:  " ))
sigma=float(input("donnez la volatilité annuelle:  " ))
rate=float(input("donnez le Taux domestique sans risque :  " ))
divrate=float(input("donnez le Taux étrangé sans risque :  " ))
T=int(input("donnez la maturité de l'option en jour :  " ))
sigma=sigma/100
rate=rate/100
divrate=divrate/100
sigtsqrt= sqrt(Decimal(T)/365)*sigma
edivt= exp((-divrate*T)/365)
ert= exp((-rate*T)/365)
d1= (log(spot/strike)+(rate-divrate+0.5*(sigma**2))*(T/365))/sigtsqrt
d2=d1-sigtsqrt

print("\n \n le prix du call : ",round(spot*edivt*norm.cdf(d1)-strike*ert*norm.cdf(d2),4),"  TND")