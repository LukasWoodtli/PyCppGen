
# from: http://stackoverflow.com/a/1695250
def enum(**enums):
    return type('Enum', (), enums)

Visibility = enum(PUBLIC=0, PROTECTED=1, PRIVATE=2)
Virtuality = enum(NON_VIRTUAL=0, VIRTUAL=1, PUREVIRTUAL=2)
Modifier   = enum(NONE=0, CONST=1, STATIC=2)

class CppMemberVar:
    def __init__(self, type, name, const=False, static=False):
        self.type = type
        self.name = name
        self.const = const
        self.static = static


class CppMethod:
    def __init__(self, name,
                 returnType,
                 arguments,
                 visibility=Visibility.PUBLIC,
                 virtuality=Virtuality.NON_VIRTUAL,
                 modifier=Modifier.NONE,
                 code=""):
        self.name = name
        self.returnType = returnType
        self.arguments = arguments
        self.visibility = visibility
        self.virtuality = virtuality
        self.modifier = modifier
        self.code = code


class CppParentClass:
    def __init__(self, classObj, visibility=Visibility.PUBLIC, virtuality=Virtuality.NON_VIRTUAL):
        self.classObj = classObj
        self.visibility = visibility
        self.virtuality = virtuality

class CppClass:
    def __init__(self, name, *parents):
        self.name = name
        self.parents = []
        for parent in parents:
            self.parents.append(parent)
        self.methods = []
        self.members = []

    def add_parent(self, name):
        self.parents.append(name)

    def add_method(self, method):
        self.methods.append(method)

    def add_member_var(self, member):
        self.members.append(member)
