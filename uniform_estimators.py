"""Experimentally verify your computations in the following way: Taking n = 100 and L = 10,
– For j = 1, . . . , 1000:
∗ Simulate X
j
1
, . . . , Xj
n and compute values for Lˆj
MOM and Lˆj
MLE
– Estimate the mean squared error for each population of estimator values.
– How do these estimated MSEs compare to your theoretical MSEs?"""
import random


def uniform_estimators(n=100, L=10):
    # First we compute the theoretical MSEs for both MOM and MLE
    theoretical_mse_mom = (L * L) / (3 * n)
    theoretical_mse_mle = ((2 * L * L) / ((n + 1) * (n + 2)))

    print("The theoretical MSE for MOM: {}".format(theoretical_mse_mom))
    print("The theoretical MSE for MLE: {}\n".format(theoretical_mse_mle))

    # We create a list where we can store the estimated MSE for each of our 1000 iterations
    estimated_mse_mom = []
    estimated_mse_mle = []

    # For a 1000 iterations, we choose 100 variables randomly and compute the estimated mse for both MOM and MSE
    for x in range(1000):
        r_vars = []
        for y in range(n):
            r_vars.append(random.random()*10)
        estimated_mse_mom.append(((2 * (sum(r_vars) / len(r_vars))) - L) ** 2)
        estimated_mse_mle.append((max(r_vars) - L) ** 2)

    # We then take the average of all 1000 experiments to compute the average of the estimated MSEs
    average_estimated_mse_mom = sum(estimated_mse_mom) / len(estimated_mse_mom)
    average_estimated_mse_mle = sum(estimated_mse_mle) / len(estimated_mse_mle)

    print("The average estimated MSE for MOM: {}".format(average_estimated_mse_mom))
    print("The average estimated MSE for MLE: {}\n".format(average_estimated_mse_mle))

    # We print the difference between the estimated and theoretical MSE
    print("Difference for MOM = {}".format(abs(average_estimated_mse_mom - theoretical_mse_mom)))
    print("Difference for MLE = {}".format(abs(average_estimated_mse_mle - theoretical_mse_mle)))


if __name__ == '__main__':
    uniform_estimators()
