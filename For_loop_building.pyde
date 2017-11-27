def setup():
    size(400, 400)
def draw():
    background(255)
    fill(0)
    rect(0, 200, 100, 200)
    
    #(200= where it starts, 401= max, 30 is intervals)
    for y in range(210, 401, 30):
        for x in range(10, 100, 30):
            fill(255)
            rect(x, y, 20, 20)
        

    