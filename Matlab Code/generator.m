format long
dc = 0.8;
dt = 0.025;
stroke = 12;
r1 = 10;
r2 = 20;
L = 5;

xc1 = L/2;
yc1 = 0;
xc2 = -L/2;
yc2 = 0;
T = 1;
w = 2*pi/T;

a3 = (-4*(stroke/2+stroke/dc*dt)-2*stroke/dc*(T-dc-2*dt))/(T-dc-2*dt)^3;
a2 = -3/2*a3*(T-dc-2*dt);
a1 = -stroke/dc;
a0 = -(stroke/2+stroke/dc*dt);
i=1;
ht = 6;
n = 1/0.01 + 1;
Time = zeros(n, 1);
x = zeros(n, 1);
y = zeros(n, 1);
Q1 = zeros(n, 1);
Q2 = zeros(n, 1);
o1 = zeros(n, 1);
o2 = zeros(n, 1);
a = zeros(n, 1);
b = zeros(n, 1);
for time = 0:0.01:1
Time(i)=time;
t = mod(time,1);
if t<=(dc+dt)
x(i)= stroke/2 + stroke/dc*(-t);%stroke with velocity extension for 'dt'seconds
elseif t<=(T-dt)
x(i) = a0 + a1*(t-(dc+dt)) + a2*(t-(dc+dt))^2 + a3*(t-(dc+dt))^3;%stride path
else
x(i)= stroke/2 + stroke/dc*(T-t);%velocity extension for 'dt'seconds before stride
end
%t = mod(t,1);
if t<=dc
y(i)= -18;%stance
else
y(i) = -18 + 0 + 16*ht/(T-dc)^2*(t-dc)^2 - 32*ht/(T-dc)^3*(t-dc)^3 + 16*ht/(T-dc)^4*(t-dc)^4;%stride
end

a(i) = sqrt((x(i) - xc1)^2 + (y(i) - yc1)^2);
b(i) = sqrt((x(i) - xc2)^2 + (y(i) - yc2)^2);
o1(i) = acos((-r2^2 + r1^2 + b(i)^2 )/(2*r1*b(i)));
o2(i) = acos((-r2^2 + r1^2 + a(i)^2 )/(2*r1*a(i)));
g1 = acos (-(a(i)^2 - L^2 - b(i)^2 )/(2*L*b(i)));
g2 = acos (-(b(i)^2 - L^2 - a(i)^2 )/(2*L*a(i)));
Q2(i) = - (g1+o1(i))*180/pi;
Q1(i) = - (pi-(g2+o2(i)))*180/pi;
xa = xc1 + r1 * cos(Q1(i));
ya = yc1 + r1 * sin(Q1(i));
xb = xc2 + r1 * cos(Q2(i));
yb = yc2 + r1 * sin(Q2(i));
i=i+1;
end
plot(x, y);
