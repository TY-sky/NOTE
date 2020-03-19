clear all;
%clc;
 %描述一个16位位宽的数据
y=0:1;
 N = length(y);        %%数据的长度，即存储器深度。
word_len = 16;           %%每个单元的占据的位数，需自己设定。
len = ceil(word_len/8);  %%转换成字节数。
y_quan =fi(y,1,word_len,0); %%该函数详细见Matlab帮助
fid=fopen('p1.txt','w');%打开文件
temp1=fi(256,0,9,0);
 word_len = fi(len,0,8,0); %%即前面所说的”nn”
for i=1:N
 addr = fi(i-1,0,16,0); %%即前面所说的”aaaa”
%%下面计算校验和
    temp=word_len+bitsliceget(addr,16,9)+bitsliceget(addr,8,1);
     temp=temp+bitsliceget(y_quan(i),16,9)+bitsliceget(y_quan(i),8,1);
     temp=bitsliceget(temp,8,1); %%取低8位，即相当于取模256
     temp=temp1-temp;%%上面两步是取其补码，如果字长是n位，大小%%为a,则其补码为2^n-a;
     temp=bitsliceget(temp,8,1); %%重新取低8位，这里需要明白%Matlab中fi构造的定点数性质
    fprintf(fid,strcat(':',hex(word_len),hex(addr),'00',hex(bitsliceget(y_quan(i),16,9)),hex(bitsliceget(y_quan(i),8,1)),hex(temp),'\n')); 
 end
 fprintf(fid,':00000001ff');

fclose(fid);  %%关闭文件

