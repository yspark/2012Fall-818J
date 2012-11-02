#include <stdio.h>

int sizeofarray(int array[])
{
	printf("0:%d 1:%d\n", array[0], array[1]);

	return sizeof(*array);
}

int main(void)
{
	int array[10];

	array[0] = 10;
	array[1] = 1;
	
	printf("%d\n", sizeof(array));		
	

	printf("function %d\n", sizeofarray(array));

	return 0;
}
