#include <stdio.h> // for printf, scanf
#include <math.h> // for sqrt

//183880QF
//1001
int main()
{
	
	double square_roots [128 * 256]; // holds pointers to the square roots taken
	int nsquare_roots = 0; // holds the number of square roots that were taken
	
	unsigned long long number; // holds the actual numeric value of the number read in by scanf
	while (scanf("%ull", &number) != EOF)
	{
		square_roots[nsquare_roots++] = sqrt(number);
	}
	
	
	int k;
	for (k=nsquare_roots-1; k >= 0; k--){
		printf("%.4f\n", square_roots[k]);
	}
	
	
	/*
	int k;
	for (k=0; k < nsquare_roots;k++){
		printf("%.4f\n", square_roots[k]);
	}
	*/
	
	return 0;
}