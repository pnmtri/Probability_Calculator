import copy
import random

class Hat:
    def __init__(self, **balls): # **balls allows the function to accept many keyword arguments, each representing a color and its count

        self.contents = [] # Create the list of balls given
        for color, count in balls.items():
            self.contents += [color]*count # [color] * count creates a list of repeated strings. If we use color * count, we get one long string like 'redredred'

    
    def draw(self, num_balls): # number of balls to draw from the hat
        if num_balls >= len(self.contents): 
            # If we're trying to draw more balls than we have, just return all the balls (no random selection needed)
            drawn = self.contents.copy()
            self.contents.clear()  # remove all balls from the hat
            return drawn
        
        # randomly pick balls
        drawn_balls = random.sample(self.contents, num_balls) # sample() is used to pick randomly the balls into a list of colors picked

        for ball in drawn_balls:
            self.contents.remove(ball) # remove balls randomly picked from list contents
        
        return drawn_balls
        
        

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    """
        hat --> balls (object)
        expected_balls --> attempted balls to draw (object), e.g. {'blue': 2, 'red': 1}
        num_balls_drawn --> numvber of balls to draw out of the hat in each experiment
        num_experiments --> number of experiments to perform => The more experiments to perform, the more accurate the probability returned to be
        ### Probability = M / N (whereas, M is the count of how many times I get the specific balls with expected colors, and N is the numer of experiments which will be given in the function call)
    """
    
    # success counts how many times we get the expected balls. It will be later used to calculate probability
    success = 0
    
    # Because num_experiments parameter is given, use for loop for the whole function to repeat the random tests for num_experiments times:
    for _ in range(num_experiments):
        # Make a deep copy of hat
        test_hat = copy.deepcopy(hat)   # A normal copy (copy.copy) would still share the same data inside.
                                        # If we change it, it can affect the original hat.
                                        # deepcopy makes a full independent copy.

        # Draw balls 
        """
            Essentially, test_hat is actually a copy of class hat which contains a balls dictionary in which
            the keys are color names and their values are number for each color.
            # 1. Use test_hat to draw randomly balls from it. --> Use draw() method from class Hat --> Same as making a list of
            colors counted.
            # 2. Then, create a dictionary of drawn balls with their colors as values to support the next demand.
            # 3. Then, increment 1 for success variable if the condition (of the balls' colors are match with expected_balls colors) is satisfied. 
            Otherwise, move to the next experiment. The repetition will stop until the _ temporary var is equal to num_experiments.
        """
        
        # 1. Create the list of drawn balls with specified numbers of colors
        drawn = test_hat.draw(num_balls_drawn)
        
        # 2. Create 
        drawn_count = {}
        for ball in drawn:
            if ball in drawn_count:
                drawn_count[ball] += 1 
            else:
                drawn_count[ball] = 1 
            """
                The operation of '= 1' is because specified ball was drawn but was not counted in the dictionary, 
                we set it to 1 the first time we see this color in the drawn list.
            """
        
        # 3. 
        
        # match is a flag (True/False) to decide whether to count this experiment as a success
        match = True
        # Building specific constraint for match variable 
        for color in expected_balls: # 'color' is a key in the expected_balls dictionary, representing the target color we want to check its count
            if drawn_count.get(color, 0) < expected_balls[color]: # Both drawn_count.get(color, 0) and expected_balls[color] will return number digits. 
                match = False
                break # Once the match variable is False. The success will not be incremented by using break the loop
            """
                the reason for match being True only when the num of color drawn is equal to or bigger than the num of color expected,
                is actually
            """
        
        if match:
            success += 1 
    
    # After the mother loop, return the probability using the following formula
    return success/num_experiments # Probability = number of successful draws / total number of experiments



# SOME TESTS
print("#### Test 1 ####")
hat = Hat(red=2, blue=3)
print(hat.contents)
print("\n")

print("#### Test 2 ####")
hat = Hat(green=4, yellow=3)
drawn = hat.draw(3)
print("Drawn:", drawn)
print("Remaining in hat:", hat.contents)
print("\n")

print("#### Test 3 ####")
hat = Hat(blue=2)
drawn = hat.draw(5)
print("Drawn:", drawn)
print("Remaining in hat:", hat.contents)
print("\n")

print("#### Test 4 ####")
hat = Hat(red=4, green=3, blue=2)
result1 = experiment(hat, {"red": 2}, 4, 100)
result2 = experiment(hat, {"red": 2}, 4, 100)
print("Result 1:", result1)
print("Result 2:", result2)
print("\n")

print("#### Test 5 ####")
hat = Hat(red=2)
drawn = hat.draw(0)
print("Drawn:", drawn)
print("Remaining:", hat.contents)
print("\n")

print("#### Test 6 ####")
hat = Hat(blue=1)
result = experiment(hat, {"blue": 2}, 1, 100)
print("Probability:", result)
print("\n")

print("#### Test 7 ####")
hat = Hat(red=5, green=3)
result = experiment(hat, {"red": 1}, 4, 200)
print("Probability:", result)
print("\n")
