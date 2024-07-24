import enum
import datetime

class progress(enum.Enum):
    ORDER_QUEUED = "Order queued."
    ORDER_PREPARING = "Order preparing."
    ORDER_DONE = "Order sendt."

class TeslaCarOrdering:
    __slots__ = "model","price","engine","self_driving"

    def __init__(self,model,price,engine):
        self.model = model
        self.price = price
        self.engine = engine
        self.self_driving = False


    def prepare_car(self,car):
        print(f"Started preparing car model: {car.model}")
        print(f"This will take about {car.preparation_time}.\nPick up {car.be_prepared}")


class TeslaBuilder:
    __slots__ = ()

    def __init__(self):
        self.order = CarOrdering("Tesla Model Y",70000,"1800 WAT", True)
        self.progress = progress.ORDER_QUEUED
        self.preparation_time = "About 50 or 60 days"
        self.be_prepared = self.get_prepared_time()
        
    def prepare_car(self):
        self.progress = progress.ORDER_PREPARING
        self.order.prepare_car(self)

    def get_prepared_time(self):
        current_date = datetime.datetime.now(tz=datetime.timezone.utc)
        prepared_time = current_date + datetime.timedelta(days=50)

        return prepared_time

        
