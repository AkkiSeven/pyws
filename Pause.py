import turtle

wn = turtle.Screen()
wn.title("Game Pause Demo")
wn.bgcolor("black")

bob = turtle.Turtle()
bob.speed(0)
bob.color("yellow")
bob.shape("triangle")
bob.penup()

is_paused = False


def toggle_pause():
    global is_paused
    is_paused = not is_paused


wn.listen()
wn.onkeypress(toggle_pause, "space")

while True:
    if not is_paused:
        bob.fd(1)
        bob.lt(1)
    else:
        wn.update()
