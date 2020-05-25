import abc
class CIMReport(abc.ABC):
    """
    Interface for CIM report.
    """
    @abc.abstractmethod
    def set_title(self, string):
        raise NotImplementedError()

    @abc.abstractmethod
    def add_statistics(self, string):
        raise NotImplementedError()

    @abc.abstractmethod
    def write(self, path):
        raise NotImplementedError()


    # All required methods goes here
    # . . .

