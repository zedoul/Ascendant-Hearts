 
init -1:
    style textbox_window:
        background Frame("ui/textbox.png",0,0)
        yminimum 450
        #top_margin 100
        top_padding 200
        #background None
        # left_margin 500
        # right_margin 550
        # top_margin 6
        # bottom_margin 50
        left_padding 400
        right_padding 400
        bottom_padding 50
        # top_padding 60
        # bottom_padding 0
        # yminimum 300
    style say_dialogue:
        outlines [(1, "#000", 0, 0)]
        size 26
    style say_thought:
        outlines [(1, "#000", 0, 0)]
        size 26
    style say_label:
        outlines [(1, "#000", 0, 0)]
        size 36
        font "fonts/Delius-Regular.ttf"
        xpos 30
    style history_name_text:
        font "fonts/Delius-Regular.ttf"
        min_width gui.history_name_width
        color "#2980b9"
        size 50
        text_align gui.history_name_xalign