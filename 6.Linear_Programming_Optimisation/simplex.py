import numpy
import math
import constants
"""
Input: { m, n, Mat[m x n] }, where:
    b = mat[1..m,0] .. column 0 is b >= 0, so x=0 is a basic feasible solution.
    c = mat[0,1..n] .. row 0 is z to maximize, note c is negated in input.
    A = mat[1..m,1..n] .. constraints.
    x = [x1..xm] are the named variables in the problem.
    Slack variables are in columns [m+1..m+n]

    e.g.:
    Tableau tab  = { 4, 5, {                     // Size of tableau [4 rows x 5 columns ]
        {  0.0 , -0.5 , -3.0 ,-1.0 , -4.0,   },  // Max: z = 0.5*x + 3*y + z + 4*w,
        { 40.0 ,  1.0 ,  1.0 , 1.0 ,  1.0,   },  //    x + y + z + w <= 40 .. b1
        { 10.0 , -2.0 , -1.0 , 1.0 ,  1.0,   },  //  -2x - y + z + w <= 10 .. b2
        { 10.0 ,  0.0 ,  1.0 , 0.0 , -1.0,   },  //        y     - w <= 10 .. b3
        }
        };

    Tableau tab  = { 4, 5,
                        {
                            {  ...}, => MAX
                            { .... },  => b1
                            { ....},  => b2
                            {... }, => b3
                        }
                    };
"""

#make Tableua as object
class Tableau:
    def __init__(self,m,n,mat):
        self.m = m
        self.n = n
        self.mat = mat

    def np(self, k):
        for j in range(0, k):
            print("-", end = '')
        print("")

    def check_equal(self, a, b):
        return True if math.fabs(a-b) < constants.epsilon else False

    def print_tableau(self, message):
        constants.counter += 1
        print(f"\n {constants.counter}. Tableau: {message}")
        self.np(70)
        print("col:", "\tb[i]", end='')
        for j in range(1,self.n):
            # print(f" \tx{j},", end='')
            print("   x%d," % j, end='')
        print("")
        for i in range(0, self.m):
            if(i == 0):
                print("max:", end='')
            else:
                print(f"b{i}: ", end='')
            for j in range(0, self.n):
                if(self.check_equal(int(self.mat.item(i,j)), self.mat.item(i,j))):
                    # print(f" {''* 6} {self.mat.item(i,j)}", end='')
                    print ("%6d" % int(self.mat.item(i,j)), end='')
                    # print(f" \t{int(self.mat.item(i,j))}", end='')
                else:
                    print("%6.2lf" % self.mat.item(i, j), end='')
            print("")
        self.np(70)

    def add_slack_variables(self):
        for i in range(1, self.m):
            for j in range(1, self.m):
                if (i == j):
                    self.mat = numpy.insert(self.mat, j+self.n -1, 0, axis = 1)
                    self.mat[i, j+self.n - 1] = (i == j)
        self.n += (self.m -1)

    def check_b_positive(self):
        for i in range(1, self.m):
            assert self.mat[i, 0] >= 0, "Unfortunately, Simplex method cannot be ran on these variables"

    def find_pivot_column(self):
        pivot_col = 1
        lowest = self.mat[0][pivot_col]
        for j in range(1, self.n):
            if (self.mat[0,j] < lowest):
                lowest = self.mat[0, j]
                pivot_col = j
        print(f"Most negative column in row[0] us col {pivot_col} = {lowest}.")
        if (lowest >= 0):
            return -1
        return pivot_col

    def print_optimal_vector(self, message):
        print(f"{message} at ", end='')
        for j in range(1, self.n):
            xi = self.find_basic_variable(j)
            # print(xi)
            if (xi != -1):
                # print("x%d=%3.2lf, " %j %self.mat[xi, 0], end='')
                print(f"x{j}={self.mat[xi, 0]}", end='')
            else:
                print(f"x{j}=0 ", end='')
        print()

    def find_basic_variable(self, col):
        xi = -1
        for i in range(1, self.m):
            if (self.check_equal(self.mat[i, col], 1)):
                if (xi == 1):
                    xi = i
                else:
                    return -1
            elif  not(self.check_equal(self.mat[i, col], 0)):
                return -1
        return xi

    def find_pivot_row(self, pivot_col):
        pivot_row = 0
        min_ratio = -1
        print(f"Rations A[row_i,0]/A[row_i,{pivot_col}] = [", end='')
        for i in range(1, self.m):
            ratio = self.mat[i,0] / self.mat[i, pivot_col]
            print("%3.2lf, " %ratio, end='')
            if ((ratio > 0 and (ratio < min_ratio)) or (min_ratio < 0)):
                min_ratio = ratio
                pivot_row = i
        print("].")
        if (min_ratio == -1):
            return -1
        print(f"Found pivot A[{pivot_row},{pivot_col}], min positive ratio={min_ratio} in row={pivot_row}.")
        return pivot_row
    
    def pivot_on(self, pivot_row, pivot_col):
        pivot = self.mat[pivot_row, pivot_col]
        assert pivot > 0, "Pivot is less than 0"
        for j in range(0, self.n):
            self.mat[pivot_row, j] /= pivot
        assert self.check_equal(self.mat[pivot_row, pivot_col], 1.), "No 1"
        for i in range(0, self.m):
            multiplier = self.mat[i, pivot_col]
            if (i==pivot_row):
                continue
            for j in range(0, self.n):
                self.mat[i, j] -= multiplier * self.mat[pivot_row, j]

    def simplex(self):
        loop = 0
        #pivot_row
        self.add_slack_variables()
        self.check_b_positive()
        self.print_tableau("Padded with slack variables")
        while True:
            loop += 1
            pivot_col = self.find_pivot_column()
            if (pivot_col < 0):
                print ("Found optimal value = A[0,0] = %3.2lf (no negative interges in row 0)." %self.mat[0,0])
                self.print_optimal_vector('Optimal Vector')
                break
            print(f"Entering variable {pivot_col} to be made basic, so pivot_col={pivot_col}.")
            pivot_row = self.find_pivot_row(pivot_col)
            if (pivot_row < 0):
                print("unbounded (no pivot_row).")
                break
            print(f"Leaving variable x{pivot_row}, so pivot_row={pivot_row}")
            self.pivot_on(pivot_row, pivot_col)
            self.print_tableau("After Pivoting")
            self.print_optimal_vector("Basic feasible solution")

            if(loop > 20):
                print(f"Too many iterations > {loop}")
                break

tab = Tableau(4,5,
        numpy.array([[0.0 , -0.5, -3.0, -1.0, -4.0],
        [40.0 , 1.0, 1.0 , 1.0 , 1.0],
        [10.0 , -2.0, -1.0 , 1.0 , 1.0],
        [10.0 , 0.0, 1.0 , 0.0 , -1.0]], dtype=object))

tab.print_tableau("Initial")
tab.simplex()



# print_tableau

# read_tableau

# pivot_on

# find_pivot_column

# find_pivot_row

# add_slack_variables

# check_b_positive

# find_basis_variable

# print_optimal_vector

# simplex