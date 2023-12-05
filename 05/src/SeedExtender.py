class SeedExtender:

    def extend_seed(self, seeds):
        extended_seeds = []
        for i in range(0, len(seeds), 2):
            range_to_append = (seeds[i], seeds[i] + seeds[i+1])
            extended_seeds.extend(range_to_append)
        print(extended_seeds)
        return extended_seeds