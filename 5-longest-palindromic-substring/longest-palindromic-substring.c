#include<string.h>
char* longestPalindrome(char* s)
{
    int i,j,m,max_len=0,start=0;
    int n =strlen(s);
    char *max_palendrome;
    for(int offset=0;offset<2;offset++)
    {
        for(int i=0;i<n;i++)
        {
            int k=i;
            int l=i+offset;
            int len=l-k+1;
            while(k>=0 && l<n && s[k]==s[l])
            {
                len=l-k+1;
                if(len>max_len)
                {
                    start=k;
                    max_len = len;
                }
                k--;
                l++;
            }
        }
    }
    max_palendrome=(char*)malloc((max_len+1)*sizeof(char));
    for(m=0;m<max_len;m++)
    {
        max_palendrome[m]=s[m+start];
    }
    max_palendrome[max_len]='\0'; 
    return max_palendrome;
}