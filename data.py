import plotly.figure_factory as ff
import plotly.graph_objects as go
import statistics
import random


student_performance =[]
for i in range(0,100):
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    student_performance.append(dice1)

mean = sum(student_performance)/ len(student_performance)
std_deviation = statistics.stdev(student_performance)

median= statistics.median(student_performance)
mode= statistics.mode(student_performance)

first_std_deviation_start, first_std_deviation_end= mean- std_deviation, mean+std_deviation
second_std_deviation_start, second_std_deviation_end= mean- (2*std_deviation), mean+(2*std_deviation)
third_std_deviation_start, third_std_deviation_end= mean- (3*std_deviation), mean+(3*std_deviation)


fig = ff.create_distplot([student_performance],["Result"], show_hist=False)
fig.add_trace(go.Scatter(x=[mean, mean], y=[0,0,17], mode="lines", name= "MEAN"))
fig.add_trace(go.Scatter(x=[first_std_deviation_start, first_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_deviation_end, first_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))

fig.add_trace(go.Scatter(x=[second_std_deviation_start, second_std_deviation_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_deviation_end, second_std_deviation_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.show()

list_of_data_within_1_std_deviation = [result for result in student_performance if result > first_std_deviation_start and result < first_std_deviation_end]
list_of_data_within_2_std_deviation = [result for result in student_performance if result > second_std_deviation_start and result < second_std_deviation_end]
list_of_data_within_3_std_deviation = [result for result in student_performance if result > third_std_deviation_start and result < third_std_deviation_end]


print("STANDARD deviation of the data : {}" .format(std_deviation) )
print("{}% of data lies within 1 standard deviation".format(len(list_of_data_within_1_std_deviation)*100.0/len(student_performance)))
print("{}% of data lies within 2 standard deviation".format(len(list_of_data_within_2_std_deviation)*100.0/len(student_performance)))
print("{}% of data lies within 3 standard deviation".format(len(list_of_data_within_3_std_deviation)*100.0/len(student_performance)))



print(" Median : ", median)
print(" mode : ",mode)
print(" Mean : ", mean)
print(" Std_deviation : ",std_deviation)