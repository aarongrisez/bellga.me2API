import importlib
import os

def extract_name_from_file(filename):
    """
    """
    return filename.replace(".py", "")

def construct_full_module_path(module_name, location):
    """
    """
    return os.path.dirname(location).split("./")[1].replace("/", ".") + f".{module_name}"

def get_module_import_path(file_path, location):
    module_name = extract_name_from_file(file_path)
    return {"name": module_name, "path": construct_full_module_path(module_name, location)}

def get_modules(location, comparator):
    files = os.listdir(os.path.dirname(location))
    return filter(
        lambda mod: comparator(mod["name"]),
        map(lambda file_path: get_module_import_path(file_path, location), files)
    )

def import_modules(modules):
    return {
        mod["name"]: importlib.import_module(mod["path"])
        for mod in modules 
    }

class AutoloadingContainer:

    def __init__(self, name):
        self.name = name
        self.registry = dict()

    def register(self, name, contents):
        self.registry[name] = contents
    
    def __getattr__(self, name):
        try:
            return self.registry[name]
        except KeyError:
            raise ValueError(f"Item {name} was not registered with AutoloadingContainer for {self.name}, {self}")

def get_initialization(name, location, comparator):

    def _(app):
        print(f"Starting autoload for {name}")
        container = AutoloadingContainer(name)
        modules = get_modules(location, comparator)
        imports = import_modules(modules)
        for mod_name, mod in imports.items():
            print(f"Autoloading {mod_name} into {name}")
            container.register(mod_name, mod)
            if hasattr(mod, "init"):
                print(f"Initializing {mod_name}")
                mod.init(app)
        setattr(app, name, container)
    
    return _