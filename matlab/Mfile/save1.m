a= imread('f:\cloud\Mfile\Part1_G140_DemuraFlash_rendBGR.bmp');
BK=zeros(4279,4,3,'uint8');
BK(:,:,:) = 170;

fid = fopen('f:\cloud\Mfile\b.txt','wt');
fprintf(fid,'%x',BK);  
fclose(fid);