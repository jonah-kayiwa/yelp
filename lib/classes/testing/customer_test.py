import pytest
from classes.many_to_many import Restaurant
from classes.many_to_many import Customer
from classes.many_to_many import Review

class TestCustomer:
    def __init__(self, first_name, last_name):
        if not isinstance(first_name, str) or len(first_name) > 25 or len(first_name) < 1:
            raise ValueError("First name must be a string between 1 and 25 characters")
        if not isinstance(last_name, str) or len(last_name) > 25 or len(last_name) < 1:
            raise ValueError("Last name must be a string between 1 and 25 characters")

        self.first_name = first_name
        self.last_name = last_name    

    """Customer in many_to_many.py"""

    def test_has_names(self):
        """Customer is initialized with first name and last name"""
        customer = Customer("Steve", "Wayne")
        assert customer.first_name == "Steve"
        assert customer.last_name == "Wayne"

    def test_names_are_mutable_strings(self):
        """names must be of type str and mutable"""
        customer_1 = Customer("Ned", "Stark")

        assert isinstance(customer_1.first_name, str)
        assert isinstance(customer_1.last_name, str)

        # comment out the next five lines if using Exceptions
        customer_1.first_name = "Rob"
        customer_1.last_name = 3
        customer_1.first_name = 3
        assert customer_1.first_name == "Rob"
        assert customer_1.last_name == "Stark"

        # uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     customer_1.last_name = 3

        # uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     customer_1.first_name = 3

    def test_names_are_valid(self):
        """first and last names must be between 1 and 25 characters, inclusive"""
        customer = Customer("Steve", "Wayne")

        assert 1 <= len(customer.first_name) <= 25
        assert 1 <= len(customer.last_name) <= 25

        # comment out the next four lines if using Exceptions
        customer.first_name = "F" * 26
        customer.first_name = ""
        customer.last_name = "F" * 26
        customer.last_name = ""
        assert customer.first_name == "Steve"
        assert customer.last_name == "Wayne"

        # uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     Customer('', 'Lastname')

        # uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     Customer('Firstname', '')

        # uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     Customer('F' * 26, 'Lastname')

        # uncomment the next two lines if using Exceptions
        # with pytest.raises(Exception):
        #     Customer('Firstname', 'L' * 26)

    def test_has_many_reviews(self):
        """customer has many reviews"""
        restaurant = Restaurant("Mels")
        customer = Customer("Steve", "Wayne")
        review_1 = Review(customer, restaurant, 2)
        review_2 = Review(customer, restaurant, 5)

        assert len(customer.reviews()) == 2
        assert review_1 in customer.reviews()
        assert review_2 in customer.reviews()

    def test_reviews_of_type_review(self):
        """reviews must be of type Review"""
        customer = Customer("Ned", "Stark")
        restaurant = Restaurant("Lento")
        Review(customer, restaurant, 5)
        Review(customer, restaurant, 2)

        assert isinstance(customer.reviews()[0], Review)
        assert isinstance(customer.reviews()[1], Review)

    def test_has_many_restaurants(self):
        """customer has many restaurants."""
        restaurant = Restaurant("Mels")
        restaurant_2 = Restaurant("Chipotle")
        restaurant_3 = Restaurant("Mel'b")
        customer = Customer("Steve", "Wayne")
        Review(customer, restaurant, 2)
        Review(customer, restaurant_2, 5)

        assert restaurant in customer.restaurants()
        assert restaurant_2 in customer.restaurants()
        assert restaurant_3 not in customer.restaurants()

    def test_restaurants_of_type_restaurant(self):
        """restaurants must of type Restaurant"""
        restaurant_1 = Restaurant("Mels")
        restaurant_2 = Restaurant("Chipotle")

        customer = Customer("Steve", "Wayne")
        Review(customer, restaurant_1, 2)
        Review(customer, restaurant_2, 5)

        assert isinstance(customer.restaurants()[0], Restaurant)
        assert isinstance(customer.restaurants()[1], Restaurant)

    def test_restaurants_unique(self):
        """customer restaurants are unique"""
        restaurant_1 = Restaurant("Mels")
        restaurant_2 = Restaurant("Chipotle")

        customer = Customer("Steve", "Wayne")
        Review(customer, restaurant_1, 2)
        Review(customer, restaurant_2, 5)
        Review(customer, restaurant_2, 3)

        assert len(set(customer.restaurants())) == len(customer.restaurants())
        assert len(customer.restaurants()) == 2
        assert restaurant_1 in customer.restaurants()
        assert restaurant_2 in customer.restaurants()

    def test_num_negative_reviews(self):
        """returns the total number of negative reviews by that customer"""
        restaurant_1 = Restaurant("Mels")
        restaurant_2 = Restaurant("Mel'b")
        customer_1 = Customer("Steve", "Wayne")
        customer_2 = Customer("Ned", "Stark")
        customer_3 = Customer("Sponge", "Bob")
        Review(customer_1, restaurant_1, 2)
        Review(customer_1, restaurant_2, 3)
        Review(customer_1, restaurant_1, 1)
        Review(customer_2, restaurant_2, 3)
        Review(customer_2, restaurant_1, 2)
        Review(customer_3, restaurant_1, 3)

        assert customer_1.num_negative_reviews() == 2
        assert customer_2.num_negative_reviews() == 1
        assert customer_3.num_negative_reviews() == 0

    def test_has_reviewed_restaurant(self):
        """returns True if the customer reviewed the restaurant, else False"""
        restaurant_1 = Restaurant("Mels")
        restaurant_2 = Restaurant("Mel'b")
        customer_1 = Customer("Steve", "Wayne")
        Review(customer_1, restaurant_1, 2)

        assert customer_1.has_reviewed_restaurant(restaurant_1) == True
        assert customer_1.has_reviewed_restaurant(restaurant_2) == False

    # def test_top_negative_reviewer(self):
        def num_negative_reviews(self):
          negative_reviews = 0
        for review in self.reviews:
            if review.rating <= 2:
                negative_reviews += 1
        return negative_reviews
        
    #     assert Customer.top_negative_reviewer() is None
        
    #     restaurant_1 = Restaurant("Mels")
    #     restaurant_2 = Restaurant("Mel'b")
    #     customer_1 = Customer('Steve', 'Wayne')
    #     customer_2 = Customer("Ned", "Stark")
    #     customer_3 = Customer("Sponge", "Bob")
        
    #     assert Customer.top_negative_reviewer() is None
        
    #     Review(customer_1, restaurant_2, 3)
        
    #     assert Customer.top_negative_reviewer() is None
        
    #     Review(customer_1, restaurant_1, 2)
    #     Review(customer_1, restaurant_1, 1)
    #     Review(customer_2, restaurant_2, 3)
    #     Review(customer_2, restaurant_1, 2)
    #     Review(customer_3, restaurant_1, 3)

    #     assert Customer.top_negative_reviewer() == customer_1