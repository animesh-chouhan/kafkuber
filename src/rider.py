import json


class Rider:
    def __init__(self, rider_id, rider_name, rider_assigned, rider_assigned_to, rider_latitude, rider_longitude):
        """Initialize the rider."""
        self.rider_id = rider_id
        self.rider_name = rider_name
        self.rider_assigned = rider_assigned
        self.rider_assigned_to = rider_assigned_to
        self.rider_latitude = rider_latitude
        self.rider_longitude = rider_longitude

    def __repr__(self):
        return json.dumps(self.__dict__)

    def get_rider_id(self):
        return self.rider_id

    def get_rider_name(self):
        return self.rider_name

    def get_rider_assigned(self):
        return self.rider_assigned

    def get_rider_assigned_to(self):
        return self.rider_assigned_to

    def get_rider_latitude(self):
        return self.rider_latitude

    def get_rider_longitude(self):
        return self.rider_longitude

    def set_rider_assigned(self, rider_assigned):
        self.rider_assigned = rider_assigned
        if rider_assigned == False:
            self.rider_assigned_to = None

    def set_rider_assigned_to(self, rider_assigned_to):
        self.rider_assigned_to = rider_assigned_to

    def set_rider_location(self, rider_latitude, rider_longitude):
        self.rider_latitude = rider_latitude
        self.rider_longitude = rider_longitude


if __name__ == "__main__":
    tuffy = Rider("r1213", "tuffy", True, "d1456", 75, 85)
    print(tuffy)
    tuffy.set_rider_assigned(False)
    tuffy.set_rider_location(45, 95)
    print(tuffy)
