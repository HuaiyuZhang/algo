def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        count_by_user = {}
        for i, j in logs:
            if i not in count_by_user:
                count_by_user[i] = set()
            count_by_user[i].add(j)
        
        count_by_minute = {}
        for user in count_by_user:
            curr_user_count = len(count_by_user[user])
            if curr_user_count not in count_by_minute:
                count_by_minute[curr_user_count] = 1
            else:
                count_by_minute[curr_user_count] += 1
        
        res = [0]*k
        for i in range(k):
            if i+1 in count_by_minute:
                res[i] = count_by_minute[i+1] 
        return res