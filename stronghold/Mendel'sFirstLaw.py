#This problem is about to solve Mendel's First Law using Python. To find the probability of an offspring being dominant phenotype.

def calculate_dominant_probability(k, m, n):
    '''calculates the probabolity that two randomly selected mating organisms will produce an individual possessing a dominant allele.
    
    Args:
        k (int): number of homozygous dominant individuals
        m (int): number of heterozygous individuals
        n (int): number of homozygous recessive individuals
        
    returns:
        A float representing the probability of an offspring being dominant phenotype.
    '''
    #Calculate  the total number of ways to pick two distinct organisms.
    #This is T*(T-1) .
    total_pairs = (k + m + n) * (k + m + n - 1)

    # === Calculate the probabitity of getting a homozygous recessive ('aa') offspring ===

    # 1. probability of 'aa' from Aa x Aa mating: 
    #    - Probability of picking Aa then Aa: (m / T) * (m - 1) / (T - 1)
    #    - probability of 'aa' offspring from this pair: 0.25
    #    - Combination: (m * (m - 1) * 0.25) / (T * (T - 1))
    prob_aa_from_mm = (m * (m - 1)) * 0.25 

    # 2. Probability of 'aa' from Aa x aa mating:
    #    - Probability of picking Aa then aa: (m / T) * (n / (T - 1))
    #    - Probability of picking aa then Aa: (m / T) * (n / (T - 1))
    #    - Total probability of this pair type: (2 * m * n) / (T(T - 1))
    #    - probability of 'aa' offspring from this pair: 0.5
    #    - combination: (2 * m * n * 0.5) / (T * (T - 1))
    prob_aa_from_mn_nm = (m * n) # We've combined the 0.5 * 2 here

    # 3. Probability of 'aa' from aa x aa mating:
    #    - Probability of picking aa then aa: (n / T) * ((n - 1) / (T - 1))
    #    - Probability of 'aa' offspring from this pair: 1
    #    - Combination: (n * (n - 1) *1.0) / (T * (T - 1))
    prob_aa_from_nn = (n * (n - 1)) * 1.0

    #Calculate the Total probability of getting 'aa' offspring (P_aa)
    #this is the sum of the numerators divided by the total pairs (demoninator)
    prob_aa =(prob_aa_from_mm + prob_aa_from_mn_nm +prob_aa_from_nn) / total_pairs

    # The probability of having a dominant allel (p_dom) is 1 - p_aa
    prob_dominant = 1 - prob_aa
    
    return prob_dominant

# ===solution of question:===
k = 23
m = 16
n = 24

# calculate the probability
probability = calculate_dominant_probability(k, m, n)

# print the result:
print(f"given k = {k}, m ={m}, n = {n}.")
print(f"The probability of an offspring with a dominant is: {probability}")
print(f"Formatted to 5 decimal places: {probability:.5f}")

