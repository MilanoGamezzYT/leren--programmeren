import time
from termcolor import colored
import math
from data import COST_HORSE_SILVER_PER_DAY, COST_TENT_GOLD_PER_WEEK
from data import JOURNEY_IN_DAYS
from data import COST_FOOD_HORSE_COPPER_PER_DAY
from data import COST_FOOD_HUMAN_COPPER_PER_DAY
from data import investors

##################### M04.D02.O2 #####################

def copper2silver(amount:int) -> float:
    return amount / 10

def silver2gold(amount:int) -> float:
    return amount / 5 

def copper2gold(amount:int) -> float:
    return silver2gold(copper2silver(amount))

def platinum2gold(amount:int) -> float:
    return amount * 25

def getPersonCashInGold(personCash:dict) -> float:
    return (platinum2gold(personCash['platinum']) + personCash['gold'] + silver2gold(personCash['silver']) + copper2gold(personCash['copper']))

##################### M04.D02.O4 #####################

def getJourneyFoodCostsInGold(people:int, horses:int) -> float:
    return (people * COST_FOOD_HUMAN_COPPER_PER_DAY / 50 * JOURNEY_IN_DAYS) + (horses * COST_FOOD_HORSE_COPPER_PER_DAY / 50 * JOURNEY_IN_DAYS)

##################### M04.D02.O5 #####################

def getFromListByKeyIs(list:list, key:str, value:any) -> list:
    return [item for item in list if item[key] == value]

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people, 'adventuring', True)

def getShareWithFriends(friends:list) -> int:
    return getFromListByKeyIs(friends, 'shareWith', True)

def getAdventuringFriends(friends:list) -> list:
    return getFromListByKeyIs(friends, 'adventuring', True)

##################### M04.D02.O6 #####################

def getNumberOfHorsesNeeded(people: int) -> int:
    return math.ceil(people / 2)

def getNumberOfTentsNeeded(people: int) -> int:
    return math.ceil(people / 3)

def getTotalRentalCost(horses: int, tents: int) -> float:
   return (silver2gold((horses * COST_HORSE_SILVER_PER_DAY) * (JOURNEY_IN_DAYS))) + ((tents * COST_TENT_GOLD_PER_WEEK ) * math.ceil( JOURNEY_IN_DAYS / 7))

##################### M04.D02.O7 #####################

def getItemsAsText(items:list) -> str:
    return ', '.join([f"{item['amount']}{item['unit']} {item['name']}" for item in items])

def getItemsValueInGold(items: list) -> float:
    total_gold = 0
    for item in items:
        if item['price']['type'] == 'gold':
            total_gold += item['amount'] * item['price']['amount']
        elif item['price']['type'] == 'silver':
            total_gold += silver2gold(item['amount'] * item['price']['amount'])
        elif item['price']['type'] == 'copper':
            total_gold += copper2gold(item['amount'] * item['price']['amount'])
        elif item['price']['type'] == 'platinum':
            total_gold += platinum2gold(item['amount'] * item['price']['amount'])
    return total_gold



##################### M04.D02.O8 #####################

def getCashInGoldFromPeople(people:list) -> float:
    total_cash = 0
    for person in people:
        total_cash += getPersonCashInGold(person['cash'])
    return total_cash


##################### M04.D02.O9 #####################

def getInterestingInvestors(investors:list) -> list:
    return getFromListByKeyIs(investors, 'interesting', True)


def getAdventuringInvestors(investors:list) -> list:
    return getFromListByKeyIs(investors, 'adventuring', True)

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    total_gold = 0
    for investor in investors:
        if investor['cash'] == 'gold':
            total_gold += investor(['amount'] * investor['cash']['gold'])
        elif investor['price']['type'] == 'silver':
            total_gold += silver2gold(investor['amount'] * investor['cash']['silver'])
        elif investor['price']['type'] == 'copper':
            total_gold += copper2gold(investor['amount'] * investor['cash']['copper'])
        elif investor['price']['type'] == 'platinum':
            total_gold += platinum2gold(investor['amount'] * investor['cash']['platinum'])
    return total_gold
      

##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    pass

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    pass

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    pass

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:int) -> float:
    pass

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    pass

##################### view functions #####################
def print_colorvars(txt:str='{}', vars:list=[], color:str='yellow') -> None:
    vars = map(lambda string, color=color: colored(str(string), color, attrs=['bold']) ,vars)
    print(txt.format(*vars))

def print_title(name:str) -> None:
    print_colorvars(vars=['=== [ {} ] ==='.format(name)], color='green')

def print_chapter(number:int, name:str) -> None:
    nextStep(2)
    print_colorvars(vars=['- CHAPTER {}: {} -'.format(number, name)], color='magenta')

def nextStep(secwait:int=1) -> None:
    print('')
    time.sleep(secwait)

def ifOne(amount:int, yes:str, no:str, single='een') -> str:
    text = yes if amount == 1 else no
    amount = single if amount == 1 else amount
    return '{} {}'.format(amount, text).lstrip()