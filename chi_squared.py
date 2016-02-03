from scipy import stats
import collections
import pandas as pd
import matplotlib.pyplot as plt

loansData = pd.read_csv('https://spark-public.s3.amazonaws.com/dataanalysis/loansData.csv')
loansData.dropna(inplace=True)

freq = collections.Counter(loansData['Amount.Funded.By.Investors'])
freq1= collections.Counter(loansData["Amount.Requested"])

chi, p = stats.chisquare(freq.values())
chi1,p1=stats.chisquare(freq1.values())

print "Amount Funded by Investors"
print "The Chi squared value is :",chi
print "The P value is", p
print ""
print "Amount Requested"
print "The Chi squared value is :",chi1
print "The P value is", p1
