"Q.1) Calculate the probability of MPG of Cars for the below cases.
"MPG <- Cars$MPG
"a.	P(MPG>38)
"b.	P(MPG<40)
"c.	P (20<MPG<50)
"

import pandas as pd
import numpy as np

cars = pd.read_csv("E:/Data Science 18012022/Probability Distributions,CLT, Confidence/Cars.csv")

# Exploratory Data Analysis
# Measures of Central Tendency / First moment business decision
cars.MPG.mean() # '.' is used to refer to the variables within object
cars.MPG.median()
cars.MPG.mode()

# mean 34.422
#Median 35.15
#mode 29.62

cars.MPG.var() # variance
cars.MPG.std() # standard deviation

#Variance 83.38
#Standard Deviation 9.131

 
#a. P(MPG>38)

# z-distribution
# cdf => cumulative distributive function; # similar to pnorm in R
stats.norm.cdf(38, 34.422, 9.133)  # Given a value, find the probability
# Probability 0.6523

# Z = (x-mu)/sigma
(38-34.422)/9.131
# Z = 0.39
# P = 65.23
#This implies the area under the curve (towards the left tail) from 0.39 of z value is around 65.23%

#b.	P(MPG<40)

# z-distribution
# cdf => cumulative distributive function; # similar to pnorm in R
stats.norm.cdf(40, 34.422, 9.133)  # Given a value, find the probability
# Probability 0.7293

# Z = (x-mu)/sigma
(40-34.422)/9.131
# Z = 0.61
#This implies the area under the curve (towards the left tail) from 0.61 of z value is around 72.93%

#c.	P (20<MPG<50) 
# z-distribution
# cdf => cumulative distributive function; # similar to pnorm in R
stats.norm.cdf(20, 34.422, 9.133)  # Given a value, find the probability
# Probability 0.0571

# Z = (x-mu)/sigma
(20-34.422)/9.131
# Z = -1.579
# p = 0.0571
#This implies the area under the curve (towards the left tail) from 0.0571 of z value is around 5.71%

stats.norm.cdf(50, 34.422, 9.133)  # Given a value, find the probability
# Probability 0.955

# Z = (x-mu)/sigma
(50-34.422)/9.131
# Z = 1.706        
# p = 0.955
#This implies the area under the curve (towards the left tail) from 0.0571 of z value is around 95.5%

P(20<MPG<50) 
0.955-0.0571
#P(20<MPG<50)=0.955-0.0571 = 0.8978
##################################################################
##################################################################

"Q2) Check whether the data follows normal distribution
"a)	Check whether the MPG of Cars follows Normal Distribution Dataset: Cars.csv
"b)	Check Whether the Adipose Tissue (AT) and Waist Circumference (Waist) from wc-at data set follows Normal Distribution
"Dataset: wc-at.csv

"a)"
#Normal Quantile-Quantile Plot
import scipy.stats as stats
import pylab

# Checking Whether data is normally distributed
stats.probplot(cars.MPG, dist='norm',plot=pylab) #pylab is visual representation
# Yes MPG of Cars follows Normal Distribution

"b"

wc = pd.read_csv("E:/Data Science 18012022/Probability Distributions,CLT, Confidence/wc-at.csv")

# Checking Whether data is normally distributed
stats.probplot(wc.Waist, dist='norm',plot=pylab) #pylab is visual representation
# Waist Circumference (Waist) from wc-at data set not follows Normal Distribution
# Waist data distribution plot is unnormal

stats.probplot(wc.AT, dist='norm',plot=pylab) #pylab is visual representation
# Adipose Tissue (AT) from wc-at data set follows Normal Distribution.
# Adipose Tissue data distribution plot is unnormal

"Q3) Calculate the Z scores of 90% confidence interval,94% confidence interval, 60% confidence interval"

# z-distribution
# ppf => Percent point function; # similar to qnorm in R
"Z scores of 90% confidence interval"
stats.norm.ppf(0.05,0,1) 
# -1.644

"Z scores of 94% confidence interval"
stats.norm.ppf(0.03,0,1) 
# -1.88

"Z scores of 60% confidence interval"
stats.norm.ppf(0.02,0,1) 
# -2.053

"Q4) Calculate the t scores of 95% confidence interval, 96% confidence interval, 99% confidence interval for sample size of 25"


#t-distribution
#(t-value,sample size)
"t scores of 95% confidence interval"
#sample size = 25, n-1 = 24
stats.t.ppf(0.975, 24) # 2.063
"t scores of 96% confidence interval"
stats.t.ppf(0.98, 24) # 2.171
"t scores of 99% confidence interval"
stats.t.ppf(0.99, 24) # 2.492

"Q5) A Government company claims that an average light bulb lasts 270 days. A researcher randomly selects 18 bulbs for testing. 
"The sampled bulbs last an average of 260 days, with a standard deviation of 90 days. If the CEO's claim were true, 
"what is the probability that 18 randomly selected bulbs would have an average life of no more than 260 days"

import scipy.stats as stats
import numpy as np
t = (260-270)/(90/np.sqrt(18))
#(t-value,sample size)
#sample size = 18, n-1 = 17
stats.t.cdf(t,17) # given a value, find the probability; # similar to pt in R, 0.321 = 32%

#32% of probability that 18 randomly selected bulbs would have an average life of no more than 260 days

