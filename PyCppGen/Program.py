__author__ = 'Boot'
import os


class Program:
    def __init__(self, sourceDirectory, prefix=""):
        self.classes = []
        self.sourceDir = sourceDirectory
        self.prefix = prefix

    def add_class(self, klass):
        self.classes.append(klass)

    def gen_source_files(self):
        if not os.path.exists(self.sourceDir):
            os.makedirs(self.sourceDir)
        for klass in self.classes:
            baseName = os.path.join(self.sourceDir, self.prefix + klass.file_name)
            with open(baseName + ".hpp", 'w') as hppFile:
                hppFile.write(klass.generate_header_code())
            with open(baseName + ".cpp", 'w') as cppFile:
                cppFile.write(klass.generate_implementation_code(self.prefix))
