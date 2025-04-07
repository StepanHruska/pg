import random

"""
vyneruje balicek vsech 108 karet
list
"""
def buildDeck():
    deck = []
    colours = ["Red", "Green", "Blue", "Yellow"]
    values = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, "Draw two", "Skip", "Reverse"]
    wilds = ["Wild", "Draw four"]
    for colour in colours:
        for value in values:
            cardValue = "{} {}".format(colour,value)
            deck.append(cardValue)  
            if value != 0:
                deck.append(cardValue)
    for i in range (4):
        deck.append(wilds[0])
        deck.append(wilds[1])
    return deck

def shuffleDeck(deck):
    for cardPos in range(len(deck)):
        randPos = random.randint(0, 107)
        deck[cardPos], deck[randPos] = deck[randPos], deck[cardPos]
    return deck

def drawCards(numCards):
    cardsDrawn = []
    for x in range(numCards):
        cardsDrawn.append(unoDeck.pop(0))
    return cardsDrawn

def showHand(player, playerHand):
    print("Player {}s Turn".format(player+1))
    print("Your hand")
    print("------------")
    y = 1
    for card in playerHand:
        print("{} {}".format(y,card))
        y += 1
    print("")

def canPlay(colour, value, playerHand):
    for card in playerHand:
        if "Wild" in card:
            return True
        elif colour in card or value in card:
            return True
    return False

unoDeck = buildDeck()
unoDeck = shuffleDeck(unoDeck)
discards = []

players = []
colours = ["Red", "Green", "Blue", "Yellow"]
numPlayers = int(input("How many players?"))
while numPlayers<2 or numPlayers>4:
    numPlayers = int(input("please enter a number between 2 - 4. How many players?"))
for player in range(numPlayers):
    players.append(drawCards(5))

print(players)

playerTurn = 0
playDirection = 1
playing = True
discards.append(unoDeck.pop(0))
splitCard = discards[0].split(" ",1)
currentColour = splitCard[0]
if currentColour != "Wild":
    cardValue = splitCard[1]
else:
    cardValue = "Any"

while playing:
    showHand(playerTurn, players[playerTurn])
    print("Card on top of the discard pile: {}".format(discards [-1]))
    if canPlay(currentColour, cardValue, players[playerTurn]):
        cardChosen = int(input("Which card do you want to play?"))
        while not canPlay(currentColour, cardValue,[players[playerTurn][cardChosen-1]]):
            cardChosen = int(input("Not a valid card. Which card do you want to play?"))
        print("You played {}".format(players[playerTurn][cardChosen-1]))
        discards.append(players[playerTurn].pop(cardChosen-1))
        
        #check for special cards
        splitCard = discards[-1].split(" ",1)
        currentColour = splitCard[0]
        if len(splitCard) == 1:
            cardValue = "Any"
        else:
            cardValue = splitCard[1]
        if currentColour == "Wild":
            for x in range(len(colours)):
                print("{} {}".format(x+1, colours[x]))
            newColour = int(input("What colour would you like to choose?"))
            while newColour < 1 or newColour > 4:
                newColour = int(input("Invalid option. What colour would you like to choose?")) 
            currentColour = colours[newColour-1]
        if cardValue == "Reverse":
            playDirection = playDirection * -1
        elif cardValue == "Skip":
            playerTurn += playDirection
        elif cardValue == "Draw two":
            players[playerTurn].extend(drawCards(2))
        elif cardValue == "Draw four":
            players[playerTurn].extend(drawCards(4))
        print("")
    else:
        print("You cant play, you have to draw a card")
        players[playerTurn].extend(drawCards(1))

    


    playerTurn += playDirection
    if playerTurn == numPlayers:
        playerTurn = 0
    elif playerTurn < 0:
        playerTurn = numPlayers-1