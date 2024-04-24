
# runtimes for low utilization under SJN
low_FIFO = [2*60+30.81, 2*60+30.81, 2*60+30.78, 2*60+30.80, 2*60+30.78, 2*60+30.81, 2*60+30.82, 2*60+30.80, 2*60+30.79, 2*60+30.78]
low_SJN = [2*60+30.81, 2*60+30.77, 2*60+30.80, 2*60+31.93, 2*60+30.79, 2*60+30.80, 2*60+30.80, 2*60+30.79, 2*60+30.79, 2*60+30.85]

high_FIFO = [38.01, 38.01, 38.01, 38.00, 38.00, 37.99, 38.00, 38.01, 38.00, 38.00]
high_SJN = [38.03, 37.99, 37.99, 38.00, 37.98, 37.98, 37.98, 38.00, 38.00, 38.00]

avg_low_FIFO = sum(low_FIFO) / 10
avg_low_SJN = sum(low_SJN) / 10

avg_high_FIFO = sum(high_FIFO) / 10
avg_high_SJN = sum(high_SJN) / 10

print(avg_low_FIFO)
print(avg_low_SJN)
print(avg_high_FIFO)
print(avg_high_SJN)