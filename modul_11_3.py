import inspect


def introspection_info(obj):
    about_obj = {}
    about_obj['type'] = type(obj).__name__
    list_attributes = dir(obj)
    methods_obj = []
    attributes_obj = []
    classes_obj = []
    for method in list_attributes:
        if callable(getattr(obj, method)):
            if isinstance(getattr(obj, method), type):
                classes_obj.append(method)
            else:
                methods_obj.append(method)
        else:
            attributes_obj.append(method)
    about_obj['attributes'] = attributes_obj
    about_obj['methods'] = methods_obj
    about_obj['classes'] = classes_obj
    try:
        about_obj['modul'] = inspect.getmodule(obj).__name__
    except AttributeError:
        about_obj['modul'] = '__main__'
    return about_obj


a = 42
number_info = introspection_info(a)
print(number_info)
