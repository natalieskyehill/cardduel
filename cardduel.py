from random import *
NUMCARDS = 52
DECK = 0
PLAYER = 1
COMP = 2
#Create variable DISCARD of type integer with initial value 3
DISCARD = 3

cardLoc = [0] * NUMCARDS
suitName = ("hearts", "diamonds", "spades", "clubs")
rankName = ("Ace", "Two", "Three", "Four", "Five", "Six", "Seven",
            "Eight", "Nine", "Ten", "Jack", "Queen", "King")
playerName = ("deck", "player", "computer")

#Create varaible playerScore of type integer with initial value 0
playerScore = 0
#Create varaible comScore of type integer with initial value 0
comScore = 0

def main():
  clearDeck()

  for i in range(5):
    assignCard(PLAYER)
    assignCard(COMP)

  #showDeck()
  showHand(PLAYER)
  #showHand(COMP)

  playerSelect()
  computerSelect()

  compareAndScore()
  drawCard()


def clearDeck():
    #Import global variables cardLoc, NUMCARDS, playerScore, and comScore
    global cardLoc
    global NUMCARDS
    global playerScore
    global comScore

    #Reset all cardLoc indeces to 0
    cardLoc = [0] * NUMCARDS

    #Reset playerScore to 0
    playerScore = 0
    #Reset comScore to 0
    comScore = 0

def getCardName(card):
    rank = card % 13
    suit = card // 13
    cardName = "{} of {}".format(rankName[rank],suitName[suit])
    return cardName


def assignCard(whichOne):
    global cardLoc
    valueToAssign = whichOne
    card = randint(0,51)
    if (cardLoc[card] == 0):
        cardLoc[card] = valueToAssign
    else:
        assignCard(whichOne)


def showDeck():
    global deck
    print("\nLocation of all cards:")
    for i in range(len(cardLoc)):
        print("{}: {} ({})".format(i, getCardName(i), playerName[cardLoc[i]]))
    print("\n")


def showHand(whichOne):
    print("Showing {}'s hand:".format(playerName[whichOne]))
    for i in range(len(cardLoc)):
        if (cardLoc[i] == whichOne):
            print("{}: {}".format(i, getCardName(i)))
    print("\n")

#Create function playerSelect() with no parameters
def playerSelect():
    #Create global variable pSelection
    global pSelection
    #Import global variable cardLoc
    global cardLoc

    #Input card number to play and store result in pSelection
    pSelection = input("Which card will you play? \n")

    try:
        #Convert pSelection to integer
        pSelection = int(pSelection)

        #If cardLoc at index pSelection is equal to 1, set value to 3
        if (cardLoc[pSelection] == 1):
            cardLoc[pSelection] = 3
        #If cardLoc at index pSelection is not equal to 1, output message to user and rerun playerSelect()
        else:
            print("Card not in your hand! Please select another")
            playerSelect()
    except ValueError:
        print("Card not in your hand! Please select another")
        playerSelect()
    except IndexError:
        print("Card not in your hand! Please select another")
        playerSelect()

#Create function computerSelect() with no parameters
def computerSelect():
    #Create variable comHand of type list with empty initial value
    comHand = []

    #Create variable comBest of type integer with initial value 0
    comBest = 0

    #Import global variables comSelection and cardLoc
    global comSelection
    global cardLoc

    #Begin with i at 0 and add 1 to sentry until greater than or equal to length of cardLoc
    for i in range(len(cardLoc)):
        #If cardLoc at index i equals 2, join i to comHand
        if (cardLoc[i] == 2):
            comHand.append(i)
            #If i % 13 is greater than or equal to comBest, set comBest to i
            if ((i % 13) >= comBest):
                comBest = i

    #Set comSelection to comBest
    comSelection = comBest
    #Convert comSelection to integer
    comSelection = int(comSelection)

    #Set cardLoc at index comSelection to 3
    cardLoc[comSelection] = 3

#Create function compareAndScore() with no parameters that returns variable string
def compareAndScore():
    #Import global variables pSelection, comSelection, playerScore, and comScore
    global pSelection
    global comSelection
    global playerScore
    global comScore

    #Output result of getCardName() with parameter pSelection
    print("\nPlayer played " + getCardName(pSelection))
    #Output result of getCardName() with parameter comSelection
    print("Computer played " + getCardName(comSelection) + "\n")

    #If pSelection % 13 is greater than comSelection % 13, output "Player wins round" and add 1 to playerScore
    if ((pSelection % 13) > (comSelection % 13)):
        print("\nPlayer wins round")
        playerScore += 1
    #If comSelection % 13 is greater than pSelection % 13, output "Computer wins round" and add 1 to comScore
    elif ((pSelection % 13) < (comSelection % 13)):
        print("\nComputer wins round")
        comScore += 1
    #If pSelection % 13 equals comSelection % 13, output "Round is a tie"
    else:
        print("Round is a tie")

    #Output playerScore and comScore
    print("Current score: Player {}, Computer {}\n".format(playerScore,comScore))

#Create function drawCard() with no parameters
def drawCard():
    #Import global variable cardLoc
    global cardLoc

    #If there is a 0 remaining in cardLoc, rerun assignCard() with parameter PLAYER and again with parameter COMP
    if 0 in cardLoc:
        assignCard(PLAYER)
        assignCard(COMP)
    #If there is a 1 remaining in cardLoc, rerun showHand() with parameter PLAYER and run newRound()
    if 1 in cardLoc:
        showHand(PLAYER)
        newRound()
    #If there is no 1 remaining in cardLoc, run finalScore()
    else:
        finalScore()

#Create function newRound() with no parameters
def newRound():
    #Run playerSelect(), computerSelect(), compareAndScore(), and drawCard()
    playerSelect()
    computerSelect()
    compareAndScore()
    drawCard()

#Create function finalScore() with no parameters that returns string
def finalScore():
    #Import global variables playerScore, comScore, and cardLoc
    global playerScore
    global comScore
    global cardLoc

    #Output "End of game"
    print("End of game")
    #Output playerScore and comScore
    print("Final score: Player {}, Computer {}".format(playerScore,comScore))

    #If playerScore is greater than comScore, output "Player wins"
    if (playerScore > comScore):
        print("Player wins!\n")
    #If comScore is greater than playerScore, output "Computer wins"
    elif (playerScore < comScore):
        print("Computer wins!\n")
    #If playerScore is equal to comScore, output "Game is a tie"
    else:
        print("Game is a tie!\n")

    #Rerun menu()
    menu()

def menu():
    print("Card Duel!\n")
    selection = input(" 0) Play\n 1) Instructions\n\n")
    selection = int(selection)
    if (selection == 0):
        main()
    elif (selection == 1):
        print("Card Duel is a game similar to War, only in each round, the player chooses the card they will play from their hand. Get the most points to win!\n")
        menu()
    else:
        print("Please select an option")
        menu()



menu()
main()

