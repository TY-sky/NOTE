img = zeros(2436,1125,'uint8');
gray_step = floor(1125/256);
gray_xstep = mod(1125 ,256); 
address = 0;
a=0;
x = 0;
y = 0;
for i = 1:256
    
    if ((mod(i,2))&&gray_xstep)
        gray_xstep = gray_xstep -1;
        img(:,address+1 :address +gray_step) = uint8(i -1);
        img(:,address +gray_step+1) = uint8(255);
        img (1,address +gray_step+1 );
        address = address + gray_step+1;
        x = x+1;
    else  
        img(:,address+1 :address +gray_step) = uint8(i -1);
        address = address + gray_step;
        y = y+1;
    end
    a = a+1;
end
imshow(img);
imwrite(img,'1.bmp')