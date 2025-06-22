# mean,,median,mode

# from statistics import mode
# import scipy.stats as sp

# data=[10,20,30,40,50]
# mean=sum(data)/len(data)
# print("Mean:",mean)

# sorted_data=sorted(data)
# median=sorted_data[len(data)//2] if len(data)%2!=0 else \
#     (sorted_data[len(data)//2-1]+sorted_data[len(data)//2])/2
# print("median:",median)


# print("mode",mode(data))

# varience=sum((x-mean)**2 for x in data)/len(data)
# std_der=varience**0.5

# sample_mean=mean
# z_score=1.96

# ci=(sample_mean-z_score*(std_der/len(data)**0.5),
#     (sample_mean+z_score*(std_der/len(data)**0.5)))
# print("95% confidence interval",ci)

from scipy.stats import ttest_ind
group1=[2.3,2.5,2.8,3.6,3.1,2.9]
group2=[1.3,1.5,1.8,2.6,2.1,2.4]

t_stat,p_value=ttest_ind(group1,group1)
print("T_Statistic:",t_stat)
print("P_Value:",p_value)

alpha=0.5
if p_value<alpha:
    print("Reject the null hypothesis")
else:
    print("failed to reject to the null hypothesis") 



