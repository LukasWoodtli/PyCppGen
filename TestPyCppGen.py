__author__ = 'Boot'

import os
import PyCppGen.PyCppGen as PyCpp
import PyCppGen.Program as p

output_path = os.path.split(__file__)[0]


program = p.Program(output_path)

myClass = PyCpp.CppClass("MyClass")
myMethod = PyCpp.CppMethod("myMethod", "void")
myClass.add_method(myMethod)


program.add_class(myClass)

program.gen_source_files()
