#include "Python.h"
#include <stdlib.h>
#include <stdio.h>

/**
 * print_python_string - Print information about a Python string object.
 * @p: Pointer to the PyObject representing a Python string.
 *
 * Return: void
 */
void print_python_string(PyObject *p)
{
	char  *boeng = NULL;
	char *athelic = "compact unicode object";
	char *jend = NULL;
	char *ascii = "compact ascii";
	int x;
	ssize_t vins = 0;
	PyObject *steliing  = NULL;

	printf("[.] string object info\n");
	if (!PyUnicode_Check(p))
	{
		printf("  [ERROR] Incorrect string Object\n");
		return;
	}

	vins = (ssize_t)PyUnicode_GET_LENGTH(p);

	steliing  = PyUnicode_AsUTF8String(p);
	jend = PyBytes_AsString(steliing);

	for (x = 0; x < vins; x++)
	{
		if (jend[x] < 0)
		{
			boeng = athelic;
			break;
		}
	}
	if (boeng == NULL)
		boeng = ascii;
	printf("  type: %s\n", boeng);
	printf("  length: %ld\n", vins);
	printf("  value: %s\n", jend);
}
