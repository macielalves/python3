# Estudando python
import random
import turtle as t
from math import factorial
import math
import os
import shutil
# import classes as msg


def compare(x: int, y: int) -> int:
    """
    A função compara dois valores e retorna 1 se x maior que y, 0 se os valores forem iguais e -1 se x for menor que y
    """
    if x > y:
        return 1
    elif x == y:
        return 0
    elif x < y:
        return -1


def distancia_entre_dois_pontos(x1: int, y1: int, x2: int, y2: int):
    """A função calcula a distância entre dois pontos a e b, onde passamos como parâmetros as coordenadas dos números"""
    dx = x2 - x1
    dy = y2 - y1
    quadrado = dx ** 2 + dy ** 2
    return quadrado ** (1 / 2)


# print(distancia_entre_dois_pontos(1, 2, 4, 6))  #
# n / (n + 1) onde n=1 ao infinito


def hipotenusa():
    ca = 10  # dx
    co = 6  # dy
    hipo = ((co ** 2) + (ca ** 2)) ** (1 / 2)
    return hipo


# hipotenusa()


# website = "http://google.com"
#
# slice = slice(7, -4)
#
# print(website[slice])


# phone_number = "123-456-7890"
#
# for i in phone_number:
#     if i == '-':
#         continue  # não executa o bloco abaixo dele se for verdade(Pode haver correções futuras para essa afirmação)
#     print(i, end="")


# loop Control, pass, continue and break
#
# for i in range(1, 15):
#
#     if i == 10:
#         pass  # ignora o bloco
#     else:
#         print(i)


# listas
#
# coisas = ['mochila', 'sapato', 'cinto', 'copo', 'celular', 'chaves']
#
# coisas.remove('celular')  # remove um item pelo nome, ou característica do item
# coisas.pop(3) # remove um item da lista especificando o número referente ao item
# string = 'Botas'
# coisas.insert(0, string)  # insere um item na posição desejado
# coisas.sort()  # ordena em ordem crescente os termos da lista
# coisas.clear()  # remove todos os itens de uma lista
#
# for i in coisas:
#     print(i)


# 2D lists = a list of lists
#
# drinks = ["coffee", "soda", "tea"]
# dinner = ["pizza", "hamburger", "hotdog"]
# dessert = ["cake", "ice cream"]
#
# food = [drinks, dinner, dessert]
#
# print(food)


# tuple = collection which is ordered and unchangeable used to group together related data
#
# student = ("Bro", 21, "male")
#
# print(student.count("Bro"))
# print(student.index("male"))
#
# for i in student:
#     print(i)
#
# if "Bro" in student:
#     print("Bro is here!")
#
#
# set = collection which is unordered, un_indexed. No duplicate values
#
# utensils = {"fork", "spoon", "knife"}
# dishes = {"bowl", "plate", "cup", "knife"}
#
# utensils.add("napkin")  # adiciona o napkin
# utensils.remove("fork")  # remove o fork
# utensils.clear()  # limpa o set
#
# utensils.update(dishes)  # coloca os itens de dishes dentro de utensils
#
# dinner_table = utensils.union(dishes)  # une utensils e dishes
#
# print(utensils.difference(dishes))  # mostra qual a diferença de utensils para dishes
#
# print(utensils.intersection(dishes))  # mostra qual os valores iguais em ambos os sets
#
# for x in dinner_table:
#     print(x)


# dictionary = A changeable, unordered collection of unique key: value pairs
#              Fast because they use hashing, allow us to access a value quickly
#
# capitals = {'USA': 'Washington DC',
#             'India': 'New Deli',
#             'China': 'Beijing',
#             'Russia': 'Moscow'}
#
# capitals.update({'Germany': 'Berlin'})
# capitals.update({'USA': 'Las Vegas'})
# capitals.pop('China')
# capitals.clear()
#
# print(capitals.keys())
# print(capitals.values())
# print(capitals.items())
#
# print(capitals['Germany'])
# print(capitals.get('Germany'))
#
# for keys, values in capitals.items():
#     print(keys, values)


# index operator [] = gives access to a sequence's  element (str, list, tuples)
#
# name = "maciel Alves!"
#
# if (name[0].islower()):
#     name = name.capitalize()
#
# first_name = name[0:6].upper()
# last_name = name[7:].lower()
# last_character = name[-1]
#
# print(first_name)
# print(last_name)
# print(last_character)


