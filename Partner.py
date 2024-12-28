class Partner(object):
    """
    Represents a partner to be partnered with.
    """
    def __init__(self, name, level, competitive, mixed, competitions, dances, requests):
        self.name = name
        self.level = level
        self.competitive = competitive
        self.mixed = mixed
        self.competitions = competitions
        self.dances = dances
        self.requests = requests

    def level_match(self, candidate):
        """
        Returns True if the levels of the two partners match.
        """
        return self.level == candidate.level
    
    def competitive_match(self, candidate):
        """
        Returns True if the competitive preferences of the two partners match.
        """
        return self.competitive == candidate.competitive
    
    def mixed_match(self, candidate):
        """
        Returns True if the mixed preferences of the two partners match.
        """
        return self.mixed != candidate.mixed
    
    def competition_match(self, candidate):
        """
        Returns True if the competitions of the two partners match.
        """
        return set(self.competitions) == set(candidate.competitions)
    
