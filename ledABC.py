from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

X = [255, 0, 0]  # Red
O = [255, 255, 255]  # White

Letter = [
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
O, O, O, O, O, O, O, O,
]

letterA = [
O, O, O, X, X, O, O, O,
O, O, X, O, O, X, O, O,
O, O, X, O, O, X, O, O,
O, X, O, O, O, O, X, O,
O, X, X, X, X, X, X, O,
O, X, O, O, O, O, X, O,
X, O, O, O, O, O, O, X,
X, O, O, O, O, O, O, X,
]

LetterB = [
O, X, X, X, X, O, O, O,
O, X, O, O, O, X, O, O,
O, X, O, O, O, X, O, O,
O, X, X, X, X, O, O, O,
O, X, O, O, O, X, O, O,
O, X, O, O, O, O, X, O,
O, X, O, O, O, X, O, O,
O, X, X, X, X, O, O, O,
]

LetterC = [
O, O, O, X, X, X, X, O,
O, X, X, O, O, O, O, O,
X, O, O, O, O, O, O, O,
X, O, O, O, O, O, O, O,
X, O, O, O, O, O, O, O,
X, O, O, O, O, O, O, O,
O, X, X, O, O, O, O, O,
O, O, O, X, X, X, X, O,
]

LetterD = [
O, X, X, X, O, O, O, O,
O, X, O, O, X, X, O, O,
O, X, O, O, O, O, X, O,
O, X, O, O, O, O, X, O,
O, X, O, O, O, O, X, O,
O, X, O, O, O, O, X, O,
O, X, O, O, X, X, O, O,
O, X, X, X, O, O, O, O,
]

LetterE = [
O, X, X, X, X, X, X, O,
O, X, O, O, O, O, O, O,
O, X, O, O, O, O, O, O,
O, X, X, X, X, O, O, O,
O, X, O, O, O, O, O, O,
O, X, O, O, O, O, O, O,
O, X, O, O, O, O, O, O,
O, X, X, X, X, X, X, O,
]

LetterF = [
O, X, X, X, X, X, X, O,
O, X, O, O, O, O, O, O,
O, X, O, O, O, O, O, O,
O, X, X, X, X, O, O, O,
O, X, O, O, O, O, O, O,
O, X, O, O, O, O, O, O,
O, X, O, O, O, O, O, O,
O, X, O, O, O, O, O, O,
]

sense.set_pixels(letterA)
sleep(0.5)
sense.set_pixels(LetterB)
sleep(0.5)
sense.set_pixels(LetterC)
sleep(0.5)
sense.set_pixels(LetterD)
sleep(0.5)
sense.set_pixels(LetterE)
sleep(0.5)
sense.set_pixels(LetterF)
sleep(0.5)
sense.clear()
