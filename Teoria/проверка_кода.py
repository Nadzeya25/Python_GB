def calc(action):
    data = action.split()
    sign = data[1]
    data = list(filter(lambda x: str(x).isdigit(), data))

    if sign == "*":
        answer = int(data[0]) * int(data[1])
    elif sign == "/":
        answer = [int(data[0]) / int(data[1]) if int(data[1]) != 0 and sign == "/" else print("Division for zero is forbidden. It's sad, sorry.")]
    elif sign == "+" or "-":
        answer = [int(data[0]) - int(data[1]) if sign == "-" else int(data[0]) + int(data[1])]
    else: print("I don't know this sign, try again.")

    return answer
print(calc("*"))
# def calc(action):
#     data = action.split()
#     sign = data[1]
#     data = list(filter(lambda x: str(x).isdigit(), data))

#     if sign == "*":
#         answer = int(data[0]) * int(data[1])
#     elif sign == "/":
#         answer = [int(data[0]) / int(data[1]) if int(data[1]) != 0 and sign == "/" else print("Division for zero is forbidden. It's sad, sorry.")]
#     elif sign == "+" or "-":
#         answer = [int(data[0]) - int(data[1]) if sign == "-" else int(data[0]) + int(data[1])]
#     else: print("I don't know this sign, try again.")

#     return answer