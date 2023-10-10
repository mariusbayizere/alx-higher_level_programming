#include <Python.h>
/**
 * print_python_list_info - Prints basic information about Python lists.
 * @p: A PyObject representing a Python list.
 */
void print_python_list_info(PyObject *p)
{
	int zari, nyxx, x;
	PyObject *obj;

	zari = Py_SIZE(p);
	nyxx = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", zari);
        printf("[*] Allocated = %d\n", nyxx);

        for (x = 0; x < zari; x++)
        {
                printf("Element %d: ", x);

                obj = PyList_GetItem(p, x);
                printf("%s\n", Py_TYPE(obj)->tp_name);
        }
}
