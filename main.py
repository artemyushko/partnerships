"""
Main file to run the code.

@TODO: Add partnership notes (lead/follow, mixed/regular, style etc.)
"""

from Matchmaker import Matchmaker

def main():

    # parse the input csv and create the list of partners for each style
    partners = []

    # for each one, run the matchmaker algorithm
    matchmaker = Matchmaker()
    matches = matchmaker.match(partners)

    # output the results

    return

if __name__=="__main__":
    main()