import time
from termcolor import colored
import math
from data import COST_HORSE_SILVER_PER_DAY, COST_TENT_GOLD_PER_WEEK
from data import JOURNEY_IN_DAYS
from data import COST_FOOD_HORSE_COPPER_PER_DAY
from data import COST_FOOD_HUMAN_COPPER_PER_DAY
from data import COST_INN_HUMAN_SILVER_PER_NIGHT
from data import COST_INN_HORSE_COPPER_PER_NIGHT

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
    newlist = []
    for teller in range (0,len(list)):
        if list[teller][key] == value: 
                newlist.append(list[teller])
    return newlist

def getAdventuringPeople(people:list) -> list:
    return getFromListByKeyIs(people,'adventuring',True)

def getShareWithFriends(friends:list) -> int:
    return getFromListByKeyIs(friends,'shareWith',True)

def getAdventuringFriends(friends:list) -> list:
    newlist= []
    for teller in range (0,len(friends)):
        if friends[teller]['adventuring'] and friends[teller]['shareWith']: 
            newlist.append(friends[teller])
    return newlist 

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
    InterestingInvestors = []
    for index in range(0,len(investors)):    
        if investors[index]['profitReturn'] <= 10:
            InterestingInvestors.append(investors[index])
    return InterestingInvestors

def getAdventuringInvestors(investors:list) -> list:
    adventuringInvestors= []
    for index in range (len(getInterestingInvestors(investors))):
        if getInterestingInvestors(investors)[index]['adventuring'] :
            adventuringInvestors.append(getInterestingInvestors(investors)[index])
    return adventuringInvestors

def getTotalInvestorsCosts(investors:list, gear:list) -> float:
    people= getAdventuringInvestors(investors)
    rentalCost = getTotalRentalCost(1,1)
    foodCost = getJourneyFoodCostsInGold(1,1)
    totaal = (getItemsValueInGold(gear)  + rentalCost + foodCost) * len(people)
    return totaal
      
##################### M04.D02.O10 #####################

def getMaxAmountOfNightsInInn(leftoverGold:float, people:int, horses:int) -> int:
    people_cost = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) * people
    horses_cost  = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT) * horses
    herberg_cost = people_cost  + horses_cost
    try:
        maxNachten = leftoverGold // herberg_cost
    except ZeroDivisionError: 
        maxNachten = 0
    return maxNachten

def getJourneyInnCostsInGold(nightsInInn:int, people:int, horses:int) -> float:
    people_cost = silver2gold(COST_INN_HUMAN_SILVER_PER_NIGHT) * people
    horses_cost  = copper2gold(COST_INN_HORSE_COPPER_PER_NIGHT) * horses
    herberg_cost = round(nightsInInn * (people_cost + horses_cost) , 2)
    return herberg_cost

##################### M04.D02.O12 #####################

def getInvestorsCuts(profitGold:float, investors:list) -> list:
    goldList = []
    AdventuringInvestors = getInterestingInvestors(investors)
    for teller in range (len(AdventuringInvestors)):
        investorsCuts = round(profitGold / 100 * AdventuringInvestors[teller][ 'profitReturn'] , 2)
        goldList.append(investorsCuts)
    return goldList

def getAdventurerCut(profitGold:float, investorsCuts:list, fellowship:list) -> float:
    for gold in investorsCuts:
        profitGold -= gold
    adventureCut = round(profitGold / fellowship ,2)
    return adventureCut

##################### M04.D02.O13 #####################

def getEarnigs(profitGold:float, mainCharacter:dict, friends:list, investors:list) -> list:
    people = [mainCharacter] + friends + investors
    earnings = []

    # haal de juiste inhoud op
    adventuringFriends = getAdventuringFriends(friends)
    adventuringInvestors = getAdventuringInvestors(investors)
    investorsCuts = getInvestorsCuts(profitGold ,getInterestingInvestors(investors))
    goldCut = round(getAdventurerCut(profitGold,investorsCuts,len([mainCharacter]+adventuringFriends+getAdventuringInvestors(investors))),2)

    donateGold = 10

    # verdeel de uitkomsten
    for person in people:
        #code aanvullen
        startAdventure = getPersonCashInGold(person["cash"])
        endAdventure = startAdventure
        if person == mainCharacter:
            endAdventure += round(goldCut + (donateGold*len(adventuringFriends)),2)
        if person in adventuringFriends:
            endAdventure += round(goldCut-donateGold,2)
        
        if person in getInterestingInvestors(investors):
            if person in getAdventuringPeople(investors):
                    endAdventure += round((profitGold/100)*person["profitReturn"]+goldCut,2)
            else:
                    endAdventure += round((profitGold/100)*person["profitReturn"],2)
        earnings.append({
            'name'   : person["name"],
            'start'  : startAdventure,
            'end'    : endAdventure
        })
    return earnings

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