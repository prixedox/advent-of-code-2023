class RaceMaker:

    def __init__(self):
        pass

    def make_races(self, races: dict[str, list]):
        record_beats = []
        print(races)
        for i, time in enumerate(races["times"]):
            beated = 0
            for hold in range(time):

                distance = hold * (time - hold)
                if races["distances"][i] < distance:
                    beated += 1
            
            record_beats.append(beated)
        
        return record_beats