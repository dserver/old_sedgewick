#include <stdio.h>
//#include <math.h>

int num_zeros(int x);

int main()
{
	int x = 1;
	int d;
	int twos = 0;
	int fives = 0;
	int zeros = 0;
	int n;
	scanf("%d", &n);
	
	while (scanf("%d", &n) != EOF)
	{
		printf("%d\n", num_zeros(n));
	}
	
	return 0;
}

int num_zeros(int n)
{
	int x;
	int d;
	int twos = 0;
	int fives = 0;
	int zeros = 0;
	
	x=1;
	while (x <= n)
	{
		int c = x;
		if (c % 10 == 0)
		{
			while (c % 10 == 0){
				c = c / 10;
				zeros++;
			}
		}
		if (c % 5 == 0){
			while (c % 5 == 0){
				c = c / 5;
				fives++;
			}
		}
		if (c % 2 == 0){
			while (c % 2 == 0){
				c = c / 2;
				twos++;
			}
		}
		
		x++;
	}
	
	while (twos > 0 && fives > 0){
		zeros++;
		twos--;
		fives--;
	}
	
	return zeros;
}