# Object Relations Code Challenge - Restaurants

For this assignment, we'll be working with a Yelp-style domain.

We have three models: `Restaurant`, `Customer`, and `Review`.

For our purposes, a `Restaurant` has many `Reviews`, a `Customer` has many
`Review`s, and a `Review` belongs to a `Customer` and to a `Restaurant`.

`Restaurant` - `Customer` is a many to many relationship.

**Note**: You should draw your domain on paper or on a whiteboard _before you
start coding_. Remember to identify a single source of truth for your data.

## Topics

- Classes and Instances
- Class and Instance Methods
- Variable Scope
- Object Relationships
- lists and list Methods

## Instructions

To get started, run `pipenv install` while inside of this directory. Then run
`pipenv shell` to jump into the shell.

Build out all of the methods listed in the deliverables. The methods are listed
in a suggested order, but you can feel free to tackle the ones you think are
easiest. Be careful: some of the later methods rely on earlier ones.

**Remember!** This code challenge has tests to help you check your work. You can
run `pytest` to make sure your code is functional before submitting.

We've provided you with a tool that you can use to test your code. To use it,
run `python debug.py` from the command line. This will start a `ipdb` session
with your classes defined. You can test out the methods that you write here. You
can add code to the `debug.py` file to define variables and create sample
instances of your objects.

Writing error-free code is more important than completing all of the
deliverables listed - prioritize writing methods that work over writing more
methods that don't work. You should test your code in the console as you write.

Similarly, messy code that works is better than clean code that doesn't. First,
prioritize getting things working. Then, if there is time at the end, refactor
your code to adhere to best practices. When you encounter duplicated logic,
extract it into a shared helper method.

**Before you submit!** Save and run your code to verify that it works as you
expect. If you have any methods that are not working yet, feel free to leave
comments describing your progress.

## Deliverables

Write the following methods in the classes in the files provided. Feel free to
build out any helper methods if needed.

### Initializers and Properties

#### Customer

- `Customer __init__(self, first_name, last_name)`
  - Customer is initialized with a given name and family name
- `Customer property first_name` and `Customer property last_name`
  - Return first and last name, respectively
  - Names must be of type `str`
  - Names must be between 1 and 25 characters, inclusive
  - Names **can be** changed after the `Customer` object is initialized

#### Restaurant

- `Restaurant __init__(self, name)`
  - Restaurant is initialized with a name
- `Restaurant property name`
  - Returns the restaurant's name
  - Names must be of type `str`
  - Names must be 1 or more characters
  - Names **can be** changed after the `Restaurant` object is initialized

#### Review

- `Review __init__(self, customer, restaurant, rating)`
  - Review is initialized with a `Customer` instance, a `Restaurant` instance,
    and a rating
- `Review property rating`
  - Returns the rating for a restaurant
  - Ratings must be of type `int`
  - Ratings must be between 1 and 5, inclusive
  - Ratings **cannot be** changed after the `Review` object is initialized

### Object Relationship Methods and Properties

#### Review

- `Review customer`
  - Returns the customer object for that review
  - Must be of type `Customer`
  - Customers **can be** changed after the `Review` object is initialized
- `Review restaurant`
  - Returns the restaurant object for that review
  - Must be of type `Restaurant`
  - Restaurants **can be** changed after the `Review` object is initialized

#### Restaurant

- `Restaurant reviews()`
  - Returns a list of all reviews for that restaurant
  - Reviews must be of type `Review`
- `Restaurant customers()`
  - Returns a **unique** list of all customers who have reviewed that
    restaurant.
  - Customers must be of type `Customer`

#### Customer

- `Customer reviews()`
  - Returns a list of all reviews a customer has written
  - Reviews must be of type `Review`
- `Customer restaurants()`
  - Returns a **unique** list of all restaurants a customer has reviewed
  - Restaurants must be of type `Restaurant`

### Aggregate and Association Methods

#### Customer

- `Customer num_negative_reviews()`
  - **Reminder**: a review is considered negative if its rating is 1 or 2
  - Returns the total number of negative reviews that a customer has authored
  - Returns `0` if the customer never left a bad review
- `Customer has_reviewed_restaurant(restaurant)`
  - Receives a `Restaurant` instance as argument
  - Returns `True` if the customer has written a review for the given restaurant
    object
  - Returns `False` otherwise

#### Restaurant

- `Restaurant average_star_rating()`
  - Returns the average star rating for a restaurant based on its reviews
  - Returns `0.0` if the user has no reviews
  - Rounds the result to the first decimal digit
  - **Reminder**: you can calculate the average by adding up all the ratings and
    dividing by the number of ratings
- `Restaurant classmethod top_two_restaurants()`
  - Returns the top 2 restaurants in descending order by average star rating
  - Restaurants must be of type `Restaurant`
  - Returns `None` if there are no reviews

### Bonus: Aggregate and Association Method

- `Customer classmethod top_negative_reviewer()`
  - **Reminder**: a review is considered negative if its rating is 1 or 2
  - Returns the `Customer` instance with the most negative reviews
  - Returns `None` if there are no negative reviews
  - Uncomment lines 157-182 in the customer_test file
  - _hint: will need a way to remember all customer objects_

### Bonus: For any invalid inputs raise an `Exception`

- First, **comment out** the following lines
  - **customer_test.py**
    - lines 23-27, and 45-50
  - **restaurant_test.py**
    - lines 24-25, and 37-38
  - **review_test.py**
    - lines 26-27, and 74
- Then, **uncomment** the following lines in the test files
  - **customer_test.py**
    - lines 30-35, 53-54, 57-58, 61-62, and 65-66
  - **restaurant_test.py**
    - lines 28-29, and 41-42
  - **review_test.py**
    - lines 30-31, 43-44, 47-48, 51-52, 85-86, and 115-116
# yelp
# yelp
