class SeedExtender:

    def extend_seed(self, seeds):
        extended_seeds = []
        for i in range(0, 2, 2):
            range_to_append = range(seeds[i], seeds[i] + seeds[i+1])
            extended_seeds.extend(range_to_append)
        return extended_seeds

    def get_seeds_boundary(self, seeds):
        seeds_boundary = []
        for i in range(0, len(seeds), 2):
            seeds_boundary.append([seeds[i], seeds[i] + seeds[i+1]])
            
        return seeds_boundary