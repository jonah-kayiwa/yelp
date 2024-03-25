import pytest
from classes.many_to_many import Restaurant
from classes.many_to_many import Customer
from classes.many_to_many import Review

class TestReview:
    """Review in many_to_many.py"""

    def test_has_rating(self):
        """Review is initialized with a rating"""
        restaurant = Restaurant("Mels")
        customer = Customer("Steve", "Wayne")
        review_1 = Review(customer, restaurant, 2)
        review_2 = Review(customer, restaurant, 5)

        assert review_1.rating == 2
        assert review_2.rating == 5

    def test_rating_is_immutable(self):
        """rating is immutable"""
        restaurant = Restaurant("Mels")
        customer = Customer("Steve", "Wayne")
        review_1 = Review(customer, restaurant, 2)

        # comment out the next two lines if using Exceptions
        review_1.rating = 1
        assert review_1.rating == 2

        # uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     review_1.rating = 4

    def test_rating_is_valid_int(self):
        """rating must be of type int and between 1 and 5"""
        restaurant = Restaurant("Mels")
        customer = Customer("Steve", "Wayne")
        review_1 = Review(customer, restaurant, 4)

        assert isinstance(review_1.rating, int)
        assert 1 <= review_1.rating <= 5

        # uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     Review(customer, restaurant, 0)

        # uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     Review(customer, restaurant, 6)

        # uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     Review(customer, restaurant, "4")

    def test_has_a_customer(self):
        """review has a customer"""
        restaurant = Restaurant("Mels")
        customer = Customer("Steve", "Wayne")
        review_1 = Review(customer, restaurant, 2)
        review_2 = Review(customer, restaurant, 5)

        assert review_1.customer == customer
        assert review_2.customer == customer

    def test_customer_of_type_customer_and_mutable(self):
        """customer must be of type Customer and mutable"""

        restaurant = Restaurant("Mels")
        customer_1 = Customer("Steve", "Wayne")
        customer_2 = Customer("Steve", "Jobs")
        review_1 = Review(customer_1, restaurant, 2)
        review_2 = Review(customer_1, restaurant, 5)

        # comment out next line if using Exceptions
        review_1.customer = "Casper"

        assert isinstance(review_1.customer, Customer)
        assert isinstance(review_2.customer, Customer)
        assert review_1.customer == customer_1
        
        review_1.customer = customer_2
        assert review_1.customer.last_name == "Jobs"
        assert isinstance(review_2.customer, Customer)

        # uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     Review("Johnny", restaurant, 5)

    def test_has_a_restaurant(self):
        """review has a restaurant"""
        restaurant = Restaurant("Mels")
        customer = Customer("Steve", "Wayne")
        customer_2 = Customer("Dima", "Bay")
        review_1 = Review(customer, restaurant, 2)
        review_2 = Review(customer_2, restaurant, 5)

        assert review_1.restaurant == restaurant
        assert review_2.restaurant == restaurant

    def restaurant_of_type_restaurant_and_mutable(self):
        """restaurant must be of type Restaurant and mutable"""
        restaurant_1 = Restaurant("Mels")
        restaurant_2 = Restaurant("Moms")
        customer = Customer("Steve", "Wayne")
        review_1 = Review(customer, restaurant_1, 2)
        review_2 = Review(customer, restaurant_2, 5)

        assert isinstance(review_1.restaurant, Restaurant)
        assert isinstance(review_2.restaurant, Restaurant)

        review_1.restaurant = restaurant_2
        assert review_1.restaurant.name == "Moms"
        assert isinstance(review_2.restaurant, Restaurant)

        # uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     Review(customer, "Da Giovanni", 5)

    def test_has_all_property(self):
        """Review class has an all property"""
        Review.all = []
        restaurant = Restaurant("Mels")
        customer = Customer("Steve", "Wayne")
        review_1 = Review(customer, restaurant, 2)
        review_2 = Review(customer, restaurant, 5)

        assert len(Review.all) == 2
        assert review_1 in Review.all
        assert review_2 in Review.all