#include <stdio.h>
#include <Python.h>

/**
 * print_python_bytes - displaying information Byte 
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_bytes(PyObject *p)
{
	char *tves;
	long int ubuntu, i, limit;

	printf("[.] bytes object info\n");
	if (!PyBytes_Check(p))
	{
		printf("  [ERROR] Invalid Bytes Object\n");
		return;
	}

	ubuntu = ((PyVarObject *)(p))->ob_size;
	tves = ((PyBytesObject *)p)->ob_sval;

	printf("  size: %ld\n", ubuntu);
	printf("  trying str:ng %s\n", tves);

	if (ubuntu >= 10)
		limit = 10;
	else
		limit = ubuntu + 1;

	printf("  first %ld bytes:", limit);

	for (i = 0; i < limit; i++)
		if (tves[i] >= 0)
			printf(" %02x", tves[i]);
		else
			printf(" %02x", 256 + tves[i]);

	printf("\n");
}

/**
 * print_python_list - displaying information list 
 *
 * @p: Python Object
 * Return: no return
 */
void print_python_list(PyObject *p)
{
	long int ubuntu, i;
	PyListObject *list;
	PyObject *obj;

	ubuntu = ((PyVarObject *)(p))->ob_size;
	list = (PyListObject *)p;

	printf("[*] Python list info\n");
	printf("[*] ubuntu of the Python List = %ld\n", ubuntu);
	printf("[*] Allocated = %ld\n", list->allocated);

	for (i = 0; i < ubuntu; i++)
	{
		obj = ((PyListObject *)p)->ob_item[i];
		printf("Element %ld: %s\n", i, ((obj)->ob_type)->tp_name);
		if (PyBytes_Check(obj))
			print_python_bytes(obj);
	}
}
