class Solution:
    def videoStitching(self, clips: List[List[int]], time: int) -> int:
        dp = [99999] * (time + 1)
        dp[0] = 0
        
        clips.sort(key=lambda x: (x[1], -x[0]))
        reach = 0
        
        for clip in clips:
            if (clip[0] > reach) or (clip[0] >= time):
                continue
            
            for i in range(clip[0] + 1, min(clip[1] + 1, time + 1)):
                dp[i] = min(dp[i], dp[clip[0]] + 1)
            
            reach = max(reach, clip[1])
            
        if reach >= time:
            return dp[time]
        else:
            return -1
