from random import randrange

def GenerateWinSets(AmountWinners,SharedNumbersToggle):
    WinnerSets = [[] for i in range(0,AmountWinners)]
    if SharedNumbersToggle is True:
        UsedNumbers = []
    for i in range(0,AmountWinners):
        while len(WinnerSets[i]) <=5:
            CurrentPullNumber = randrange(0,99)
            if SharedNumbersToggle is True:
                if CurrentPullNumber not in UsedNumbers and CurrentPullNumber not in WinnerSets[i]:
                    WinnerSets[i].append(CurrentPullNumber)
                    UsedNumbers.append(CurrentPullNumber)
            else:
                if CurrentPullNumber not in WinnerSets[i]:
                    WinnerSets[i].append(CurrentPullNumber)
    return WinnerSets

print("---- 6 Number Lottery Generator ----")
WinSetAmount = int(input("How many winning sets do you wish to generate? - "))
ShareBetweenSets = input("Share Number Pool between sets? (0-99) S/N - ")

match ShareBetweenSets:
    case "S":
        SharedNumbersToggle = True
        print(GenerateWinSets(WinSetAmount,SharedNumbersToggle))
    case "N":
        SharedNumbersToggle = False
        print(GenerateWinSets(WinSetAmount,SharedNumbersToggle))
    case _:
        print("Please input only a S / N")
input()


