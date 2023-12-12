from colorama import init, Fore
import random
import string

init()

text = """
##########################################
#####1111111######1111111####11#######1###
####1#############1##########1#1######1###
###1##############1##########1##1#####1###
###1##############1111111####1###1####1###
###111111111######1##########1####1###1###
###1########1#####1##########1####1##1####
###1########1#####1##########1######1#1###
####11111111######1111111####1#######11###
##########################################
##########################################

"""


colored_text = text.replace('1', Fore.BLUE + '1').replace('#', Fore.YELLOW + '#')
print(colored_text)

while True:
    print(Fore.BLUE + "What you want to generate?")
    print(Fore.YELLOW + "1.Amazon\n"
                        "2.Steam\n"
                        "3.Working on it\n"
                        "4.Working on it\n"
                        "5.Working on it\n"
                        "5.Exit")
    user_choice = input()

    if user_choice == "1" or user_choice == "Amazon" :
        def generate_code(length):
            letters_and_digits = string.ascii_uppercase + string.digits
            code = ''.join(random.choice(letters_and_digits) for _ in range(length))
            return code


        def generate_multiple_codes(num_codes, length):
            codes = [generate_code(length) for _ in range(num_codes)]
            return codes


        num_of_codes = int(input("Enter codes count: "))
        code_length = random.choice([14, 15])


        generated_codes = generate_multiple_codes(num_of_codes, code_length)


        print("Generated codes:")
        for code in generated_codes:
            print(code)

    elif user_choice == "2" or user_choice == "Steam":
        def generate_code():
            code = '-'.join(
                ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(5)) for _ in range(3))
            return code



        num_of_codes = int(input("Enter codes count: "))


        generated_codes = [generate_code() for _ in range(num_of_codes)]


        print("Generated codes:")
        for code in generated_codes:
            print(code)


    elif user_choice == "exit" or user_choice == "Exit":
        print("Okay, finish")
        break
    else:
        print("Sorry, but now i don't now this code.")
