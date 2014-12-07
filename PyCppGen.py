
# from: http://stackoverflow.com/a/1695250
def enum(**enums):
    return type('Enum', (), enums)

Visibility = enum(PUBLIC=0, PROTECTED=1, PRIVATE=2)
Virtuality = enum(NON_VIRTUAL=0, VIRTUAL=1, PURE_VIRTUAL=2)
Modifier   = enum(NONE=0, CONST=1, STATIC=2)


TEMPLATE_HPP = \
"""// generated by PyCppGen

%INCLUDES%

%FORWARD_DECLARATIONS%

class %CLASS_NAME% %PARENT_CLASSES%
{
 // Constructors and Destructors
public:
    %PUBLIC_CTORS%

    %PUBLIC_DTORS%
protected:
    %PROTECTED_CTORS%

    %PROTECTED_DTORS%
private:
    %PRIVATE_CTORS%

    %PRIVATE_DTORS%

  // Overloaded Operators
public:
    %PUBLIC_OPERATOS%

protected:
    %PROTECTED_OPERATORS%

private:
    %PRIVATE_OPERATORS%

  // Methods (Member Functions)
public:
    %PUBLIC_METHODS%

protected:
    %PROTECTED_METHODS%

private:
    %PRIVATE_METHODS%

// Member Variables
public:
    %PUBLIC_MEMBERS%

protected:
    %PROTECTED_MEMBERS%

private:
    %PRIVATE_MEMBERS%
};

// Related Non-Members

%RELATED_NON_MEMBERS%

"""

class CppMemberVar:
    def __init__(self, type, name, const=False, static=False):
        self.type = type
        self.name = name
        self.const = const
        self.static = static

    def generate_header_code(self):
        str = ""
        if self.static:
            str += "static "
        if self.const:
            str += "const "

        str += self.type + " " + self.name + ";"
        return str


class CppFunction:
    def __init__(self, name,
                 returnType,
                 arguments,
                 code=""):
        self.name = name
        self.returnType = returnType
        self.arguments = arguments

    def generate_common_code(self):
        return self.returnType + " " + self.name + "(" + self.arguments + ")"

    def generate_header_code(self):
        return self.generate_common_code() + ";\n"


    def generate_implementation_code(self):
        str = self.generate_common_code() + " {\n"
        str += self.code
        str += "\n}\n"
        return str



class CppMethod(CppFunction):
    def __init__(self,
                 visibility=Visibility.PUBLIC,
                 virtuality=Virtuality.NON_VIRTUAL,
                 modifier=Modifier.NONE, *args, **kwargs):
        super(CppMethod, self).__init__(*args, **kwargs)
        self.visibility = visibility
        self.virtuality = virtuality
        self.modifier = modifier



    def generate_common_code(self):
        return self.returnType + " " + self.name + "(" + self.arguments + ")"

    def generate_header_code(self):
        str = ""
        if self.virtuality != Virtuality.NON_VIRTUAL:
            str += "virtual "
        elif self.modifier == Modifier.STATIC:
            str += "static "

        str += self.generate_common_code()
        if self.modifier == Modifier.CONST:
            str += " const "
        if self.virtuality == Virtuality.PURE_VIRTUAL:
            str += " = 0"
        str += ";\n"
        return str


    def generate_implementation_code(self):
        str = ""
        # add className::
        str += self.generate_common_code()
        if self.modifier == Modifier.CONST:
            str += " const "
        if self.virtuality == Virtuality.PURE_VIRTUAL:
            str += " = 0"
        str += "{\n"
        str += self.code
        str += "\n}\n"
        return str





class CppParentClass:
    def __init__(self, classObj, visibility=Visibility.PUBLIC, virtuality=Virtuality.NON_VIRTUAL):
        self.classObj = classObj
        self.visibility = visibility
        self.virtuality = virtuality

    def generate_header_code(self):
        str += self.visibility.__repr__().toLower()
        if self.virtuality == Virtuality.VIRTUAL:
            str += " virtual"
        str += " " + self.classObj


class CppClass:
    def __init__(self, name, *parents):
        self.name = name
        self.parents = []
        for parent in parents:
            self.parents.append(parent)
        self.includes = []
        self.methods = []
        self.related_functions = []
        self.members = []

    def add_includes(self, *includes):
        for include in includes:
            self.includes.append(include)

    def add_forward_declarations(self, *forward_declarations):
        for forward_declaration in forward_declarations:
            self.forward_declarations.append(forward_declaration)

    def add_parent(self, name):
        self.parents.append(name)

    def add_method(self, method):
        self.methods.append(method)

    def add_related_function(self, function):
        self.related_functions.append(function)

    def add_member_var(self, member):
        self.members.append(member)
