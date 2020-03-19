BK=zeros(730,720,3,'uint8');
i= 0;
for x = 730:-1:1
    for k =1:720
        for m = 3:-1:1
           a  =  mod(i,256);
           BK(x,k,m)=a;
            if (a == 0)
                BK(x,k,m)=floor( i/65536);       
            end
            if (a == 1)
                BK(x,k,m)=(mod(i,65536)/256);
            end
            if (a == 2)
                BK(x,k,m)=0;
            end
      
            i= i+1;
            
        end
    end
end
imshow(BK);
imwrite(BK,'cc.bmp')

