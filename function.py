def pythagorean_theorem(a, b, unknown_side=None):
    if unknown_side == None or type(unknown_side) != str:
        return "Please insert unknown side as: Hypotenuse or Leg!"
    else:
        try:
            a - b
        except Exception as error_message:
            return f"ErrorMessage: {error_message}"
        else:
            if a <= 0 or b <= 0:
                return f"None of the triangle's side's length can be equal to 0, or smaller than 0!"
            else:
                if unknown_side.lower() == "hypotenuse":
                    c2 = (a ** 2) + (b ** 2)
                    c = c2 ** (1 / 2)
                    return f"Unknown hypotenuse's length is: {c}"

                elif unknown_side.lower() == "leg":
                    if a > b:
                        c2 = (a ** 2) - (b ** 2)
                        c = c2 ** (1 / 2)
                        return f"Unknown leg's length is: {c}"

                    elif a < b:
                        c2 = (b ** 2) - (a ** 2)
                        c = c2 ** (1 / 2)
                        return f"Unknown leg's length is: {c}"

                    elif a == b:
                        return f"ErrorMessage: Leg and hypotenuse can not be the same length!"

                    else:
                        return "Something went wrong!"
                else:
                    return "Please insert unknown side as: Hypotenuse or Leg!"


if __name__ == "__main__":
    print(pythagorean_theorem(8, 5, "leg"))
