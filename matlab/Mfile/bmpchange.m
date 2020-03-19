A = imread('f:\cloud\Mfile\aa.bmp');


a = 0;
b=0;
c=0;
for x = 730:-1:1
    for k =1:720
        for m = 3:-1:1
           a  = a + uint32(A(x,k,m));
        end
    end
end
A = imread('f:\cloud\Mfile\bb.bmp');
for x = 730:-1:1
    for k =1:720
        for m = 3:-1:1
           b  = b + uint32(A(x,k,m));
        end
    end
end
A = imread('f:\cloud\Mfile\cc.bmp');
for x = 730:-1:1
    for k =1:720
        for m = 3:-1:1
           c  = c + uint32(A(x,k,m));
        end
    end
end
d = a+b+c
