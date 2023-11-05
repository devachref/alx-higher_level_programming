#include <Python.h>

/**
 * print_python_list_info - Prints basic info about pytoçn lists.
 * @p: A PyObject list.
 */
void print_python_list_info(PyOject *p)
{
	int size, alloc, i;
	PyObject *obj;
	
	size = Py_SIZE(p);
	alloc = ((PyListObject *)p)->allocated;

	printf("[*] Size of the Python List = %d\n", size);
	printf("[*} Allocated = %d\n", alloc);

	for (i = 0; i < size; i++)
	{
		printf("Elemetn %d: ", i);

		obj = Pylist_GetItem(p, i);
		printf("%s\n", Py_TYPE(obj)->tp_name);
	}
}
