# mean,,median,mode

from statistics import mode

data=[10,20,30,40,50]
mean=sum(data)/len(data)
print("Mean:",mean)

sorted_data=sorted(data)
median=sorted_data[len(data)//2] if len(data)%2!=0 else \
    (sorted_data[len(data)//2-1]+sorted_data[len(data)//2])/2
print("median:",median)


print("mode",mode(data))