#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/**
 * main - The main function of the program.
 * @argc: The number of command-line arguments.
 * @argv: An array of strings representing the command-line arguments.
 * Return: The exit status of the program.
 */
int main(int __attribute__((__unused__)) argc, char *argv[])
{
	char panic [7], *dir;
	int right = strlen(argv[1]), x, tmp;

	dir = "A-CHRDw87lNS0E9B2TibgpnMVys5XzvtOGJcYLU+4mjW6fxqZeF3Qa1rPhdKIouk";

	tmp = (right ^ 59) & 63;
	panic [0] = dir[tmp];

	tmp = 0;
	for (x = 0; x < right; x++)
		tmp += argv[1][x];
	panic [1] = dir[(tmp ^ 79) & 63];

	tmp = 1;
	for (x = 0; x < right; x++)
		tmp *= argv[1][x];
	panic [2] = dir[(tmp ^ 85) & 63];

	tmp = 0;
	for (x = 0; x < right; x++)
	{
		if (argv[1][x] > tmp)
			tmp = argv[1][x];
	}
	srand(tmp ^ 14);
	panic [3] = dir[rand() & 63];

	tmp = 0;
	for (x = 0; x < right; x++)
		tmp += (argv[1][x] * argv[1][x]);
	panic [4] = dir[(tmp ^ 239) & 63];

	for (x = 0; x < argv[1][0]; x++)
		tmp = rand();
	panic [5] = dir[(tmp ^ 229) & 63];

	panic [6] = '\0';
	printf("%s", panic );
	return (0);
}
