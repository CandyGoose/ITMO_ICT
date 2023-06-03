import abc # Python's built-in abstract class library

class QuackStrategyAbstract():
    """You do not need to know about metaclasses.
    Just know that this is how you define abstract
    classes in Python."""
    __metaclass__ = abc.ABCMeta
    @abc.abstractmethod

    def quack(self):
        """Required Method"""


class LoudQuackStrategy(QuackStrategyAbstract):
    def quack(self):
        print("QUACK! QUACK!!")

class GentleQuackStrategy(QuackStrategyAbstract):
    def quack(self):
        print("quack!")



class LightStrategyAbstract():
    __metaclass__ = abc.ABCMeta

    @abc.abstractmethod
    def lights_on(self):
        """Required Method"""


class OnForTenSecondsStrategy(LightStrategyAbstract):
    def lights_on(self):
        print("Lights on for 10 seconds")
