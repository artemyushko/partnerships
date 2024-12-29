class Matchmaker(object):
    def __init__(self):
        pass

    def mutual(self, partners):
        """
        Returns a list of partners who want to dance with one another.
        """
        mutual = []
        i = 0
        while i < len(partners):
            j = i + 1
            while j < len(partners):
                if partners[i].name in partners[j].requests and partners[j].name in partners[i].requests:
                    mutual.append((partners[i], partners[j]))
                    partners.remove(i, j)
            i += 1
        return mutual
    
    def firm(self, partners):
        """
        Returns a list of partners who are firm matches.
        """
        firm = []
        i = 0
        while i < len(partners):
            j = i + 1
            while j < len(partners):
                if partners[j].name not in partners[i].no_go and partners[i].name not in partners[j].no_go:
                    if partners[i].level_match(partners[j]) or partners[i].mixed_match(partners[j]):
                        if partners[i].competitive_match(partners[j]) and partners[i].competition_match(partners[j]):
                            firm.append((partners[i], partners[j]))
                            partners.remove(i, j)
            i += 1
        return firm
    
    def non_firm(self, partners):
        """
        Returns a list of partners who are non-firm matches.
        """
        non_firm = []
        i = 0
        while i < len(partners):
            j = i + 1
            while j < len(partners):
                if partners[j].name not in partners[i].no_go and partners[i].name not in partners[j].no_go:
                    if partners[i].level_match(partners[j]) or partners[i].mixed_match(partners[j]):
                        non_firm.append((partners[i], partners[j]))
                        partners.remove(i, j)
            i += 1
        return non_firm

    def match(self, partners):
        """
        The main matching function. 
        No need to run any other ones.
        """
        
        matches = []

        # match the people who want to dance with one another
        matches.extend(self.mutual(partners))

        # make firm matches
        matches.extend(self.firm(partners))

        # make non-firm matches
        matches.extend(self.non_firm(partners))

        return matches
    