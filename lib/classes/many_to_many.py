class NationalPark:
    all = []

    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 3:
            raise ValueError("Name must be a string with at least 3 characters")
        self._name = name
        NationalPark.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        
        if hasattr(self, "_name"):
            return  

    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]

    def visitors(self):
        return list({trip.visitor for trip in self.trips()})

    def total_visits(self):
        return len(self.trips())

    def best_visitor(self):
        from collections import Counter
        visitors = [trip.visitor for trip in self.trips()]
        if not visitors:
            return None
        return Counter(visitors).most_common(1)[0][0]

    @classmethod
    def most_visited(cls):
        if not cls.all:
            return None
        return max(cls.all, key=lambda park: park.total_visits())
class Visitor:
    all = []

    def __init__(self, name):
        if not isinstance(name, str):
            raise TypeError("Name must be a string")
        if not (1 <= len(name) <= 15):
            raise ValueError("Name must be 1-15 characters")
        self._name = name
        Visitor.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 15:
            self._name = value

    # Make sure this method is properly indented at the class level
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]

    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})

    def total_visits_at_park(self, park):
        return sum(1 for trip in self.trips() if trip.national_park == park)

class Trip:
    all = []

    def __init__(self, visitor, national_park, start_date, end_date):
        if not isinstance(visitor, Visitor):
            raise TypeError("visitor must be a Visitor instance")
        if not isinstance(national_park, NationalPark):
            raise TypeError("national_park must be a NationalPark instance")
        if not isinstance(start_date, str) or len(start_date) < 7:
            raise ValueError("start_date must be string length >= 7")
        if not isinstance(end_date, str) or len(end_date) < 7:
            raise ValueError("end_date must be string length >= 7")

        self._visitor = visitor
        self._national_park = national_park
        self._start_date = start_date
        self._end_date = end_date
        Trip.all.append(self)

    @property
    def visitor(self):
        return self._visitor

    @property
    def national_park(self):
        return self._national_park

    @property
    def start_date(self):
        return self._start_date

    @start_date.setter
    def start_date(self, value):
        # Only update if value is a valid string of length >= 7
        if isinstance(value, str) and len(value) >= 7:
            self._start_date = value

    @property
    def end_date(self):
        return self._end_date

    @end_date.setter
    def end_date(self, value):
        # Only update if value is a valid string of length >= 7
        if isinstance(value, str) and len(value) >= 7:
            self._end_date = value

class Result:
    all = []

    def __init__(self, player, game, score):
        from classes.many_to_many import Player, Game  # only if needed

        if not isinstance(player, Player):
            raise TypeError("player must be a Player instance")
        if not isinstance(game, Game):
            raise TypeError("game must be a Game instance")
        if not isinstance(score, int) or score < 1 or score > 5000:
            raise ValueError("score must be int between 1-5000")

        self._player = player
        self._game = game
        self._score = score
        Result.all.append(self)

    @property
    def score(self):
        return self._score

    @property
    def player(self):
        return self._player

    @property
    def game(self):
        return self._game