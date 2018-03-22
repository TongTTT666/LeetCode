class Solution:
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        if not timeSeries:
            return 0
        # Object: find all these intervals where Ashe is not in poisoned status
        # Initial
        # endTime is the end time of poisoned status
        # If the attack time is in poisoned status, that will have no interval.
        interval = endTime = 0
        for i in range(len(timeSeries)):
            if timeSeries[i] > endTime:
                interval += timeSeries[i] - endTime
            endTime = timeSeries[i] + duration
                   
        return timeSeries[len(timeSeries)-1] + duration - interval
        