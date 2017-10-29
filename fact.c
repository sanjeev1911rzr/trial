#include<stdio.h>
int main()
{
	int a[10000], n, d=9999, i, k, cal, f, j, c;
	scanf("%d",&n);
	for(i=0; i<10000; i++)
		a[i]=1;
	for(j=1; j<=n; j++)
	{
		k=0;
		for(i=9999; i>=d; i--)
		{
			if(i>d)
			{
				cal=(j*a[i])+k;
				a[i]=cal%10;
				k=cal/10;
			}
			else
			{
				c=0;
				cal=(j*a[i])+k;
				if(cal>9)
				{
					f=cal;
					while(f>0)
					{
						c++;
						f=f/10;
					}
					d=d-(c-1);
					while(cal>0)
					{
						a[i]=cal%10;
						cal=cal/10;
						i--;
					}
				}
				else
				{
					a[i]=cal;
				}
			}
		}
	}
	for(i=d; i<10000; i++)
		printf("%d",a[i]);
	return 0;
}