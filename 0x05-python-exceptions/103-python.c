#include <Python.h>

/**
* print_python_list - Prints information about a Python list object.
* @p: The PyObject representing the Python list.
*/
void print_python_list(PyObject *p)
{
Py_ssize_t size, i;
PyObject *item;
const char *type;

printf("[*] Python list info\n");

if (!PyList_Check(p))
{
printf("  [ERROR] Invalid List Object\n");
return;
}

size = PyList_Size(p);
printf("[*] Size of the Python List = %ld\n", size);

printf("[*] Allocated = %ld\n", ((PyListObject *)p)->allocated);

for (i = 0; i < size; i++)
{
item = PyList_GetItem(p, i);
type = item->ob_type->tp_name;

printf("Element %ld: %s\n", i, type);

if (PyBytes_Check(item))
print_python_bytes(item);
else if (PyFloat_Check(item))
print_python_float(item);
}
}

/**
* print_python_bytes - Prints information about a Python bytes object.
* @p: The PyObject representing the Python bytes.
*/
void print_python_bytes(PyObject *p)
{
Py_ssize_t size, i;
char *str;

printf("[.] bytes object info\n");

if (!PyBytes_Check(p))
{
printf("  [ERROR] Invalid Bytes Object\n");
return;
}

size = PyBytes_Size(p);
str = PyBytes_AsString(p);

printf("  size: %ld\n", size);
printf("  trying string: %s\n", str ? str : "(null)");

if (size < 10)
printf("  first %ld bytes: ", size + 1);
else
printf("  first 10 bytes: ");

for (i = 0; i < size && i < 10; i++)
printf("%02x ", (unsigned char)str[i]);

printf("\n");
}

/**
* print_python_float - Prints information about a Python float object.
* @p: The PyObject representing the Python float.
*/
void print_python_float(PyObject *p)
{
double value;

printf("[.] float object info\n");

if (!PyFloat_Check(p))
{
printf("  [ERROR] Invalid Float Object\n");
return;
}

value = PyFloat_AsDouble(p);
printf("  value: %f\n", value);
}
