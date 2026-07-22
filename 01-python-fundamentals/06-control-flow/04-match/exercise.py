day = "Monday"

match day:
    case "Monday":
        print("Start of the week")
    case "Thursday":
        print("Almost weekend")
    case "Saturday":
        print("Weekend")
    case _:
        print("Invalid day")



fruit = Banana

match fruit:
    case "Apple":
        print("Red")
    case "Banana":
        print("Yellow")
    case "Orange":
        print("Orange")
    case _:
        print("Unknown fruit")



command = "start"

match command:
    case "start":
        print("You can proceed")
    case "stop":
        print("You need to stop here")
    case "restart":
        print("Time to start again")
    case _:
        print("Invalid commabd")

Exercise 4

Without running the code, determine the output.

status = "error"

match status:

    case "loading":
        print("Loading")

    case "success":
        print("Done")

    case _:
        print("Unknown")

Answer : Unknown