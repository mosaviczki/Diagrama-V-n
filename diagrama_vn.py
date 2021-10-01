import math
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

n_lim_pos = 2.5
n_lim_neg = -1
n_ult_pos = 3.75
n_ult_neg = -1.5
dens_ar = 1.225
g = 9.80665

peso = float(input('Peso da aeronave (N): '))
area_asa = float(input('Area da asa (m^2): '))
cl_max = float(input('Coeficiente de sustentação máximo: '))
v_max = float(input('Velocidade maxima (m/s): '))
envergadura = float(input('Envergadura da asa (m): '))
a = float(input('Inclinação da curva de sustentação da asa no encontro com a rajada: '))

#CALCULOS PARA DIAGRAMA DE MANOBRA:

v_cru = 0.9 * v_max
v_mergulho = 1.25 * v_max
v_estol = math.sqrt((2*peso)/(dens_ar*area_asa*cl_max))
v_manobra = v_estol * math.sqrt(n_lim_pos)

#curva superior fator limite
n_AB = (np.linspace(0, n_lim_pos, 200, True ))
v_AB = list(map(lambda n: (math.sqrt((n*2*peso)/(dens_ar*area_asa*cl_max))), n_AB))
n_BC = [n_lim_pos, n_lim_pos]
v_BC = [v_AB[-1], v_mergulho]

#curva inferior fator limite
n_AE = (np.linspace(0, n_lim_neg, 200, True ))
v_AE = list(map(lambda n: (math.sqrt((n*2*peso)/(dens_ar*area_asa*-cl_max))), n_AE))
n_ED = [n_lim_neg, n_lim_neg]
v_ED = [v_AE[-1], v_mergulho]

#curva superior fator ultimo
n_ult_sup = (np.linspace(n_lim_pos, n_ult_pos, 200, True ))
v_ult_sup = list(map(lambda n: (math.sqrt((n*2*peso)/(dens_ar*area_asa*cl_max))), n_ult_sup))
n_ult_sup_linha = [n_ult_pos, n_ult_pos]
v_ult_sup_linha = [v_ult_sup[-1], v_mergulho]

#curva inferior fator ultimo
n_ult_inf = (np.linspace(n_lim_neg, n_ult_neg, 200, True ))
v_ult_inf = list(map(lambda n: (math.sqrt((n*2*peso)/(dens_ar*area_asa*-cl_max))), n_ult_inf))
n_ult_inf_linha = [n_ult_neg, n_ult_neg]
v_ult_inf_linha = [v_ult_inf[-1], v_mergulho]

#linhas limite de velocidade
v_aux = [v_mergulho, v_mergulho]
n_linha_v1 = [n_lim_pos, n_ult_pos]
n_linha_CD = [n_lim_neg, n_lim_pos]
n_linha_v2 = [n_ult_neg, n_lim_neg]


#CALCULOS PARA DIAGRAMA DE RAJADA:

massa = peso/g
corda_m = (area_asa/envergadura)
mi = (2*massa)/(dens_ar * corda_m * a * area_asa)
kg = (0.88 * mi)/(5.3 + mi)

#linhas de rajada
vetor_rajada_mer = [0, v_mergulho]
vetor_rajada_cru = [0, v_cru]
vetor_rajada_man = [0, v_manobra]
n_rajada1 = [1, 1+((kg * 7.62 * v_mergulho * a * dens_ar * area_asa)/(2*peso))]
n_rajada2 = [1, 1+((kg * 15.24 * v_cru * a * dens_ar * area_asa)/(2*peso))]
n_rajada3 = [1, 1+((kg * 20.1168 * v_manobra * a * dens_ar * area_asa)/(2*peso))]
n_rajada4 = [1, 1+((kg * -7.62 * v_mergulho * a * dens_ar * area_asa)/(2*peso))]
n_rajada5 = [1, 1+((kg * -15.24 * v_cru * a * dens_ar * area_asa)/(2*peso))]
n_rajada6 = [1, 1+((kg * -20.1168 * v_manobra * a * dens_ar * area_asa)/(2*peso))]

#linhas verticais tracejadas
v_aux = [v_mergulho, v_mergulho]
v_aux2 = [v_cru, v_cru]
v_aux3 = [v_manobra, v_manobra]
link_rajada1 = [n_rajada1[-1], n_rajada4[-1]]
link_rajada2 = [n_rajada2[-1], n_rajada5[-1]]
link_rajada3 = [n_rajada3[-1], n_rajada6[-1]]

