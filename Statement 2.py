"Q3) Suppose we want to estimate the average weight of an adult male in Mexico. 
"We draw a random sample of 2,000 men from a population of 3,000,000 men and weigh them. 
"We find that the average person in our sample weighs 200 pounds, and the
"standard deviation of the sample is 30 pounds. Calculate 94%,98%,96% confidence interval?

"Given: n = 2000; N = 3,000,000; x̄ = 200; s = 30"

import scipy.stats as stats
#t-distribution
#(t-value,sample std deviation (s))
"t scores of 94% confidence interval"
#sample size = 2000, n-1 = 1999
stats.t.ppf(0.97, 1999) # 1.8818614764780113
"t scores of 98% confidence interval"
stats.t.ppf(0.99, 1999) # 2.328214776106972
"t scores of 96% confidence interval"
stats.t.ppf(0.98, 1999) # 2.055089962825778

"7	How many randomly selected employers (minimum number) must we contact in order to guarantee a margin of error of no more than 4% (at 95% confidence)?

"A.  600
"B.   400
"C.   550
"D. 1000
"

#We want to construct a 95% confidence interval for p with a margin of error equal to 4%.
#Because there is no estimate of the proportion given, we use p~=0.50 for a conservative estimate.
#For a 95% confidence interval, z∗=1.960
stats.norm.ppf(0.975,0,1)
#n=(1.960/0.04)^2 * (0.5)(1−0.5)=600.25
i=(1.960/0.04)**2 #2401.0
n=2401.0*0.5*0.5 #600.25
#This is the minimum sample size, therefore we should round up to 601. In order to construct a 95% confidence interval with a margin of error of 4%, we should obtain a sample of at least n=601.

#A. is the answer

"8	Suppose we want the above margin of error to be based on a 98% confidence level. What sample size (minimum) must we now use?

"A. 1000
"B.   757
"C.   848
"D.  543
"
#z score at 98% CI
z = stats.norm.ppf(0.99)
z #2.3263478740408408

# using the base formula for margin of error = z_scores*(sqrt([((p(hat))(1-p(hat))/N]))
# here p(hat) = sample proportion
# N = sample size

# calculating for N
N = ((z*z)*(0.5*0.5))/(0.04*0.04)
N # 845.6085048522405

# So, here N is nearest to option C

#C. is the answer