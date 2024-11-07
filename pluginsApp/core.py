from abc import ABC, abstractmethod

class PluginBase(ABC):
    @abstractmethod
    def get_notifications(self, user):
        pass
