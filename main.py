def on_button_pressed_a():
    global hunger
    music.play_sound_effect(music.builtin_sound_effect(soundExpression.spring),
        SoundExpressionPlayMode.IN_BACKGROUND)
    basic.show_leds("""
        . . . . .
                . # . # .
                . . . . .
                # . # . #
                . # . # .
    """)
    basic.show_leds("""
        . . . . .
                . # . # .
                . . . . .
                . # . # .
                # . # . #
    """)
    basic.show_leds("""
        . . . . .
                . # . # .
                . . . . .
                # . # . #
                . # . # .
    """)
    basic.show_leds("""
        . . . . .
                . # . # .
                . . . . .
                # . . . #
                . # # # .
    """)
    hunger = 0
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_gesture_screen_up():
    global time
    time = 0
    basic.show_icon(IconNames.ASLEEP)
    basic.pause(10000)
    time += 1
    if True:
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.yawn),
            SoundExpressionPlayMode.IN_BACKGROUND)
        basic.show_icon(IconNames.ASLEEP)
        basic.show_leds("""
            . . . . .
                        . # . # .
                        . . . . .
                        . # # # .
                        . . . . .
        """)
        basic.show_icon(IconNames.HAPPY)
input.on_gesture(Gesture.SCREEN_UP, on_gesture_screen_up)

def on_button_pressed_b():
    global thirst
    music.play_sound_effect(music.builtin_sound_effect(soundExpression.twinkle),
        SoundExpressionPlayMode.IN_BACKGROUND)
    basic.show_leds("""
        # # # # #
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    """)
    basic.show_leds("""
        . . . . .
                # # # # #
                # # # # #
                # # # # #
                # # # # #
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                # # # # #
                # # # # #
                # # # # #
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                # # # # #
                # # # # #
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                # # # # #
    """)
    basic.show_icon(IconNames.HAPPY)
    thirst = 0
input.on_button_pressed(Button.B, on_button_pressed_b)

def on_gesture_shake():
    music.play_sound_effect(music.builtin_sound_effect(soundExpression.soaring),
        SoundExpressionPlayMode.IN_BACKGROUND)
    basic.show_icon(IconNames.ANGRY)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_logo_pressed():
    global mood
    music.play_sound_effect(music.builtin_sound_effect(soundExpression.giggle),
        SoundExpressionPlayMode.IN_BACKGROUND)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . . . . .
                . . # . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                . . . . .
                . # # # .
                . . # . .
    """)
    basic.show_leds("""
        . . . . .
                . . . . .
                # # # # #
                . # # # .
                . . # . .
    """)
    basic.show_leds("""
        . . . . .
                # # # # #
                # # # # #
                . # # # .
                . . # . .
    """)
    basic.show_icon(IconNames.HEART)
    basic.show_icon(IconNames.HAPPY)
    mood = 0
input.on_logo_event(TouchButtonEvent.PRESSED, on_logo_pressed)

time = 0
thirst = 0
mood = 0
hunger = 0
sleep = 0
hunger = 0
mood = 0
thirst = 0
music.play_sound_effect(music.builtin_sound_effect(soundExpression.yawn),
    SoundExpressionPlayMode.IN_BACKGROUND)
basic.show_icon(IconNames.ASLEEP)
basic.show_leds("""
    . . . . .
        . # . # .
        . . . . .
        . # # # .
        . . . . .
""")
basic.show_icon(IconNames.HAPPY)

def on_forever():
    global sleep, hunger, mood, thirst
    basic.pause(10000)
    sleep += 1
    basic.pause(5000)
    hunger += 1
    basic.pause(2000)
    mood += 1
    basic.pause(25000)
    thirst += 1
    if hunger >= 100:
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.soaring),
            SoundExpressionPlayMode.IN_BACKGROUND)
        basic.show_icon(IconNames.CONFUSED)
    if mood >= 0:
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.sad),
            SoundExpressionPlayMode.IN_BACKGROUND)
        basic.show_icon(IconNames.SAD)
    if sleep >= 0:
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.yawn),
            SoundExpressionPlayMode.UNTIL_DONE)
        basic.show_leds("""
            . . . . .
                        # # . # #
                        . . . . .
                        . # # # .
                        # . . . #
        """)
    if thirst >= 0:
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.spring),
            SoundExpressionPlayMode.UNTIL_DONE)
        basic.show_leds("""
            . # . # .
                        . . . . .
                        # # # # #
                        . # # . .
                        . # # . .
        """)
    if hunger == 200 or thirst == 200:
        music.play_sound_effect(music.builtin_sound_effect(soundExpression.mysterious),
            SoundExpressionPlayMode.IN_BACKGROUND)
        basic.show_icon(IconNames.SKULL)
basic.forever(on_forever)