#controno do diagrama de rajada
contorno_rajada_v = [v_mergulho, v_cru, v_manobra]
contorno_rajada_n_sup = [n_rajada1[-1], n_rajada2[-1], n_rajada3[-1]]
contorno_rajada_n_inf = [n_rajada4[-1], n_rajada5[-1], n_rajada6[-1]]

print('--------------------------------------------------------')
print('Velocidade de estol:     {0:.2f} m/s' .format(v_estol)) 
print('Velocidade de manobra:   {0:.2f} m/s' .format(v_manobra)) 
print('Velocidade de cruzeiro:  {0:.2f} m/s' .format(v_cru)) 
print('Velocidade de mergulho:  {0:.2f} m/s' .format(v_mergulho)) 
print('--------------------------------------------------------')

#plots diagrama de manobra
plt.plot(v_AB,n_AB, color='blue', linewidth = 3, label='Fator de carga limite')
plt.plot(v_BC,n_BC, color='blue', linewidth = 3)
plt.plot(v_AE,n_AE, color='blue', linewidth = 3)
plt.plot(v_ED,n_ED, color='blue', linewidth = 3)
plt.plot(v_aux, n_linha_CD, color='blue', linewidth = 3)
plt.plot(v_ult_sup, n_ult_sup, linestyle= 'dashed', color='red', label='Fator de carga último')
plt.plot(v_ult_inf, n_ult_inf, linestyle= 'dashed', color='red')
plt.plot(v_ult_sup_linha, n_ult_sup_linha, linestyle= 'dashed', color='red')
plt.plot(v_ult_inf_linha, n_ult_inf_linha, linestyle= 'dashed', color='red')
plt.plot(v_aux, n_linha_v1, linestyle= 'dashed', color='red')
plt.plot(v_aux, n_linha_v2, linestyle= 'dashed', color='red')
plt.plot(contorno_rajada_v, contorno_rajada_n_sup, linestyle= 'dashed', color='black')
plt.plot(contorno_rajada_v, contorno_rajada_n_inf, linestyle= 'dashed', color='black')
plt.plot(vetor_rajada_mer, n_rajada1, linestyle= 'dashed', color='black')
plt.plot(vetor_rajada_cru, n_rajada2, linestyle= 'dashed', color='black')
plt.plot(vetor_rajada_man, n_rajada3, linestyle= 'dashed', color='black')
plt.plot(vetor_rajada_mer, n_rajada4, linestyle= 'dashed', color='black')
plt.plot(vetor_rajada_cru, n_rajada5, linestyle= 'dashed', color='black')
plt.plot(vetor_rajada_man, n_rajada6, linestyle= 'dashed', color='black', label='Fator de carga de rajada')
plt.plot(v_aux, link_rajada1, linestyle= 'dashed', color='gray')
plt.plot(v_aux2, link_rajada2, linestyle= 'dashed', color='gray')
plt.plot(v_aux3, link_rajada3, linestyle= 'dashed', color='gray')

plt.axhline(0, 0, 1, color='black')
plt.axvline(v_estol, 0, 1, linestyle= 'dashed', color='gray')
plt.scatter(v_estol, 0, color='gray')
plt.scatter(v_manobra, 0, color='gray')
plt.scatter(v_cru, 0, color='gray')
plt.scatter(v_mergulho, 0, color='gray')
plt.text(v_estol, 0.2, '  v. de estol')
plt.text(v_manobra, 0-0.2, '  v. de manobra')
plt.text(v_cru, 0.2, '  v. de cruzeiro')
plt.text(v_mergulho, 0-0.2, '  v. de mergulho')
plt.text((v_mergulho/2), (n_rajada1[-1]/2)+0.1, '66 fps' )
plt.text((v_cru/2), (n_rajada2[-1]/2)+0.2, '50 fps' )
plt.text((v_manobra/2), (n_rajada3[-1]/2)+0.3, '25 fps' )
plt.text((v_mergulho/2), (n_rajada4[-1]/2)-0.1, '-66 fps' )
plt.text((v_cru/2), (n_rajada5[-1]/2)-0.2, '-50 fps' )
plt.text((v_manobra/2), (n_rajada6[-1]/2)-0.3, '-25 fps' )

plt.title("Diagrama v-n")
plt.xlabel('Velocidade (m/s)')
plt.ylabel('Fator de carga')
plt.legend()
plt.show()