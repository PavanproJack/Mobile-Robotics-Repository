%  create a homogeneous transformation using the function SE2

T1 = SE2(1, 2, 30*pi/180);
disp(T1)
 
 % Coordinate frames drawn using the Toolbox function trplot2
 axis([0 5 0 5])
 trplot2(T1, 'frame', '1', 'color', 'b');
 grid on
 
 T2 = SE2(2, 1, 0);
 disp(T2)
 
 hold on
 trplot2(T2, 'frame', '2', 'color', 'red')
 
 T3 = T1 * T2;
 T4 = T2 * T1;
 
 hold on 
 trplot2(T3, 'frame', '3', 'g');
 trplot2(T4, 'frame', '4', 'c');
 
 
 point = [3; 2];
 plot_point(point, '*');
 
 p_1 = inv(T1) ;
 
 disp(p_1; point)

 
 
 
 