# You can place the script of your game in this file.

# Declare images below this line, using the image statement.
# eg. image eileen happy = "eileen_happy.png"

# Declare characters used by this game.
define e = Character('Shiori',color="#fff")
image healer small = "healer.png"
image side healer = "normal.png"
image mage = "mage.png"
image rogue = "rogue.png"
# The game starts here.
label start:
    scene bg fountain
    show healer small:
    #   xalign 0.85 yalign 1.0 zoom 0.70
    # show mage onlayer middle:
    #     xalign 0.50 yalign 1.0 zoom 0.70
    # show rogue onlayer middle:
    #     xalign 0.10 yalign 1.0 zoom 0.70

    with dissolve
    e "I  open my eyes and squint at bright sunlight. I’m outside, on the ground. When my eyes adjust, I ease myself up and look around. It’s some sort of town square, with a beautiful water fountain to my right."
    e "You've created a new Ren'Py game."

    e "Once you add a story, pictures, and music, you can release it to the world!"
    e "time to move the camera"
    e "does this work?"

    menu:
        "lol":
            "gogo"

        "RPG dragon slaying monsters":
            "slain"
    return
