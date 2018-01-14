#include<stdio.h>
#include<string.h>
void main()
{
 char s[100000],p[100000];
 int i,beg=0,len;
 scanf("%s",s);
 len=strlen(s);


 for(i=len-1;i>=0;i--)
 {p[beg]=s[i];
    beg++;

 }
 p[beg]='\0';

 printf("\n%s",p);
}