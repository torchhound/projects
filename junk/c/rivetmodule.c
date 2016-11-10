#include <Python.h>

/*this module adds support for multi-dimensional arrays and switch case statements.*/

static PyObject *rivetMultAr;
static PyObject *rivetSwitch;

void arArgsParser(long arr[],Py_ssize_t size, PyObject *args) /*parses rivet_mult_ar arguments*/
{
	Py_ssize_t i;
	char typeArgs[];
	char arrayArgs[];
	do
	{
		if (PyObject *args = int)
		{
			typeArgs[0] = int
		}
		else if (PyObject *args = char)
		{
			typeArgs[0] = char
		}
		else if (PyObject *args = float)
		{
			typeArgs[0] = float
		}
		else if (PyObject *args = double)
		{
			typeArgs[0] = double
		}
		else if (PyObject *args = long)
		{
			typeArgs[0] = long	
		}
		else() /*differentiate x from y*/
		{
			/*add to arrayArgs*/
		}
	}while(arr[i] != NULL);
	/*all code remaining in function is leftover and will be eliminated*/
	Py_ssize_t i;
    PyObject *temp1, *temp2;

    for (i=0;i<size;i++) {
        temp1 = PyTuple_GetItem(args,i);
        if(temp1 == NULL) 
		{
			return NULL;
		}

        /* Check if temp1 is numeric */
        if (PyNumber_Check(temp1) != 1) {
            PyErr_SetString(PyExc_TypeError,"Non-numeric argument.");
            return NULL;
        }

        /* Convert number to python long and than C unsigned long */
        temp2 = PyNumber_Long(temp_p);
        arr[i] = PyLong_AsUnsignedLong(temp2);
        Py_DECREF(temp2);
    }
}

void switchArgsParser(long arr[],Py_ssize_t size, PyObject *args) /*parses rivet_switch arguments*/
{
	Py_ssize_t i;
	char switchVar[];
	char caseVar[];
	do
	{
		for (x in arr[i]; arr[i] != NULL; x++;) /*iterate over list*/
			if (x = 0) /*first arg is switch variable*/
			{
				switchVar[0] = arr[0]; /*add first arg to switchVar[]*/
			}
			else()
			{
				caseVar[]; /*add all other args to caseVar[]*/
			}
	}while(arr[i] != NULL);
	/*all code remaining in function is leftover and will be eliminated*/
	Py_ssize_t i;
    PyObject *temp1, *temp2;

    for (i=0;i<size;i++) {
        temp1 = PyTuple_GetItem(args,i);
        if(temp1 == NULL) 
		{
			return NULL;
		}

        /* Check if temp1 is numeric */
        if (PyNumber_Check(temp1) != 1) {
            PyErr_SetString(PyExc_TypeError,"Non-numeric argument.");
            return NULL;
        }

        /* Convert number to python long and than C unsigned long */
        temp2 = PyNumber_Long(temp_p);
        arr[i] = PyLong_AsUnsignedLong(temp2);
        Py_DECREF(temp2);
    }
}

rivetMultAr(PyObject *self, PyObject *args) /*add argument for arrays other than int*/
{
	arArgsParser(PyObject *args);
	int multArray[x][y] = {
	
	};
}

rivetSwitch(PyObject *self, PyObject *args) /*first argument is switch variable all other arguments are different cases*/
{
	switch(switchArgsParser(PyObject *args)){
		/*loop for number of cases?*/
		case(switchArgsParser(PyObject *args)):
		{
			
		}
	}
}

static PyMethodDef rivetMethods[] = {
    ...
    {"switch",  rivetSwitch, METH_VARARGS,
     "switch case statement"},
	 {"mult_ar",  rivetMultAr, METH_VARARGS,
     "multi-dimensional array"},
    ...
    {NULL, NULL, 0, NULL}       
};

PyMODINIT_FUNC
initRivet(void)
{
	PyObject *r;

    r = Py_InitModule("rivet", rivetMethods);
    if (r == NULL)
        return;

    rivetError = PyErr_NewException("rivet.error", NULL, NULL);
    Py_INCREF(rivetError);
    PyModule_AddObject(r, "error", rivetError);
}