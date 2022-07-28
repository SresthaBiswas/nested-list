question_list = ["How many continents are there?","What is the capital of India?",
"NG mei kaun se course padhaya jaata hai?"]
option_list=[["1.Four", "2.Nine", "3.Seven", "4.Eight"],["1.Chandigarh", "2.Bhopal", "3.Chennai", "4.Delhi"],
["1.Software Engineering", "2.Counseling", "3.Tourism", "4.Agriculture"]]
solution_list=[3,4,1]
lifeline_solution=[["1.Nine","2.Seven"],["1.Chandigarh","2.Delhi"],["1.Software Engineering","2.Tourism"]]
lifeline_solution_list=[2,2,1]
Money=0
Amount=5000
Name=input("enter your name:")
print("welcome",Name,"to KBC")
i=0
count_lifeline=0
while i<len(question_list):
    print("Your question is on your screen:")
    print("Q.",question_list[i])
    print("Your options are")
    print(option_list[i])
    if count_lifeline==1:
        print("You have already used lifeline,you cannot use it any more")
        solution=int(input("choose your option: "))
        if solution==solution_list[i]:
            print("Yay!Your answer is correct")
            Money=Money+Amount
            print("Here you win an amount of",Money)
        else:
            print("better luck next time")
            break
    else:
        lifeline=input("enter yes if you want to use lifeline and no if you do not want: ")
        if lifeline=="yes":
            print("fifty-fifty options on your screen:")
            print(lifeline_solution[i])
            lifeline_solution_input=int(input("choose your option from fifty-fifty options:"))
            if lifeline_solution_input==lifeline_solution_list[i]:
                count_lifeline=count_lifeline+1
                # print(count_lifeline)

                print("you got this answer right")
                Money=Money+Amount
                print("Here you win an amount of",Money)
            else:
                print("try next time")
                break
        else:
            solution=int(input("choose your option: "))
            if solution==solution_list[i]:
                print("Yay!Your answer is correct")
                Money=Money+Amount
                print("Here you win an amount of",Money)
            else:
               print("better luck next time")
               break
    i=i+1
print("And here you get a total of",Money,"rupees")