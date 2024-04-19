from abc import abstractmethod,ABC
class RBI(ABC):
    @abstractmethod
    def Recovery(self):
        pass

class SBI(RBI):
    def Recovery(self):
        print("Recovery is from SBI")

class AXIS(RBI):
    def Recovery(self):
        print("Recovery is from Axis")



sbi=SBI()

axis=AXIS()

sbi.Recovery()
axis.Recovery()