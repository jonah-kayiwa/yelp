#lets Import necessary libraries
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

#Define the base class for our ORM models
Base = declarative_base()

#Customer class representing a customer who writes reviews
class Customer(Base):

#Define the table name in the databas    
    __tablename__ = "customers" 

#here, we define table columns
#Unique identifier for each customer    
    id = Column(Integer, primary_key=True) 
#Customer's first name (not null)    
    first_name = Column(String(25), nullable=False) 
 # Customer's last name (not null)
    last_name = Column(String(25), nullable=False) 

#Define the relationship between Customer and Review models (one-to-many)
# Customer can have many reviews    
    reviews = relationship("Review", backref="customer")  

#Initialize a customer object with first and last name validation
    def __init__(self, first_name, last_name):
        if not isinstance(first_name, str) or len(first_name) > 25 or len(first_name) < 1:
            raise ValueError("First name must be a string between 1 and 25 characters")
        if not isinstance(last_name, str) or len(last_name) > 25 or len(last_name) < 1:
            raise ValueError("Last name must be a string between 1 and 25 characters")

        self.first_name = first_name
        self.last_name = last_name

#Method to calculate the number of negative reviews written by the customer
    def num_negative_reviews(self):
        negative_reviews = 0
#Iterate through customer's reviews        
        for review in self.reviews:
#Check if rating is negative (1 or 2)              
            if review.rating <= 2:  
                negative_reviews += 1
        return negative_reviews

#Method to check if a customer has reviewed a specific restaurant
    def has_reviewed_restaurant(self, restaurant):
 #Iterate through customer's reviews        
        for review in self.reviews: 
#Check if restaurant matches
            if review.restaurant == restaurant:  
                return True
        return False

#Restaurant class representing a restaurant that receives reviews
class Restaurant(Base):
#Define the table name in the database

    __tablename__ = "restaurants" 
#Lets Define table columns
# Unique identifier for each restaurant
#Restaurant name (not null)    
        
    id = Column(Integer, primary_key=True)  
    name = Column(String, nullable=False) 

#Define the relationship between Restaurant and Review models (one-to-many)
#Restaurant can have many reviews    
    
    reviews = relationship("Review", backref="restaurant") 

#Initialize a restaurant object with name validation
    def __init__(self, name):
        if not isinstance(name, str) or len(name) < 1:
            raise ValueError("Restaurant name must be a string with at least one character")

        self.name = name

#Method to calculate the average star rating for the restaurant
    def average_star_rating(self):
#Check if there are any reviews        
        if not self.reviews:  
            return 0.0
        total_rating = 0
        for review in self.reviews:
#Sum up all rating values            
            total_rating += review.rating  
#Calculate and round average            
        return round(total_rating / len(self.reviews), 1)  

#Class method to find the top two restaurants with the highest average rating
    @classmethod
    def top_two_restaurants(cls, session):
        """
        This class method retrieves the top two restaurants with the highest
        average rating from the database session.

        Args:
            session: A SQLAlchemy session object.

        Returns:
            A list containing the top 2 Restaurant objects, or None if no reviews exist.
        """

        top_restaurants = (
        session.query(cls)
#Order by average rating (descending)        
            .order_by(cls.average_star_rating().desc())
#Limit to top 2 results              
            .limit(2)  
            .all()
        )
        return top_restaurants