# function = a block of code which is
#
# def hello(first_name, last_name, age):
#     print("Hello " + first_name + " " + last_name)
#     print("You are " + str(age) + " years old")
#     print("Have a nice day!")
#
#
# hello("Maciel", "Alves", 19)


# escopo de variáveis, locais e globais, para tornar uma local em global é preciso defini-la como 'global var'
#
# *args = parameter that will pack all arguments into a tuple
#         useful so that a function can accept a varying amount of arguments
#
# def add(*stuff):
#     sum = 0
#     stuff = list(stuff)
#     stuff[0] = 0
#     for i in stuff:
#         sum += i
#
#     return sum
#
#
# print(add(1, 2, 3, 4, 5, 6, 7, 8))


# **kwargs = parameter that will pack all arguments into a dictionary
#            useful so that a function can accept a varying amount of keyword argument
#
# def hello(**kwargs):  # pode-se usar outros nomes no lugar do nome kwargs
#     print("Hello", end=" ")  # + kwargs['first'] + " " + kwargs['middle'] + " " + kwargs['last'] + "!")
#     for key, value in kwargs.items():
#         print(value, end=" ")
#
#
# hello(first='Maciel', middle='Alves', last='Pereira')


# str.format() = optional method that gives users
#                more control when displaying output
#
# number = 3.14159
#
# print("The number pi is {:.3f}".format(number))  # formata um número de ponto flutuante um número de casas decimais
# print("The number is {:,}".format(number))
# print("The number is {:b}".format(number))
# print("The number is {:o}".format(number))
# print("The number is {:x}".format(number))
# print("The number is {:X}".format(number))
# print("The number is {:E}".format(number))
#
# animal = "cow"
# item = "moon"
#
# print("The {} jumped over the {}".format(animal, item))
# print("The {1} jumped over the {0}".format(animal, item))  # positional arguments
# print("The {animal} jumped over the {item}".format(animal="cow", item="moon"))  # keyword argument
#
# text = "The {} jumped over the {}"
# print(text.format(animal, item))
#
# name = "Maciel"
#
# print("Hello, my name is {}".format(name))
# # print("Hello, my name is {:10}".format(name))  # Alocar espaço para uma string
# print("Hello, my name is {:10}. Nice to meet you".format(name))
# print("Hello, my name is {:<10}. Nice to meet you".format(name))
# print("Hello, my name is {:>10}. Nice to meet you".format(name))
# print("Hello, my name is {:^10}. Nice to meet you".format(name))


# random numbers
#
# x = random.randint(1, 6)
# y = random.random()
#
# myList = ['rock', 'paper', 'scissors']
# z = random.choice(myList)
#
# cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]
#
# random.shuffle(cards)  # embaralhar
#
# print(cards)


# exception = events detected during execution that interrupt the flow of a program
#
#
# try:
#     numerator = int(input("Enter a number to divide: "))
#     denominator = int(input("Enter a number to divide by: "))
#     result = numerator / denominator
# except ZeroDivisionError as e:
#     print(e)
#     print("You can't divide by zero! idiot!")
# except ValueError as e:
#     print(e)
#     print("Enter only numbers plz")
# except Exception as e:
#     print(e)
#     print("something wong wrong :(")
# else:
#     print(result)
# finally:
#     print("This will always execution")


# file detection
# no windows é preciso usar \\ para no lugar da \ simples para acesso ao diretório
#
# path = "/home/mcy/Development/python3/OUTROS_PROJETOS/QUIZ/quiz.py"
#
# if os.path.exists(path):
#     print("Diretório encontrado!")
#     if os.path.isfile(path):
#         print("That is a file")
#     elif os.path.isdir(path):
#         print("That is a directory!")
# else:
#     print("O diretório não existe!")


# read a file
# try:
#     with open('tela_test.py') as file:
#         print(file.read())
# except FileNotFoundError:
#     print('That file was not found :(')
#
# # print(file.closed)
# # file.close()


# file write
#
# text = "Yooooooooooooo\nThis is some text\nHave a good one!\n"
#
# with open('tela_test.py', 'w') as file:
#     file.write(text)
#
# file.close()
#
# text2 = "Linha adicionada depois da ultima adição"
#
# with open('tela_test.py', 'a') as file:
#     file.write(text2)
#
# file.close()
#
# with open('tela_test.py', 'r') as file:
#     print(file.read())


# -----------------------------------------------------------------------------
# copy a file
#
# shutil.copyfile('tela_test.py', 'copy.txt')  # src, dst, source e destination
# shutil.copy('tela_test.py', '../copy.txt')
# shutil.copy2('tela_test.py', '../copy2.txt')


