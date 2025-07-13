class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        # sort the arrays
        players.sort()
        trainers.sort()
        print(players, trainers)
        # For each player we need to find the trainer with least training ability
        trdx = 0 # trainer idx 
        pdx = 0
        # We will increament this if either there is a match or trainer is not sufficient
        pairings = 0
        while pdx < len(players) and trdx < len(trainers):
            p = players[pdx]
            print(p, trainers[trdx], trdx, )

            if trainers[trdx] >= p:
                pairings += 1
                trdx += 1
                pdx += 1
            else:
                trdx += 1
        return pairings

        