%pkg load image
addpath matting/
addpath gaimc/

in_name = './in22.png'; 
disp(['Working on image index = ' int2str(i)]);
input = im2double(imread(in_name));
input = reshape_img(input, 700);
size(input)

close all
figure; imshow(input);
[h w c] = size(input);

disp('Compute Laplacian its cost a lot of time');
A = getLaplacian1(input, zeros(h, w), 1e-7, 1);

disp('finished compute Laplacian');

disp('Save to disk');
n = nnz(A);
[Ai, Aj, Aval] = find(A);
CSC = [Ai, Aj, Aval];

[rp ci ai] = sparse_to_csr(A);
Ai = sort(Ai);
Aj = ci;
Aval = ai;
CSR = [Ai, Aj, Aval];
save(['mat.mat'], 'CSR');
 
