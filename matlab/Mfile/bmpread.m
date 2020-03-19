A = imread('f:\cloud\Mfile\MEINV.bmp');
B = zeros(1920,1080,'uint8');
C = zeros(1920,1080,'uint8');
D = zeros(1920,1080,'uint8');
E = zeros(1920,1080,'uint8');
F = zeros(1920,1080,'uint8');
B(:,:) = A(:,:,1);

C(:,:) = A(:,:,2);

D(:,:) = A(:,:,3);

E = B*0.2989 + 0.5870 * C + 0.1140 * D;

F = rgb2gray(A);


for x = 1:960
    for k = 1:1080
        for m = 1:3
        V = A(x,k,m);
            A(x,k,m)= A(x+960,k,m);
        A(x+960,k,m) =V;       
        end
    end
end
imshow(A);
G = mean(A);
mean(G)





