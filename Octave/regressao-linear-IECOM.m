close all;
clear;
clc;
 
beta_0 = 1.0;
Ptx = -59;
d = 1:0.5:10; %% em metros
d = d';

rssi = [-60.0 -64.5 -71.0 -67.0 -64.0 -70.0 -69.0 -73.0 -75.0 -68.0 -68.0 -69.0 -70.5 -72.0 -61.0 -67.0 -71.0 -66.0 -71.0];
 
PL = Ptx - rssi;
PL = PL';
 
y = (PL - beta_0)/10;
x = log10(d);
 
 % Regressão Linear
 %% A = w*f
eta = (pinv(x'*x))*x'*y;
%L = eta*x;
PLm = beta_0 + 10*eta*log10(d);
 
 % Plota o gráfico de Pd em função da gamma (em dB) para cada valor de Pfa
h = figure;
semilogx(d,PL, 'ko','LineWidth',1.5);
hold on;
semilogx(d,PLm, 'r','LineWidth',1.5);
legend('Dados    ','Modelo', 'Location','NorthWest');
xlabel('d (m)', 'FontSize', 16, 'FontName','Times');
ylabel('PL (dB)', 'FontSize', 16, 'FontName','Times');
grid on;
set(gca,'FontSize', 14);
set(gca,'FontName','Times');
set(gca,'LineWidth',1.5);
set(h,'Units','Inches');
pos = get(h,'Position');
set(h,'PaperPositionMode','Auto','PaperUnits','Inches','PaperSize',[pos(3), pos(4)]);

% % % Salva a figura no formato pdf
nomefigura = ['beacons'];
print(h,nomefigura,'-dpdf','-r0');
 
 
 