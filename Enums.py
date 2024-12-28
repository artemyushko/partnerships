from enum import Enum

# This class exists purely for readability and to avoid too many variables in the code.
# Please only adjust it if new competitions are added or if the roles are expanded.

class Competitive(Enum):
    COMPETITIVE_ONLY = 0
    PRACTICE_ONLY = 1
    FAVOR_COMPETITIVE = 2
    FAVOR_PRACTICE = 3

class Role(Enum):
    LEAD = 0
    FOLLOW = 1
    EITHER = 2

class Mixed(Enum):
    ADVANCED = 0
    LESS_PROFICIENT = 1

class Level(Enum):
    # expand this as needed... ever lol
    NEWCOMER = 0
    NEWCOMER_BRONZE = 1
    BRONZE_ADVANCED_BRONZE = 2
    ADVANCED_BRONZE_SILVER = 3
    SILVER_GOLD = 4

class Competitions(Enum):
    BLAST = 0
    BADGER = 1
    DANCEFEST = 2
    NATIONALS = 3
