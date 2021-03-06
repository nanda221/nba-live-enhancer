import sys


class _const:
    class ConstError(TypeError):
        pass

    class ConstCaseError(ConstError):
        pass

    def __setattr__(self, name, value):
        if name in self.__dict__:
            raise self.ConstError("can not change const %s" % name)
        if not name.isupper():
            raise self.ConstCaseError("const name %s is not all upper" % name)
        self.__dict__[name] = value


sys.modules[__name__] = _const()


class Obj:
    def __init__(self):
        self.a = 1
