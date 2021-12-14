A_inf = [3 5; -1 -3]
A_sup = [4 6; 1 1]
b_inf = [-3; -1]
b_sup = [4; 2]

xx = [kinterval(26/21, 2/21); kinterval(-4/3, 2/3)]

A = kinterval(A_inf, A_sup)
b = kinterval(b_inf, b_sup)

opts.stepwise = true
opts.max_iterations_num = 20
opts.tau = 1;

[x, opts] = subdiff(A, b, opts)
        
while ~opts.finish
    [x_stepwise, opts] = subdiff(opts);
    fprintf("-----\niteration: %d\n",opts.status.iteration);
    x_stepwise 
endwhile
        