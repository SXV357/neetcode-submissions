class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        '''
        worst: 1 boat per person so res = len(people) since the weight of a given person cannot exceed boats limit

        either we pair people up or send people individually but minimize how many boats we're using

        [1, 2, 4, 5], lim = 6

        [1, 2, 2, 3, 3], lim = 3

        pair up as many people as possible then others go alone?
        '''

        # optimal

        pairs, individual = 0, 0
        people.sort()

        l, r = 0, len(people) - 1

        while l <= r:
            # heavy goes by themselves
            if people[l] + people[r] > limit:
                individual += 1
                r -= 1
                continue
            
            # within the limit
            if l != r:
                pairs += 1
            else:
                individual += 1

            l += 1
            r -= 1
        
        return pairs + individual
