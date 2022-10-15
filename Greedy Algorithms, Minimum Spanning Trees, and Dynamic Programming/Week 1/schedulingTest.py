import scheduling

def main():
    inp = input("Order the schedule by the ratio or difference?\n")
    choices = ["ratio","difference"]
    if inp not in choices: return
    elif inp == "ratio":
        arr = scheduling.optSchedule()
        print(scheduling.cost(arr))
    else:
        arr = scheduling.diffSchedule()
        print(scheduling.cost(arr))

main()