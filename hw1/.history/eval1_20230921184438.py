import re

text = "WaitMethod: SLEEP WaitTime: 1 0 ClocksElapsed: 1005398834 ClockSpeed: 1005.398834 WaitMethod: SLEEP WaitTime: 2 0 ClocksElapsed: 2005726376 ClockSpeed: 1002.863188 WaitMethod: SLEEP WaitTime: 3 0 ClocksElapsed: 3005821293 ClockSpeed: 1001.940431 WaitMethod: SLEEP WaitTime: 4 0 ClocksElapsed: 4001136168 ClockSpeed: 1000.284042 WaitMethod: SLEEP WaitTime: 5 0 ClocksElapsed: 5001537044 ClockSpeed: 1000.307409 WaitMethod: SLEEP WaitTime: 6 0 ClocksElapsed: 6002337878 ClockSpeed: 1000.389646 WaitMethod: SLEEP WaitTime: 7 0 ClocksElapsed: 7001505462 ClockSpeed: 1000.215066 WaitMethod: SLEEP WaitTime: 8 0 ClocksElapsed: 8002433670 ClockSpeed: 1000.304209 WaitMethod: SLEEP WaitTime: 9 0 ClocksElapsed: 9004113254 ClockSpeed: 1000.457028 WaitMethod: SLEEP WaitTime: 10 0 ClocksElapsed: 10001915962 ClockSpeed: 1000.191596 "
pattern = re.compile('ClockSpeed: (\d+\.\d+)')
matches = pattern.findall(text)
print(matches)