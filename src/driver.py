import json


class Driver:
    def __init__(self, driver_id, driver_name, driver_assigned, driver_assigned_to, driver_latitude, driver_longitude):
        """Initialize the driver."""
        self.driver_id = driver_id
        self.driver_name = driver_name
        self.driver_assigned = driver_assigned
        self.driver_assigned_to = driver_assigned_to
        self.driver_latitude = driver_latitude
        self.driver_longitude = driver_longitude

    def __repr__(self):
        return json.dumps(self.__dict__)

    def get_driver_id(self):
        return self.driver_id

    def get_driver_name(self):
        return self.driver_name

    def get_driver_assigned(self):
        return self.driver_assigned

    def get_driver_assigned_to(self):
        return self.driver_assigned_to

    def get_driver_latitude(self):
        return self.driver_latitude

    def get_driver_longitude(self):
        return self.driver_longitude

    def set_driver_assigned(self, driver_assigned):
        self.driver_assigned = driver_assigned
        if driver_assigned == False:
            self.driver_assigned_to = None

    def set_driver_assigned_to(self, driver_assigned_to):
        self.driver_assigned_to = driver_assigned_to

    def set_driver_location(self, driver_latitude, driver_longitude):
        self.driver_latitude = driver_latitude
        self.driver_longitude = driver_longitude


if __name__ == "__main__":
    tuffy = Driver("d1213", "tuffy", True, "r1456", 75, 85)
    print(tuffy)
    tuffy.set_driver_assigned(False)
    tuffy.set_driver_location(45, 95)
    print(tuffy)
