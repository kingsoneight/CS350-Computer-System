import re, statistics

text = "WaitMethod: BUSYWAIT WaitTime: 1 0 ClocksElapsed: 999940917 ClockSpeed: 999.940917 WaitMethod: BUSYWAIT WaitTime: 2 0 ClocksElapsed: 1999942501 ClockSpeed: 999.971250 WaitMethod: BUSYWAIT WaitTime: 3 0 ClocksElapsed: 2999941585 ClockSpeed: 999.980528 WaitMethod: BUSYWAIT WaitTime: 4 0 ClocksElapsed: 3999932918 ClockSpeed: 999.983229 WaitMethod: BUSYWAIT WaitTime: 5 0 ClocksElapsed: 4999924627 ClockSpeed: 999.984925 WaitMethod: BUSYWAIT WaitTime: 6 0 ClocksElapsed: 5999930128 ClockSpeed: 999.988355 WaitMethod: BUSYWAIT WaitTime: 7 0 ClocksElapsed: 6999947211 ClockSpeed: 999.992459 WaitMethod: BUSYWAIT WaitTime: 8 0 ClocksElapsed: 7999940962 ClockSpeed: 999.992620 WaitMethod: BUSYWAIT WaitTime: 9 0 ClocksElapsed: 8999939462 ClockSpeed: 999.993274 WaitMethod: BUSYWAIT WaitTime: 10 0 ClocksElapsed: 9999933213 ClockSpeed: 999.993321"
pattern = re.compile('ClockSpeed: (\d+\.\d+)')
matches = pattern.findall(text)
speeds = [float(i) for i in matches]
print(speeds)
print(max(speeds), min(speeds), statistics.mean(speeds), statistics.stdev(speeds))