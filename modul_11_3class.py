import inspect


def introspection_info(obj):
    class Inspectors():
        def __init__(self):
            self.typ = type(obj).__name__
            self.attributes = []
            self.methods = []
            self.classes = []
            info_list = dir(obj)
            for fact in info_list:
                if callable(getattr(obj, fact)):
                    if isinstance(getattr(obj, fact), type):
                        self.classes.append(fact)
                    else:
                        self.methods.append(fact)
                else:
                    self.attributes.append(fact)
            try:
                self.modul = inspect.getmodule(obj).__name__
            except AttributeError:
                self.modul = '__main__'

        def release(self):
            return {
                'type': self.typ,
                'classes': self.classes,
                'atributes': self.attributes,
                'methods': self.methods,
                'modul': self.modul
            }

    inspector = Inspectors()
    return inspector.release()


number_info = introspection_info(42)
print(number_info)
