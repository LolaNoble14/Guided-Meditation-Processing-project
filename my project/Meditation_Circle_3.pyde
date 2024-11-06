# Set up circle variables
# README.md file has reference for grow and shrink speed formula used 
radius = 50  # Starting radius of the circle
grow = True  # Boolean to track whether the circle is growing or shrinking
grow_speed = 0.28  # Speed for growing 6 seconds
shrink_speed = 0.42  # Speed for shrinking 4 seconds

def setup():
    size(400, 400)  # Canvas size
    background(255)  # White background
    frameRate(60)  # 60 frames per second

def draw():
    global radius, grow

    background(255)  # Keep the background white each frame
    noStroke()  # No border around the circle
    fill(209, 255, 185)  # circle filled light green colour

    # Circle growth and shrink logic adapted from Pho's answer on Stack overflow, "Python: How to make a circle grow and shrink"
    # Source: https://stackoverflow.com/questions/64449551/python-how-to-make-a-circle-grow-and-shrink, accessed on: 8/10/2024
    # Adapted through trial and error, above websites were used as a starting point and to understand the function
    if grow:
        radius += grow_speed  # Increase radius
        if radius >= 150:  # Max radius modified by me 
            grow = False  # Start shrinking
    else:
        radius -= shrink_speed  # Decrease radius
        if radius <= 50:  # Min radius
            grow = True  # Start growing again

    # Draw the circle radius
    # Code ellipseMode() retrieved from and published by Processing.py. (2024, February 27). ellipseMode(). Retrieved October 15, 2024, from https://py.processing.org/reference/ellipsemode
    # Customised by me is desired shape 
    ellipse(width / 2, height / 2, radius * 2, radius * 2)  # Circle at center
    
# textAlign retrieved from Processing.py. (2024, February 27). "textAlign()". Retrieved October 23, 2024, from https://py.processing.org/reference/textalign
# Placement, colour, size and writing was altered 
    fill(0, 0, 0) # Text colour was based on how circle was self set up
    textSize(20) # Text size was created based on canavas size was self set up  
    textAlign(CENTER, CENTER) # Code from Processing.py to align text to the center horizontally and vertically
    text("How are you feeling today?", width / 2, height - 30)  # Text placed bottom center
