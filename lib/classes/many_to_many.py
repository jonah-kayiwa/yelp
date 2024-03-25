class Customer:
    all = []

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.all.append(self)

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._first_name = value

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._last_name = value

    def reviews(self):
        return [review for review in Review.all if review.customer == self]

    def restaurants(self):
        return list(set([review.restaurant for review in self.reviews()]))

    def num_negative_reviews(self):
        return len([review for review in self.reviews() if review.rating <= 2])

    def has_reviewed_restaurant(self, restaurant):
        return any(review.restaurant == restaurant for review in self.reviews())


class Restaurant:
    all = []

    def __init__(self, name):
        self.name = name
        self.all.append(self)

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and 1 <= len(value) <= 25:
            self._name = value

    def reviews(self):
        return [review for review in Review.all if review.restaurant == self]

    def customers(self):
        return list(set([review.customer for review in self.reviews()]))

    def average_star_rating(self):
        ratings = [review.rating for review in self.reviews()]
        if not ratings:
            return 0.0
        return round(sum(ratings) / len(ratings), 1)

    @classmethod
    def top_two_restaurants(cls):
        sorted_restaurants = sorted(
            cls.all,
            key=lambda restaurant: restaurant.average_star_rating(),
            reverse=True
        )
        return sorted_restaurants[:2]


class Review:
    all = []

    def __init__(self, customer, restaurant, rating):
        # if not isinstance(customer, Customer):
        #     raise TypeError("Customer must be an instance of Customer")
        # if not isinstance(restaurant, Restaurant):
        #     raise TypeError("Restaurant must be an instance of Restaurant")
        # if not isinstance(rating, int):
        #     raise TypeError("Rating must be an integer")
        # if not 1 <= rating <= 5:
        #     raise ValueError("Rating must be between 1 and 5")
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        Review.all.append(self)
    
    def get_rating(self):
        return self._rating
    def set_rating(self, val):
        if isinstance(val, int) and 1 <= val <= 5 and not hasattr(self, '_rating'):
            self._rating = val
    rating = property(get_rating, set_rating)


    
    def get_customer(self):
        return self._customer
    def set_customer(self, val):
        if isinstance(val, Customer):
            self._customer = val
    customer = property(get_customer, set_customer)
    @property
    def restaurant(self):
        return self._restaurant

    @property
    def rating(self):
        return self._rating