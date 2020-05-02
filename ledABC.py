from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

X = [255, 0, 0]  # Red
O = [255, 255, 255]  # White

blankLetter = [
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

sense.set_pixels(letterA)
sleep(0.5)
sense.set_pixels(LetterB)
sleep(0.5)
sense.set_pixels(LetterC)
sleep(0.5)
sense.clear()
