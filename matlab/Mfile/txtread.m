clear all;
%clc;
 %����һ��16λλ�������
y=0:1;
 N = length(y);        %%���ݵĳ��ȣ����洢����ȡ�
word_len = 16;           %%ÿ����Ԫ��ռ�ݵ�λ�������Լ��趨��
len = ceil(word_len/8);  %%ת�����ֽ�����
y_quan =fi(y,1,word_len,0); %%�ú�����ϸ��Matlab����
fid=fopen('p1.txt','w');%���ļ�
temp1=fi(256,0,9,0);
 word_len = fi(len,0,8,0); %%��ǰ����˵�ġ�nn��
for i=1:N
 addr = fi(i-1,0,16,0); %%��ǰ����˵�ġ�aaaa��
%%�������У���
    temp=word_len+bitsliceget(addr,16,9)+bitsliceget(addr,8,1);
     temp=temp+bitsliceget(y_quan(i),16,9)+bitsliceget(y_quan(i),8,1);
     temp=bitsliceget(temp,8,1); %%ȡ��8λ�����൱��ȡģ256
     temp=temp1-temp;%%����������ȡ�䲹�룬����ֳ���nλ����С%%Ϊa,���䲹��Ϊ2^n-a;
     temp=bitsliceget(temp,8,1); %%����ȡ��8λ��������Ҫ����%Matlab��fi����Ķ���������
    fprintf(fid,strcat(':',hex(word_len),hex(addr),'00',hex(bitsliceget(y_quan(i),16,9)),hex(bitsliceget(y_quan(i),8,1)),hex(temp),'\n')); 
 end
 fprintf(fid,':00000001ff');

fclose(fid);  %%�ر��ļ�

