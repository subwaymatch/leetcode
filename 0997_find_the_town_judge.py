class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        if N == 1:
            return 1
    
        judge_candidate = None
        
        trusts_map = {}
        trusted_map = {}
        
        for t in trust:
            if t[0] not in trusts_map:
                trusts_map[t[0]] = True
        
            if t[1] in trusted_map:
                trusted_map[t[1]].append(t[0])
            else:
                trusted_map[t[1]] = [t[0]]
                
            if len(trusted_map[t[1]]) == N - 1:
                if judge_candidate is not None:
                    return -1
                else:
                    judge_candidate = t[1]
                    
        if judge_candidate is not None and judge_candidate not in trusts_map:
            return judge_candidate
        
        return -1
