duck = "Six"
match duck:
    case "One":
        print("The value of duck is one")
    case "Two":
        print("the value of duck is two")
    case "Three":
        print("The value of duck is three")
    case "Four":
        print("The value of duck is four")
    case "Five":
        print("The value of duck is five") 
    case _:
        print("The value is none of the above")