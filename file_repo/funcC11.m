function [res] = funcC11(point, tol, n_lim, flag)
  # Symbolic package is needed to run this
  # pip install sympy
  # pkg install -forge symbolic
  
  # point: vektor [x1, x2, ..., xn] titik percobaan
  # tol: tolerance
  # n_lim: limit percobaan
  # Flag: 1 if ascent, 0 if descent
  pkg load symbolic;
  warning('off', 'OctSymPy:sym:rationalapprox');
  syms x y h real;
  
  nums = size(point)(1);
  res = point;
  
  symbols = [x, y];
  funcTo = x^2 - x*y + y^2 + exp(x*y);
  
  for i = 1:length(symbols)
    funcGrad(i) = diff(funcTo, symbols(i));
  endfor
  
  # Ascent / descent
  for k = 1:nums
    k
    difference = res(k, :);
    n = 1
    while norm(difference) > tol && norm(res(k, :)) > 0 && n <= n_lim
      grad = subs(funcGrad, symbols, res(k, :));
      
      f_res = res(k, :) + h * grad;
      
      g = simplify(subs(funcTo, symbols, f_res));
      gh = simplify(diff(g, h));
      h_res = solve(gh, h);
      
      if flag == 1
        next_res = double(res(k, :) + h_res * grad);
      else
        next_res = double(res(k, :) - h_res * grad);
      endif
      
      difference = next_res - res(k, :);
      res(k, :) = next_res
      
      n = n+1
    endwhile
  endfor
  res
endfunction