"Q6) The time required for servicing transmissions is normally distributed with  = 45 minutes and  = 8 minutes. 
"The service manager plans to have work begin on the transmission of a customer’s car 10 minutes after the car is 
"dropped off and the customer is told that the car will be ready within 1 hour from drop-off. What is the probability 
"that the service manager cannot meet his commitment?"

# z-distribution
# cdf => cumulative distributive function; # similar to pnorm in R
# cdf(x,miu,sigma)
# right side portion
stats.norm.cdf(50,45,8)  
1-stats.norm.cdf(50,45,8)
# given a value, find the probability = 0.2659

"Q7) The current age (in years) of 400 clerical employees at an insurance claims processing center is normally distributed with mean= 38 and Standard deviation=6. 
"For each statement below, please specify True/False. If false, briefly explain why.
"A.	More employees at the processing center are older than 44 than between 38 and 44.
"B.	A training program for employees under the age of 30 at the center would be expected to attract about 36 employees.

"A."
# z-distribution
# cdf => cumulative distributive function; # similar to pnorm in R
# cdf(x,miu,sigma)
#probability for 44
stats.norm.cdf(44,38,6) # given a value, find the probability = 84.13 %  
#=> People above 44 age = 100 - 84.13 =  15.87% , 
#=>15.87*400/100  ≈  63  out of 400
#probability for 38  
stats.norm.cdf(38,38,6) #50%
#Hence People between 38 & 44  age = 84.13 - 50 = 34.13 %
#=>34.13*400/100  ≈  137 out of 400
#Hence More employees at the processing center are older than 44 than between 38 and 44. is FALSE

"B."
#Probability for 30
stats.norm.cdf(30,38,6) #9.12%
#=>9.15*400/100   ≈ 36 out of 400
#Hence A training program for employees under the age of 30 at the center would be expected to attract about 36 employees - TRUE

"Q9) Let X ~ N(100, 20^2) its (100, 20 square).Find two values, a and b, symmetric about the mean, such that the probability of the random variable taking a value between them is 0.99."
#X ~ N(100, 20^2)
#μ = 100, sigma = 20
#Since we need to find out the values of a and b, which are symmetric about the mean, such that the probability of random variable taking a value between them is 0.99, 
#we have to work out in reverse order. The Probability of getting value between a  and b should be 0.99. So the Probability of going wrong, or the Probability outside the  
#a and b area is 0.01 (ie. 1-0.99).
"The Probability towards left from a = -0.005 (ie. 0.01/2).The Probability towards right from b = +0.005 (ie. 0.01/2)."
#So since we have the probabilities of a and b, we need to calculate X, the random variable at a and b which has got these probabilities.
#By finding the Standard Normal Variable Z (Z Value), we can calculate the X values.

#For Probability 0.005 the Z Value is -2.57 (from Z Table)
stats.norm.ppf(0.005,0,1) #-2.57

#so, the range will become
'Z * σ + μ = X'
# for a = -0.005
#Z(-0.005)*20+100 
a = -(-2.57)*20+100 #151.4
#Z(+0.005)*20+100 
b = (-2.57)*20+100 #48.6

#So, D option is the Answer

"Q10) Consider a company that has two different divisions. The annual profits from the two divisions are independent and have distributions Profit1 ~ N(5, 3^2) and Profit2 ~ N(7, 4^2) respectively. Both the profits are in $ Million. Answer the following questions about the total profit of the company in Rupees. Assume that $1 = Rs. 45
"A.	Specify a Rupee range (centered on the mean) such that it contains 95% probability for the annual profit of the company.
"B.	Specify the 5th percentile of profit (in Rupees) for the company
"C.	Which of the two divisions has a larger probability of making a loss in a   given year?
"
#Profit1 ~ N(5, 3^2)
#Profit2 ~ N(7, 4^2)

#Applying linear transformation here, we will get new equation
# Mean1 + Mean2 = 5+7 = 12
# SD^2 = SD1^2 + SD2^2
# Profit1 ~ N(12, 5^2)

# Now converting dollars to ruppes by multiplying the equation by 45
# 45*N(12,5^2)
# We will get Mean profits from two different divisions of a company
# Mean Profit (12*45) = 540 Million rupees
# Stanndard Deviation (5*45) = RS. 225.0 Million

#A.Specify a Rupee range (centered on the mean) such that it contains 95% probability for the annual profit of the company.

stats.norm.interval(0.95,540,225) #(99.00810347848784, 980.9918965215122)
#Range is Rs (99.00810347848784, 980.9918965215122) in Millions

#B. Specify the 5th percentile of profit (in Rupees) for the company

import scipy.stats as stats
#calculation z-score at 5th percentile i.e area under the curve is 5%
#To compute 5th Percentile, we use the formula X=μ + Zσ; wherein from z table, 5 percentile = -1.645
z_score = stats.norm.ppf(0.05)
z_score # -1.6448536269514729

#Now, Profit at this percentile
profit_5_percebntile = 540+(-1.645)*(225)
profit_5_percebntile  #169.875
#5th percentile of profit (in Million Rupees) is 170.0

#C.	Which of the two divisions has a larger probability of making a loss in a   given year?

# Probability of Division 1 making a loss P(X<0)
stats.norm.cdf(0,5,3) #0.0477903522728147

# Probability of Division 2 making a loss P(X<0)
stats.norm.cdf(0,7,4) #0.040059156863817086

#Inference: Probability of Division 1 making a loss in a given year is more than Division 2.
