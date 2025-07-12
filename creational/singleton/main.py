class Singleton():
    _instance = None

    def __new__(cls, *args, **kwargs):
        if Singleton._instance:
            return Singleton._instance

        Singleton._instance = super(Singleton, cls).__new__(cls)
        return Singleton._instance

    def __init__(self):
        print('init has call ...')

    def __add__(self, other):
        print('add has call ...')

    def __mul__(self, other):
        print('mul has call ...')


instance1 = Singleton()
instance2 = Singleton()

instance1 + instance2
instance1 * instance2

print(id(instance1))
print(id(instance2))

print(instance1 is instance2)

