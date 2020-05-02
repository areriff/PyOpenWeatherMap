from sense_hat import SenseHat
from time import sleep
sense = SenseHat()

def place(intensity):
    X = [intensity, 0, 0]  # Red
    O = [intensity, intensity, intensity]  # White
    LetterA = [
        O, O, O, X, X, O, O, O,
        O, O, X, O, O, X, O, O,
        O, O, X, O, O, X, O, O,
        O, X, O, O, O, O, X, O,
        O, X, X, X, X, X, X, O,
        O, X, O, O, O, O, X, O,
        X, O, O, O, O, O, O, X,
        X, O, O, O, O, O, O, X,
    ]
    sense.set_pixels(LetterA)

count = 100
while count > 0:
    place(count)
    sleep(0.2)
    count -= 10
