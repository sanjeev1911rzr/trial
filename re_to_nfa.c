#include<stdio.h>
#include<string.h>
#include<stdlib.h>
struct node
{
	int a;
	int b;
	int e;
	int n[3][10];
};
int main()
{
	//a[i].n[0]->change using a
	//a[i].n[1]->change using b
	//a[i].n[2]->change using e->epsilon
	//a[i].a->no. of state transition using a
	//int->initial node
	//fi->final node
	//count->new node which can be used
	//part of RE having * must be stated inside ()
	//no other part of RE other than that inside * shall use ()
	struct node a[1000];
	int i, ini=0, fi=0, count=0, l, ti=0, tf=0, br, cp=-1, ast=0, lb[1000], j, bk=-1;
	char c[100];
	for(i=0; i<1000; i++)
	{
		a[i].a=-1;
		a[i].b=-1;
		a[i].e=-1;
	}
	scanf("%s",c);
	l=strlen(c);
	for(i=0; i<=l; i++)
	{
		if(c[i]=='+')
		{
			if(bk==-1)
			{
				a[ti].e++;
				a[ti].n[2][a[ti].e]=fi;
				ti=ini;
				cp++;
			}
			else
			{
				a[ti].e++;
				a[ti].n[2][a[ti].e]=lb[bk];
				ti=lb[bk];
			}
		}
		if(c[i]=='.')
		{
			if(c[i-1]!='*')
			{
				ti=count;
			}
		}
		if(c[i]=='*')
		{
			a[ti].e++;
			a[ti].n[2][a[ti].e]=lb[ast];
			ti=lb[ast];
		}
		if(c[i]=='a'||c[i]=='b')
		{
			if(c[i]=='a')
			{
				a[ti].a++;
				count++;
				a[ti].n[0][a[ti].a]=count;
				if(cp==-1)
				{
					fi=count;
				}
			}
			else
			{
				a[ti].b++;
				count++;
				a[ti].n[1][a[ti].b]=count;
				if(cp==-1)
				{
					fi=count;
				}
			}
			ti=count;
		}
		if(c[i]=='(')
		{
			tf=ti;
			lb[ast]=tf;
			ast++;
			bk++;
		}
		if(c[i]==')')
		{
			a[ti].e++;
			a[ti].n[2][a[ti].e]=lb[bk];
			ti=lb[bk];
			ast--;
			bk--;
		}
		if(c[i]=='\0')
		{
			a[ti].e++;
			a[ti].n[2][a[ti].e]=fi;
		}
	}
	printf("node\ta\tb\tepsilon\n");
	for(i=0; i<=count; i++)
	{
		printf("%d\t",i);
		for(j=0; j<=a[i].a; j++)
			printf("%d,",a[i].n[0][j]);
		printf("\t");
		for(j=0; j<=a[i].b; j++)
			printf("%d,",a[i].n[1][j]);
		printf("\t");
		for(j=0; j<=a[i].e; j++)
			printf("%d,",a[i].n[2][j]);
		printf("\t");
		printf("\n");
	}
	printf("final state : %d",fi);
	return 0;
}