clc, clearvars, close all

x = -3.5:0.01:3.5;
y = -3.5:0.01:3.5;
[X,Y] = meshgrid(x,y);

Z = complex(X,Y);
z = sym('z',size(Z));

% Rational Map
p_coeff = [-1, 0, i*sqrt(3), 0];
q_coeff = [0, -i*sqrt(3), 0, 1];

p = zeros(size(z)); % Initialize p array
q = zeros(size(z)); % Initialize q array

for i = 1:length(p_coeff) % Correct indexing
    p = p + p_coeff(i) * z.^(i-1); % Accumulate terms
end                       
for i = 1:length(q_coeff) % Correct indexing
    q = q + q_coeff(i) * z.^(i-1); % Accumulate terms
end

% Create derivative
p_prime_coeff = polyder(p_coeff);
q_prime_coeff = polyder(q_coeff);

p_prime = zeros(size(z)); % Initialize p_prime array
q_prime = zeros(size(z)); % Initialize q_prime array

for i = 1:length(p_prime_coeff) % Correct indexing
    p_prime = p_prime + p_prime_coeff(i) * z.^(i-1); % Accumulate terms
end
for i = 1:length(q_prime_coeff) % Correct indexing
    q_prime = q_prime + q_prime_coeff(i) * z.^(i-1); % Accumulate terms
end

% Energy density
den1 = abs(p_prime .* q - q_prime .* p);
den2 = real(q).^2 + imag(q).^2 + real(p).^2 + imag(p).^2;

density = ((1 + real(z).^2 + imag(z).^2).^2) .* (den1 ./ den2).^4; % Element-wise operators

% Plotting the 3D surface
figure;
sc = surfc(x, y, density(Z), 'EdgeColor', 'none');