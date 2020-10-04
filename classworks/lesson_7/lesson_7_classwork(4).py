from abc import ABC, abstractmethod

class SomeInterFace(ABC):

    @property
    @abstractmethod
    def get_name(self, a:int, b:str) -> int:
        pass

    @abstractmethod
    def get_idx(self):
        pass

class Some(SomeInterFace):
    def __init__(self, name):
        self.name = name
        self.idx = 0

    def get_idx(self):
        return 0

    def get_name(self):
        return self.name

if __name__ == '__main__':
    some = Some('NAME')