# move a file
#
# source = '../ANALISE/copy.txt'
# destination = 'copy.txt'
#
# try:
#     if os.path.exists(destination):
#         print("There is already a file there")
#     else:
#         os.replace(source, destination)
#         print(source+" was moved")
# except FileNotFoundError:
#     print(source+" was not found")


# delete a file
#
#
# path = 'teste'
#
# try:
#     # os.remove(path)
#     # os.rmdir(path)  # remove diretórios vazios
#     # shutil.rmtree(path)  # remove toda a árvore de diretório especificado
# except FileNotFoundError:
#     print("That file was not found")
# except PermissionError:
#     print("You do not have permission to delete that")
# except OSError:
#     print("You cannot delete that using that function")
# else:
#     print(path+" was deleted")


# module = a file containing python code. May contain function, classes, etc.
# Used with modular programing, which is to separate a program into parts
#
# msg.hello()
# msg.bye()


# help("modules")


# rock, paper, scissors game
#
# while True:
#     choices = ["rock", "paper", "scissors"]
#
#     computer = random.choice(choices)
#     player = None
#
#     while player not in choices:
#         player = input("rock, paper or scissors?: ").lower()
#
#     if player == computer:
#         print("Computer: ", computer)
#         print("Player: ", player)
#         print("Tie!")
#     elif player == "rock":
#         if computer == "paper":
#             print("Computer: ", computer)
#             print("Player: ", player)
#             print("You lose!")
#         elif computer == "scissors":
#             print("Computer: ", computer)
#             print("Player: ", player)
#             print("You win!")
#     elif player == "scissors":
#         if computer == "paper":
#             print("Computer: ", computer)
#             print("Player: ", player)
#             print("You lose!")
#         elif computer == "rock":
#             print("Computer: ", computer)
#             print("Player: ", player)
#             print("You win!")
#     elif player == "paper":
#         if computer == "rock":
#             print("Computer: ", computer)
#             print("Player: ", player)
#             print("You lose!")
#         elif computer == "scissors":
#             print("Computer: ", computer)
#             print("Player: ", player)
#             print("You win!")
#
#     play_again = input("Play again? (yes/no): ").lower()
#     if play_again != "yes":
#         break
#
# print("Bye!")


# # quiz game
#
# # --------------------------------------------
# def new_game():
#
#     guesses = []
#     correct_guesses = 0
#     questions_num = 1
#
#     for key in questions:
#         print("-----------------------------")
#         print(key)
#         for i in options[questions_num-1]:
#             print(i)
#         guess = input("Enter (A, B, C or D): ")
#         guess = guess.upper()
#         guesses.append(guess)
#
#         correct_guesses += check_answer(questions.get(key), guess)
#         questions_num += 1
#
#     display_score(correct_guesses, guesses)
#
#
# # --------------------------------------------
# def check_answer(answer, guess):
#
#     if answer == guess:
#         print("CORRECT!")
#         return 1
#     else:
#         print("WRONG!")
#         return 0
#
#
# # --------------------------------------------
# def display_score(correct_guesses, guesses):
#     print("-----------------------------")
#     print("RESULTS")
#     print("-----------------------------")
#     print("Answers: ", end="")
#     for i in questions:
#         print(questions.get(i), end="")
#     print()
#
#     print("Guesses: ", end="")
#     for i in guesses:
#         print(i, end="")
#     print()
#
#     score = int((correct_guesses/len(questions))*100)
#     print("Your score is: "+str(score)+"%")
#
#
# # --------------------------------------------
# def play_again():
#     response = input("Do you want to play again? (yes or no): ")
#     response = response.upper()
#
#     if response == "YES":
#         return True
#     else:
#         return False
# # --------------------------------------------
#
#
# questions = {
#     "Who created Python?: ": "A",
#     "What year was Python created?: ": "B",
#     "Python is tributed to which comedy group?: ": "C",
#     "Is the Earth round?: ": "A"
# }
#
# options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerberg"],
#            ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
#            ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
#            ["A. True", "B. False", "C. sometimes", "D. What's Earth?"]]
#
# new_game()
#
# while play_again():
#     new_game()
#
# print("Byeeee!")


# Object-Oriented Programming (OOP)
class Car:

    wheels = 4  # Variáveis de uma classe

    def __init__(self, make, model, year, color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("This "+self.model+" is driving")

    def stop(self):
        print("This "+self.model+" is stopped")


