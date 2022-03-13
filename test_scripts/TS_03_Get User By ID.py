str1 = 'test_create_user.py::TestAPI_Adequateshop::test_002_DependentOntest_001'

str = 'test_create_user.py::TestAPI_Adequateshop::test_001'
def funName(fucntioname):
    lstr = fucntioname.split('::')
    fun = lstr[2]
    m = fun.find('Dependent')
    if m > 0:
        nam = fun[m + 11:]
    else:
        nam = fun
    return nam


print(funName(str1))
