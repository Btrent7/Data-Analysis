from scipy.stats import uniform
# Linear "constant" distirbutions
# cdf = (limit, minumum value, maximum value)

# What is the probability of waiting 7 minutes (less/more) for a bus on 12 minute loop?
less_than_seven_mins = uniform.cdf(7,0,12)
more_than_seven_minutes = 1 - less_than_seven_mins

print(round(less_than_seven_mins, 4))
# Answer: 0.5833 (58.33%)
print(round(more_than_seven_minutes, 4))
# Answer: 0.4167 (41.67%)



from scipy.stats import binom
# Binomial distributions (heads / tails)
# rvs = (count of variables, probability decimal, number of tests)

# What is the probability of heads flipped 3 times?
heads_tails = binom.rvs(n=1, p=0.5, size=3)

print(heads_tails)

for trial in heads_tails:
    if trial == 1:
        print("heads")
    else:
        print("tails")

# What is the probability of 7 heads in 10 trials at 50% success rate?
seven_heads = binom.pmf(7, 10, 0.5)
# Answer: 0.1172 (11.72%)
print(round(seven_heads, 4))



from scipy.stats import poisson
# Random distributions
# pmf = calculate the probability of a specific value
# cdf = calculate the probability over an interval of outcomes

# What is the probability of getting 5 dollars when average is 4?
prob_5_pmf = poisson.pmf(5, 4)
# Answer: 0.1563 (15.63%)

prob_5_cdf = poisson.cdf(5,4)
# Answer: 0.7851 (78.51%)

print(round(prob_5_pmf, 4))

print(round(prob_5_cdf, 4))



from scipy.stats import expon
# Exponential distributions; the average time between Poisson events

# What is the probability of taking 1 hour when average is 2.5 hours?
print(round(expon.cdf(1, scale=2.5), 4))
# Answer: 0.3297 (32.97%)

# What is the probability of taking 4 hours when average is 2.5 hours?
print(round(1 - expon.cdf(4, scale=2.5), 4))
# Answer: 0.2019 (20.19%)

# What is the probability of taking between 3 - 4 hours when average is 2.5 hours?
print(round(expon.cdf(4, scale=2.5) - expon.cdf(3, scale=2.5), 4))
# Answer: 0.0993 (9.93%)