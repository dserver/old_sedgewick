#include <stdio.h>
#include <math.h>

void insertion_sort(int *a, int len);
//void print_array(int* a, int len);

int main()
{
	int stones [20];
	int n_stones = 0;
	int stone;
	scanf("%d", &n_stones);
	
	int k=0;
	while (scanf("%d", &stone) != EOF){ stones[k++] = stone; }
	
	insertion_sort(stones, n_stones);
	//print_array(stones, n_stones);
	int p1 = stones[n_stones-1];
	int p2 = 0;
	int y;
	for (y = 0; y < n_stones-1; y++){
		p2 += stones[y];
	}
	
	y = 0;
	while (p1 < p2 && stones[y] < p2-p1){
		//printf("p1: %d   p2: %d\n", p1, p2);
		p1 += stones[y];
		p2 -= stones[y];
		y++;
	}
	
	printf("%d\n", abs(p2-p1));
	
	return 0;
}

void insertion_sort(int *a, int len)
{
	if (len < 2)
	{
		return;
	}
	
	int x;
	for (x = 1; x < len; x++){
		int j = x - 1;
		int insert_val = a[x];
		while (j >= 0 && a[j] > insert_val){
			a[j+1] = a[j];
			j--;
		}
		a[j+1] = insert_val;
	}
	
	return;
}

void print_array(int* a, int len)
{
	int i;
	for (i = 0; i < len; i++)
	{
		printf("%2d: %2d    ", i, a[i]);
	}
	
	printf("\n");
	
	return;
}