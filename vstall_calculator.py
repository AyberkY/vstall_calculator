# -*- coding: utf-8 -*-
"""
Created on Sun Jan  7 21:23:35 2018

@author: Ayberk Yaraneri
"""
import math
import pylab as plt

#   Vstall = (2/Clmax)^0.5 * (((weight*g)/area)/rho)^0.5

airframe = 0.7  #Airframe empty weight. (Without payload)
payload = 0.35  #Payload weight
weight = airframe + payload     #Take-off weight
rho = 1.225     #Air density
Clmax = 1.16    #Clmax (:p)
g = 9.80665
Vthrow = 38     #Launch velocity

area_vals = []
Vstall_vals = []
loading_vals = []
Vthrow_vals = []


def Vstall_calculate(weight, area, rho, Clmax, g, Vthrow):
    
    return math.sqrt(2/Clmax) * math.sqrt(((weight*g)/area)/rho) * 3.6


area = 0.05  
while area <= 0.3:
    area_vals.append(area)
    
    Vstall = Vstall_calculate(weight, area, rho, Clmax, g, Vthrow)
    Vstall_vals.append(Vstall)
    
    loading_vals.append((weight/area)*10)
    
    Vthrow_vals.append(Vthrow)
    
    area += 0.001
    
    if abs(Vthrow - Vstall) <= 0.1:
        print('Optimum planform area: ' + str(area) + ' (m^2)')
        print('Optimum loading: ' + str((weight/area) * 10) + ' (g/dm^2)')
        print('Chosen planform area: ' + str(0.135) + ' (m^2)')
        print('Chosen loading: ' + str((weight/0.135) * 10) + ' (g/dm^2)')
        optimum_area = area
        
# Turkish 
# plt.figure('Vstall')
# plt.plot(area_vals, Vstall_vals, color = 'm', label = 'Stall Hızı')
# plt.plot(area_vals, Vthrow_vals, label = 'Launch Velocity')
# plt.axhline(y = Vthrow, color = 'r', label = 'Fırlatma Hızı')
# plt.plot(optimum_area, (Vstall_calculate(weight, optimum_area, rho, Clmax, g, Vthrow)), '*', markersize = '8.0', color = 'g', label = 'Optimum Kanat Alanı')
# plt.plot(0.135, (Vstall_calculate(weight, 0.135, rho, Clmax, g, Vthrow)), '*', markersize = '8.0', color = (1, 0.9, 0.1), label = 'Seçilen Kanat Alanı')
# plt.legend()
# plt.ylabel('Stall Hızı (Km/h)')
# plt.xlabel('Kanat Alanı (m^2)')
# plt.title('Stall Hızı ve Kanat Alanı İlişkisi: ' + str(round(weight, 3)) + 'Kg')
# plt.savefig('Vstall_1050gr.png', dpi = 500)
# plt.show()

# English
plt.figure('Vstall')
plt.plot(area_vals, Vstall_vals, color = 'm', label = 'Stall Speed')
plt.axhline(y = Vthrow, color = 'r', label = 'Launch Velocity')
plt.plot(optimum_area, (Vstall_calculate(weight, optimum_area, rho, Clmax, g, Vthrow)), '*', markersize = '8.0', color = 'g', label = 'Optimum Wing Area')
plt.plot(0.135, (Vstall_calculate(weight, 0.135, rho, Clmax, g, Vthrow)), '*', markersize = '8.0', color = (1, 0.9, 0.1), label = 'Chosen Wing Area')
plt.legend()
plt.ylabel('Stall Speed (Km/h)')
plt.xlabel('Wing Area (m^2)')
plt.title('Stall Speed vs Wing Area: ' + str(round(weight, 3)) + 'Kg')
plt.savefig('Vstall_1050gr.png', dpi = 500)
plt.show()