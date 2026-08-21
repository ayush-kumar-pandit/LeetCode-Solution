class Solution:
    def secondsBetweenTimes(self, startTime: str, endTime: str) -> int:
        x = ((int(startTime[0]) * 10) + int(startTime[1])) * 3600
        y = ((int(startTime[3]) * 10) + int(startTime[4])) * 60
        z = ((int(startTime[6]) * 10) + int(startTime[7]))
        sec1 = x + y + z

        x = ((int(endTime[0]) * 10) + int(endTime[1])) * 3600
        y = ((int(endTime[3]) * 10) + int(endTime[4])) * 60
        z = ((int(endTime[6]) * 10) + int(endTime[7]))
        sec2 = x + y + z

        return sec2 - sec1        