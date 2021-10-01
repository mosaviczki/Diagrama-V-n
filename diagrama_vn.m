clear all
clc

n_lim_pos = 2.5;
n_lim_neg = -1;
n_ult_pos = 3.75;
n_ult_neg = -1.5;
dens_ar = 1.225;
g = 9.80665;

peso = (input('Peso da aeronave (N): '));
area_asa = (input('Area da asa (m^2): '));
cl_max = (input('Coeficiente de sustentação máximo: '));
v_max = (input('Velocidade maxima (m/s): '));
envergadura = (input('Envergadura da asa (m): '));
a = (input('Inclinação da curva de sustentação da asa no encontro com a rajada: '));

%CALCULOS PARA DIAGRAMA DE MANOBRA:

v_cru = 0.9 * v_max;
v_mergulho = 1.25 * v_max;
v_estol = sqrt((2*peso)/(dens_ar*area_asa*cl_max));
v_manobra = v_estol * sqrt(n_lim_pos);

%curva superior fator limite
n_AB = (linspace(0, n_lim_pos, 200));
v_AB = (sqrt((n_AB*2*peso)/(dens_ar*area_asa*cl_max)));
n_BC = [n_lim_pos, n_lim_pos];
v_BC = [v_AB(end), v_mergulho];

%curva inferior fator limite
n_AE = (linspace(0, n_lim_neg, 200));
v_AE = (sqrt((n_AE*2*peso)/(dens_ar*area_asa*-cl_max)));
n_ED = [n_lim_neg, n_lim_neg];
v_ED = [v_AE(end), v_mergulho];

%curva superior fator ultimo
n_ult_sup = (linspace(n_lim_pos, n_ult_pos, 200));
v_ult_sup = (sqrt((n_ult_sup*2*peso)/(dens_ar*area_asa*cl_max)));
n_ult_sup_linha = [n_ult_pos, n_ult_pos];
v_ult_sup_linha = [v_ult_sup(end), v_mergulho];

%curva inferior fator ultimo
n_ult_inf = (linspace(n_lim_neg, n_ult_neg, 200));
v_ult_inf = (sqrt((n_ult_inf*2*peso)/(dens_ar*area_asa*-cl_max)));
n_ult_inf_linha = [n_ult_neg, n_ult_neg];
v_ult_inf_linha = [v_ult_inf(end), v_mergulho];

%linhas limite de velocidade
v_aux = [v_mergulho, v_mergulho];
n_linha_v1 = [n_lim_pos, n_ult_pos];
n_linha_CD = [n_lim_neg, n_lim_pos];
n_linha_v2 = [n_ult_neg, n_lim_neg];

%CALCULOS PARA DIAGRAMA DE RAJADA:
massa = peso/g;
corda_m = (area_asa/envergadura);
mi = (2*massa)/(dens_ar * corda_m * a * area_asa);
kg = (0.88 * mi)/(5.3 + mi);

%linhas de rajada
vetor_rajada_mer = [0, v_mergulho];
vetor_rajada_cru = [0, v_cru];
vetor_rajada_man = [0, v_manobra];
n_rajada1 = [1, 1+((kg * 7.62 * v_mergulho * a * dens_ar * area_asa)/(2*peso))];
n_rajada2 = [1, 1+((kg * 15.24 * v_cru * a * dens_ar * area_asa)/(2*peso))];
n_rajada3 = [1, 1+((kg * 20.1168 * v_manobra * a * dens_ar * area_asa)/(2*peso))];
n_rajada4 = [1, 1+((kg * -7.62 * v_mergulho * a * dens_ar * area_asa)/(2*peso))];
n_rajada5 = [1, 1+((kg * -15.24 * v_cru * a * dens_ar * area_asa)/(2*peso))];
n_rajada6 = [1, 1+((kg * -20.1168 * v_manobra * a * dens_ar * area_asa)/(2*peso))];

%linhas verticais tracejadas
%v_aux já declarado anteriormente
v_aux2 = [v_cru, v_cru];
v_aux3 = [v_manobra, v_manobra];
link_rajada1 = [n_rajada1(end), n_rajada4(end)];
link_rajada2 = [n_rajada2(end), n_rajada5(end)];
link_rajada3 = [n_rajada3(end), n_rajada6(end)];

%controno do diagrama de rajada
contorno_rajada_v = [v_mergulho, v_cru, v_manobra];
contorno_rajada_n_sup = [n_rajada1(end), n_rajada2(end), n_rajada3(end)];
contorno_rajada_n_inf = [n_rajada4(end), n_rajada5(end), n_rajada6(end)];

fprintf('\n--------------------------------------------------------\n');
fprintf('Velocidade de estol:     %.2f m/s\n', v_estol);
fprintf('Velocidade de manobra:   %.2f m/s\n', v_manobra);
fprintf('Velocidade de cruzeiro:  %.2f m/s\n', v_cru); 
fprintf('Velocidade de mergulho:  %.2f m/s\n', v_mergulho); 
fprintf('--------------------------------------------------------\n');

hold on


yline(0)
xline(v_estol, 'g--')
scatter(v_estol, 0, 'kx')
text(v_estol, 0.3, ' v. de estol')
scatter(v_manobra, 0, 'kx')
text(v_manobra, -0.3, ' v. de manobra')
scatter(v_cru, 0, 'kx')
text(v_cru, 0.3, ' v. de cruzeiro')
scatter(v_mergulho, 0, 'kx')
text(v_mergulho, -0.3, ' v. de mergulho')
plot(v_AB,n_AB, 'b',v_BC,n_BC, 'b',v_AE,n_AE, 'b',v_ED,n_ED, 'b',v_aux, n_linha_CD, 'b')
plot(v_ult_sup, n_ult_sup, 'r--',v_ult_inf, n_ult_inf, 'r--',v_ult_sup_linha, n_ult_sup_linha, 'r--',v_ult_inf_linha, n_ult_inf_linha, 'r--',v_aux, n_linha_v1, 'r--',v_aux, n_linha_v2, 'r--')
plot(contorno_rajada_v, contorno_rajada_n_sup, 'k--') 
plot(contorno_rajada_v, contorno_rajada_n_inf, 'k--')
plot(vetor_rajada_mer, n_rajada1, 'k--')
plot(vetor_rajada_cru, n_rajada2,'k--')
plot(vetor_rajada_man, n_rajada3, 'k--')
plot(vetor_rajada_mer, n_rajada4, 'k--')
plot(vetor_rajada_cru, n_rajada5, 'k--')
plot(vetor_rajada_man, n_rajada6, 'k--')
plot(v_aux, link_rajada1, 'k--',v_aux2, link_rajada2,  'k--',v_aux3, link_rajada3,  'k--')
legend('','','','','','','Fator de carga limite','','','','', 'Fator de carga ultimo','','','','','', 'Fator de carga de rajada')
text((v_mergulho/2), (n_rajada1(end)/2)+0.1, '66 fps' )
text((v_cru/2), (n_rajada2(end)/2)+0.2, '50 fps' )
text((v_manobra/2), (n_rajada3(end)/2)+0.3, '25 fps' )
text((v_mergulho/2), (n_rajada4(end)/2)-0.1, '-66 fps' )
text((v_cru/2), (n_rajada5(end)/2)-0.2, '-50 fps' )
text((v_manobra/2), (n_rajada6(end)/2)-0.3, '-25 fps' )

title("Diagrama v-n")
xlabel('Velocidade (m/s)')
ylabel('Fator de carga')
grid
hold off
