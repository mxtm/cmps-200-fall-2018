# Maxwell Richard Tamer-Mahoney ID #: 201804029

class Polynom:
    def __init__(self, list_of_tuples):
        self.__polynom = []
        # Keeping track of what degree we are on in the while loop
        current_deg = 0
        while len(list_of_tuples) != 0:
            # Find the tuple with the degree we want
            desired_tuple = self.__coefficient_with_degree(current_deg, list_of_tuples)
            # If it exists, add the coefficient to the internal rep
            if desired_tuple != None:
                self.__polynom.append(desired_tuple[0])
                list_of_tuples.remove(desired_tuple)
            # If it doesn't exist, then add 0 to the internal rep
            else:
                self.__polynom.append(0)
            # Increment which degree term we want now
            current_deg += 1

    def __coefficient_with_degree(self, n, l):
        # A good old inefficient linear search
        for i in l:
            if i[1] == n:
                return i
        return None

    def degree(self):
        # The degree of our polynomial
        return len(self.__polynom) - 1

    def internal_rep(self):
        # Getter for the internal representation of the polynomial
        return self.__polynom

    def human_readable(self):
        # Construct a human readable representation of the polynomial for use
        # in the string representation
        human_readable_ver = '{}'.format(self.__polynom[0])
        for i in range(1, len(self.__polynom)):
            if i == 1:
                human_readable_ver += ' + ' + str(self.__polynom[i]) + 'x'
            else:
                human_readable_ver += ' + ' + str(self.__polynom[i]) + f'x^{i}'
        return human_readable_ver

    def __str__(self):
        # A nice clean string representation
        return '<Polynomial, degree {}: {}>'.format(self.degree(), self.human_readable())

    def __eq__(self, other):
        # For two polynomials to be equal their internal representation must be
        # as well
        return self.internal_rep() == other.internal_rep()
    
    def __add__(self, other):
        # Pick the one with the higher degree because that's how many times we
        # need to iterate
        higher_degree = self if self.degree() > other.degree() else other
        # Make an empty list to fill with tuples for the construction of the new resulting
        # polynomial
        result_list_of_tuples = []
        for i in range(len(higher_degree.internal_rep())):
            # If we can, add each coefficient
            try:
                result_list_of_tuples.append((self.internal_rep()[i] + other.internal_rep()[i], i))
            # If we can't, that means the lower degree polynomial doesn't have
            # a coefficient there, so it is regarded as if it were 0
            except IndexError:
                result_list_of_tuples.append((higher_degree.internal_rep()[i], i))
        # Construct a new polynomial with our result list of tuples and return
        # it
        return Polynom(result_list_of_tuples)

    def __product_of_terms(self, term1, term2):
        # Multiplication is messy and it's made easier if you break it down, so
        # here it's done term by term
        return Polynom([(term1[0] * term2[0], term1[1] + term2[1])])

    def __mul__(self, other):
        # Pick what has the higher and lower degree so that we can cover all
        # the terms in our nested loop
        higher_degree = self if self.degree() > other.degree() else other
        lower_degree = self if self.degree() < other.degree() else other
        result = Polynom([(0, 0)]) # Initialize a result polynomial that is at first empty
        for i in range(len(higher_degree.internal_rep())):
            for j in range(len(lower_degree.internal_rep())):
                # Add to our result polynomial the multiplication of each term
                result += self.__product_of_terms((higher_degree.internal_rep()[i], i), (lower_degree.internal_rep()[j], j))
        # Return our result polynomial
        return result
            
def test():
    p1 = Polynom([(2, 0), (4, 2), (1, 3)])
    p2 = Polynom([(1, 1), (1, 2)])
    p3 = p1 + p2
    p4 = p1 * p2
    answer1 = Polynom([(2, 0), (1, 1), (5, 2), (1, 3)])
    answer2 = Polynom([(2, 1), (2, 2), (4, 3), (5, 4), (1, 5)])

    print(p3 == answer1)
    print(p4 == answer2)

if __name__ == '__main__':
    test()
