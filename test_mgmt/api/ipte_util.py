from scipy.stats.distributions import chi2


#
# def ipte_formula(iterations_or_ipte, number_of_incidents, confidence):
#     chi_square_inverse_right_tailed = chi2.ppf(confidence, df=2 * (number_of_incidents + 1))
#     return chi_square_inverse_right_tailed * (1000 / (iterations_or_ipte * 2))
#

def calculate_iterations_required(required_ipte, number_of_incidents, confidence=0.9):
    chi_square_inverse_right_tailed = chi2.ppf(confidence, df=2 * (number_of_incidents + 1))
    return chi_square_inverse_right_tailed * (1000 / (required_ipte * 2))
    # return ipte_formula(required_ipte, number_of_incidents, 0.9)


def calculate_ipte(number_of_iterations, number_of_incidents, confidence=0.9):
    chi_square_inverse_right_tailed = chi2.ppf(confidence, df=2 * (number_of_incidents + 1))
    return chi_square_inverse_right_tailed * (1000 / (number_of_iterations * 2))

# Test
# def test_util(number_of_incidents=0, number_of_iterations=576, confidence_interval=0.9, required_ipte=4.0):
#     print("Number of incidents=", number_of_incidents)
#     print("Total iterations=", number_of_iterations)
#     print("Confidence Interval(2 sided)=", confidence_interval)
#     ipti = calculate_ipte(number_of_iterations, number_of_incidents)
#     number_of_iterations_required = calculate_iterations_required(required_ipte, number_of_incidents)
#     print("IPTI: ", ipti, " \nNumber of iterations required to get this IPTI: ", number_of_iterations_required)
# test_util()
