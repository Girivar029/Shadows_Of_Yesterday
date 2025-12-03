import pygame
import sys

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((600, 400))
pygame.display.set_caption("Shadows Of Yesterday")
font = pygame.font.SysFont(None, 28)

BUTTON_WIDTH = 240
BUTTON_HEIGHT = 44
BUTTON_MARGIN = 16
SCREEN_WIDTH, SCREEN_HEIGHT = screen.get_size()
TEXT_WRAP_WIDTH = SCREEN_WIDTH - 120  # Padding both sides for text wrapping

def wrap_text(text, font, max_width):
    words = text.split(' ')
    lines = []
    current_line = ""
    for word in words:
        test_line = current_line + word + " "
        if font.size(test_line)[0] <= max_width:
            current_line = test_line
        else:
            lines.append(current_line.strip())
            current_line = word + " "
    if current_line:
        lines.append(current_line.strip())
    return lines

def type_text(surface, text, font, x, y, max_width, line_height=32, delay=30):
    lines = wrap_text(text, font, max_width)
    surface.fill((17, 13, 28))  # Clear full background at each new scene

    for line_index, line in enumerate(lines):
        rendered_text = ""
        line_y = y + line_index * line_height
        for char in line:
            rendered_text += char
            # Clear just this line area before redrawing to avoid flicker
            surface.fill((17, 13, 28), (x, line_y, max_width, line_height))
            text_render = font.render(rendered_text, True, (255, 255, 255))
            surface.blit(text_render, (x, line_y))
            pygame.display.update(pygame.Rect(x, line_y, max_width, line_height))
            pygame.time.wait(delay)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
    # Return bottom y coord of last line for buttons placement
    return y + len(lines) * line_height

def draw_button(surface, y, text):
    rect = pygame.Rect(0, 0, BUTTON_WIDTH, BUTTON_HEIGHT)
    rect.center = (SCREEN_WIDTH // 2, y)
    pygame.draw.rect(surface, (40, 40, 60), rect)
    pygame.draw.rect(surface, (220, 220, 220), rect, 2)
    text_render = font.render(text, True, (220, 220, 220))
    text_rect = text_render.get_rect(center=rect.center)
    surface.blit(text_render, text_rect)
    return rect

def wait_for_choice(choices, button_start_y=300):
    button_rects = []
    # Clear only the button area so text above remains visible
    clear_height = SCREEN_HEIGHT - button_start_y
    screen.fill((17, 13, 28), (0, button_start_y - 10, SCREEN_WIDTH, clear_height))

    for i, (text, _) in enumerate(choices):
        y = button_start_y + i * (BUTTON_HEIGHT + BUTTON_MARGIN)
        rect = draw_button(screen, y, text)
        button_rects.append((rect, _))
    pygame.display.flip()

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = event.pos
                for rect, func in button_rects:
                    if rect.collidepoint(pos):
                        return func

scene_manager = None

class ChapterStart:
    def __init__(self,manager):
        self.manager = manager

    def ch1(self):
        type_text(screen,
            "Chapter 1: A New Morning(Note: Bring a pen out maybe start noting things down)",
            font, 60, 60, TEXT_WRAP_WIDTH)
        return wait_for_choice([
            ("Start", self.wake_up)
        ])

    def wake_up(self):
        type_text(screen,
            "You wake up .... again???, in this place you call home.",
            font, 60, 60, TEXT_WRAP_WIDTH)
        return wait_for_choice([
            ("Look at watch", self.look_watch),
            ("Stay in bed", self.stay_in_bed)
        ])

    def look_watch(self):
        type_text(screen,
            "It's 7:00 AM, 24th of July",
            font, 60, 60, TEXT_WRAP_WIDTH)
        return wait_for_choice([
            ("Stay in bed", self.stay_in_bed),
            ("Wake up", self.up_morning)
        ])

    def stay_in_bed(self):
        type_text(screen,
            "You lay down again, not really sleepy, contemplating this time",
            font, 60, 60, TEXT_WRAP_WIDTH)
        return wait_for_choice([
            ("Wake up", self.wake_up),
            ("Try Sleeping", self.try_sleep_morning)
        ])

    def try_sleep_morning(self):
        type_text(screen,
            "You try to fall asleep but you feel weird.",
            font, 60, 60, TEXT_WRAP_WIDTH)
        return wait_for_choice([
            ("Wake up again", self.up_morning),
            ("Try to sleep", self.try_sleep_morn_end)
        ])

    def up_morning(self):
        type_text(screen,
            "You look around in your empty room, and decide to go outside",
            font, 60, 60, TEXT_WRAP_WIDTH)
        return wait_for_choice([
            ("Greet a man walking by", self.greet_morning),
            ("Go for a jog", self.morn_jog)
        ])

    def try_sleep_morn_end(self):
        type_text(screen,
            "Vqtb P kfku ekmrydN, you mumble before passing out!",
            font, 60, 60, TEXT_WRAP_WIDTH)
        return wait_for_choice([
            ("Wake Up", self.wake_up),
            ("Wake up", self.wake_up)
        ])

    def greet_morning(self):
        type_text(screen,
            "Hi! Mr...., you forget his name. 'Hello boy' replies the old man.",
            font, 60, 60, TEXT_WRAP_WIDTH)
        return wait_for_choice([
            ("Go for a jog", self.morn_jog),
            ("Chat longer", self.chat_longer)
        ])

    def morn_jog(self):
        type_text(screen,
            "You start jogging, panting with every step, cursing yourself in the process",
            font, 60, 60, TEXT_WRAP_WIDTH)
        return wait_for_choice([
            ("Push yourself", self.push_jog),
            ("Buy some water", self.buy_water)
        ])
    
    def push_jog(self):
        type_text(screen,
                  "You try pusing yourself, but end up fainting, but before that see a shadow of yourself similing at your pain.",
                  font,60,60,TEXT_WRAP_WIDTH)
        return wait_for_choice([
            ("Wake up?",self.ch2),
            ("Wake up again",self.wake_up)
        ])
    
    def buy_water(self):
        type_text(screen,
                  "You find a shop and enter, finding nobody, so you find the water over there and take it before anyone comes back.",
                   font,60,60,TEXT_WRAP_WIDTH)
        return wait_for_choice([
            ("Drink the water",self.drink)
        ])
    
    def drink(self):
        type_text(screen,
                  "You drink the water to cool yourself down, but start hearing a voice as you fresh up. It sounds like you but you fear it.",
                  font,60,60,TEXT_WRAP_WIDTH)
        return wait_for_choice([
            ("Ignore it",self.ingone)
        ])
    
    def ingone(self):
        type_text(screen,
                  "You try avoiding the voice but it only gets louder, the voice making you tremble. You close your eyes and then ....",
                  font,60,60,TEXT_WRAP_WIDTH)
        return wait_for_choice([
            ("Wake up?", self.ch2)
        ])


    def chat_longer(self):
        type_text(screen,
                  "What is happening?, you ask. Seems eerily quiet today! Don't you know, he replied, as he walked away smiling",
                  font,60,60,TEXT_WRAP_WIDTH)
        return wait_for_choice([
            ("Go for a jog",self.morn_jog),
            ("Go Home",self.home_after_chat)
        ])
    
    def home_after_chat(self):
        type_text(screen,
                  "You lay down not understanding, what to do? You hear a strange voice, a version of you crying.",
                  font,60,60,TEXT_WRAP_WIDTH)
        return wait_for_choice([
            ("Ignore it",self.ignore_it)
        ])
    
    def ignore_it(self):
        type_text(screen,
                  "You ignore the crying voice in your head, but it grows louder, you close your eyes and scream in pain.",
                  font,60,60,TEXT_WRAP_WIDTH)
        return wait_for_choice([
            ("Wake up???",self.ch2)
        ])
    
    def ch2(self):
        type_text(screen,
                  "You wake up to a new day, after the wierd things which happened to you",
                  font,60,60,TEXT_WRAP_WIDTH)
        return self.manager.chapter2.intro
    
class Chapter2:
    def __init__(self,manager):
        self.manager = manager

    def intro(self):
        type_text(screen,
                  "Chapter 2: A new beginning",
                  font,60,60,TEXT_WRAP_WIDTH)
        return wait_for_choice([
            ("Look at clock",self.clock),
            ("Go back to Sleep",self.sleep)
        ])
    
    def clock(self):
        type_text(screen,
                  "You check the digital clock, it shows 7:00 AM, 24th of July, confusing you.",
                  font,60,60,TEXT_WRAP_WIDTH)
        return wait_for_choice([
            ("Question youself",self.quiestion),
            ("Carry on",self.check_outside)
        ])
    
    def quiestion(self):
        type_text(screen,
                  "You pinch youself to check if you are dreaming, to a point of scratching your skin off. And it definitely hurts.",
                  font,60,60,TEXT_WRAP_WIDTH)
        return wait_for_choice([
            ("Put a bandaid", self.bandaid),
            ("Go Outside",self.check_outside)
        ])
    
    def bandaid(self):
        type_text(screen,
                  "You find a bandaid from your box and put a fresh bandaid on your forearm. You also notice a lot of bandaids here.",
                  font,60,60,TEXT_WRAP_WIDTH)
        return wait_for_choice([
            ("Go Outside",self.check_outside),
            ("Check The Box",self.box)
        ])
    
    def box(self):
        type_text(screen,
                  "You find a note on the box, it's from your mom. It reads 'Make sure to apply bandaids everytime you get hurt, do not bleed out like the other times'. You wonder, not understanding anything.",
                  font,60,60,TEXT_WRAP_WIDTH)
        return wait_for_choice([
            ("Think Harder",self.think),
            ("Go outside",self.check_outside)
        ])
    
    def think(self):
        type_text(screen,
                  "You get slight glimpses of the past, someone harming you, then you applying bandaids at all these places. This memory makes you sweat.",
                  font,60,60,TEXT_WRAP_WIDTH)
        return wait_for_choice([
            ("Go outside",self.check_outside)
        ])
    
    def check_outside(self):
        type_text(screen,
                  "You walk outside to find a bustling road, with cars and people walking around. You also notice the man",
                  font,60,60,TEXT_WRAP_WIDTH)
        return wait_for_choice([
            ("Greet The Man",self.greet),
            ("Go for a jog",self.jog)
        ])
    
    def greet(self):
        type_text(screen,
                  '"Hi Mr.Jager, how is it going?" you ask, seemingly remembering his name. He greets back and asks about the wound in your forearm.',
                  font,60,60,TEXT_WRAP_WIDTH)
        return wait_for_choice([
            ("Tell The Truth",self.truth),
            ("Lie",self.lie),
            ("Walk Away",self.walk_away)
    ])

    def truth(self):
        type_text(screen,
                  "I pinched myself after a bad dream you say. He nods, asking you to be careful with your body and walks away.",
                  font,60,60,TEXT_WRAP_WIDTH)
        return wait_for_choice([
            ("Go for jog",self.jog),
            ("Go Back Home",self.home)
        ])
    
    def jog(self):
        type_text(screen,
                  "You go for a jog, listening to music. You don't notice the car driving and end up getting hit and fainting.",
                  font,60,60,TEXT_WRAP_WIDTH)
        return wait_for_choice([
            ("Wake Up",self.ch3)
        ])
    
    def home(self):
        type_text(screen,
                  "You walk back into your home, still in pain, go to sleep",
                  font,60,60,TEXT_WRAP_WIDTH)
        return wait_for_choice([
            ("Wake Up",self.ch3)
        ])
    
    def lie(self):
        type_text(screen,
                  "You tell him you accidently hit yourself while hammering a nail. He looks at your frail body, laughs and walks away.",
                  font,60,60,TEXT_WRAP_WIDTH)
        return wait_for_choice([
            ("Ignore and Jog",self.jog),
            ("Confront",self.confront)
        ])
    
    def confront(self):
        type_text(screen,
                  "You try to confront him, but miss the truck passing by which ends up hitting you and pass out.",
                  font,60,60,TEXT_WRAP_WIDTH)
        return wait_for_choice([
            ("Wake Up",self.ch3)
        ])
    
    
    def sleep(self):
        type_text(screen,
                  "You try sleeping but are woken up by the noise of the poeple outside.",
                  font,60,60,TEXT_WRAP_WIDTH)
        return wait_for_choice([
            ("Check Outside",self.check_outside),
            ("Check Clock",self.clock)
        ])
    
    def ch3(self):
        type_text(screen,
                  "You wake up, a new day!                                                                                                                                            ",font,60,60,TEXT_WRAP_WIDTH)
        return self.manager.chapter3.intro

def scr(text):
    return type_text(screen,text,font,60,60,TEXT_WRAP_WIDTH)

class Chapter3:
    def __init__(self, manager):
        self.manager = manager

    def intro(self):
        scr("Chapter 3: A New Day?")
        return wait_for_choice([
            ("Check clock",self.clock),
            ("Check surroundings",self.surroundings)
        ])
    
    def surroundings(self):
        scr("You check on all sides finding nothing new, just your room but you see marks of nail scratches in the walls, hidden away in the fresh coat of paint.")
        return wait_for_choice([
            ("Check Walls",self.walls)
        ])
    
    def walls(self):
        scr("You check the walls, and also your nails but do not find any marks in your hand.")
        return wait_for_choice([
            ("Check Clock",self.clock),
            ("Go Outside",self.outside)
        ])
    
    def clock(self):
        scr("You check the clock, it is the same 7:00 AM, 24th of July, you just want to walk out at this point.")
        return wait_for_choice([
            ("Walk Out",self.outside)
        ])
    
    def outside(self):
        scr("You go out and find Mr.Jager again.")
        return wait_for_choice([
            ("Gree Mr.Jager",self.greet),
            ("Walk Safely",self.walk)
        ])
    
    def greet(self):
        scr("Hello Mr.Jager, you greet. He greets back and continues walking.")
        return wait_for_choice([
            ("Go for a walk",self.walk),
            ("Check your phone",self.phone)
        ])
    
    def phone(self):
        scr("You check your phone and turns out you have school today, so you go home, ready and rush to school. But on the way to school, you find a man thirsty so you decide to help him.")
        return wait_for_choice([
            ("Give some water",self.give),
            ("Walk Away",self.away)
        ])
    
    def away(self):
        scr("You walk away not really caring, .. / ... . . / -.-- --- ..- .-. / -... .-.. --- --- -.. -.-- / -... .- -.-. -.- .-.-.- he played on the wall")
        return wait_for_choice([
            ("Keep Walking",self.die)
        ])
    
    def die(self):
        scr("You keep walking but somehow get caught in a robbery and are stabbed in the back. You faint with your back aching and bleeding.")
        return wait_for_choice([
            ("Wake Up",self.ch4)
        ])
    
    def give(self):
        scr("You give him some water, he smiles back, telling you to wait a while before leaving to save yourself from danger. You take his word lightly and continue walking. You get caught in a chain snatching and are stabbed in the back. You close your eyes and")
        return wait_for_choice([
            ("Wake Up",self.ch4)
        ])
    
    def walk(self):
        scr("You walk, more careful then ever, making sure to look everywhere to make sure whatever happened before to not happen.")
        return wait_for_choice([
            ("Go buy water",self.shop),
            ("Keep walking",self.more_walk)
        ])
    
    def shop(self):
        scr("You enter the shop and buy some water, the shopkeeper oddly asks you whether you want to buy some bandages, but you keep moving.")
        return wait_for_choice([
            ("Keep Walking",self.more_walk)
        ])
    
    def more_walk(self):
        scr("You keep walking but are caught in the crossfire of a chain snatching and end up getting stabbed in the back.")
        return wait_for_choice([
            ("Wake Up",self.ch4)
            ])
    
    def ch4(self):
        scr("You wake up in you room, again.")
        return wait_for_choice([
            ("Chapter 4",self.manager.chapter4.intro)
        ])
    
class Chapter4:
    def __init__(self,manager):
        self.manager = manager

    def intro(self):
        scr("You wake up again and rush to the clock, only to find the day is still the 24th of July and it is 7:00 AM, this confuses and you have a very weird feeling about this but cannot express this to anyone or can you.")
        return wait_for_choice([
            ("Walk Out",self.out),
            ("Think Through",self.think)
        ])
    
    def think(self):
        scr("You think about this a lot, trying to explain this situation which is happening to you and find no answer. You try pinching yourself again and it definitely hurts.")
        return wait_for_choice([
            ("Walk Out",self.out),
            ("Think Harder",self.think_harder)
        ])
    
    def think_harder(self):
        scr("You see yourself sweating, wipe the sweat off your face and sit down in a chair to think this through better, you think of many reasons but it all seems fantastical, everything seems like something out of a movie. All of it from the way you always wake back up to the same day and time. But you also think that this could be a dream a very bad one in that, not knowing what to do, you decide to test one of the theories out.")
        return wait_for_choice([
            ("Dream Theory",self.dream),
            ("Time Loop Theory",self.time_loop)
        ])
    
    def time_loop(self):
        scr("You think that there is only one way to test this theory out, but it may risk your life. Yet you stand in the top of your terrace looking down, scared by the height and step back in the last moment, not wanting to lose your life to test out some stupid theory.")
        return wait_for_choice([
            ("Walk Out",self.out)
        ])
    
    def dream(self):
        scr("Still not convinced by the pinch earlier decide to poke yourself with a needle, you touch your arm with it slightly, as it touches you feel the pain coursing along your arm, making it feel worse than it already was(but there is no bandaid in hand). You go to your box of bandaids and put one in your forearm.")
        return wait_for_choice([
            ("Walk Out",self.out)
        ])
    
    def out(self):
        scr("You walk out and greet Mr.Juger, he greet you back and enquires about the bandaid you are wearing. You tell him a half baked lie, he doesn't seem to notice and asks you to be more careful with your own body and to remember to wear bandaids if you ever get hurt. You nod and ...")
        return wait_for_choice([
            ("Walk away",self.walk),
            ("Ask Him",self.ask_juger)
        ])
    
    def ask_juger(self):
        scr("Before going you think about what to ask, are you gonna explain the situation to him or are you gonna ask him about this without revealing details.")
        return wait_for_choice([
            ("Tell Truth",self.truth),
            ("Tell Lie",self.lie)
        ])
    
    def lie(self):
        scr("You ask Mr.Juger about hallucinations and time loops, he laughs it off saying that may be only possible in fantasy but not in real life. You nod, saying you understand and keep walking.")
        return wait_for_choice([
            ("Keep Walking",self.walk)
        ])
    
    def truth(self):
        scr("You confess to Mr.Juger about your situation, he asks you to calm down and focus on the present, and tells you to stay safe. 'Focus on the present', these words keep repeating in your mind, playing like a broken record.")
        return wait_for_choice([
            ("Walk Away",self.walk)
        ])
    
    def walk(self):
        scr("You walk away as safe as ever, slowly and cautiously through the road. You end up noticing the car pass by peacefully and chose to ignore the chain snatching taking place. You now ...")
        return wait_for_choice([
            ("Be more careful",self.careful),
            ("Find Thirsty Man",self.man)
        ])
    
    def man(self):
        scr("You look around to find a man you have seen before asking for some water atleast remember seeing someone like this, so you approach the same shop and try finding this man. You find him, sitting in the exact spot, what next?")
        return wait_for_choice([
            ("Buy Him Water",self.buy_man_water),
            ("Ask Questions",self.ask_man)
        ])
    
    def ask_man(self):
        scr("You want to ask the man few questions, but what will you ask and how will a homeless man in the middle of nowhere know the answers to your questions.")
        return wait_for_choice([
            ("Walk Away",self.walk_away)
        ])
    
    def buy_man_water(self):
        scr("You go to the shop, buy the man some water and give it to him. He takes it, thanks you and tells you to take care of your wounds. This seems very odd to you but you decide to move on anyway as, he may as well be a mad man.")
        return wait_for_choice([
            ("Walk Away",self.walk_away)
        ])
    
    def walk_away(self):
        scr("You walk in the direction of your school as you have to be there today, and decide to forget everything that has happened so far and move on to have a normal day at school.")
        return wait_for_choice([
            ("Enter School",self.school)
        ])
    
    def school(self):
        scr("You enter your school, walk to your class and occupy your bench, you have arrived very early today so you decide to wait for a while for others.")
        return wait_for_choice([
            ("Look Around",self.look_school),
            ("Sit and Wait",self.wait)
        ])
    
    def look_school(self):
        scr("You look around in your classroom, find nothing new, just images of your class in trips and expeditions but can hardly recognise yourself in those images, you seem sad in them, dissacioated from everyone else in the group, almost as if you have no firends or as if everyone is delibrately avoiding you.")
        return wait_for_choice([
        ("Sit and Wait",self.wait)
        ])
    
    def wait(self):
        scr("You wait around for a while, a lot longer than you expect, but find nobody around, it is as if there was no school today in the first place, you walk around the school trying to find if anyone is there. All you find is empty rooms and a TV running in the staff room, talking about a virus spreading in the town and schools being cancelled due to that.")
        return wait_for_choice([
            ("Wake Up?",self.ch5)
        ])
    
    def ch5(self):
        scr("You wake up again, now with a plan to do something this time.")
        return wait_for_choice([
            ("Test Hypothesis",self.manager.chapter5_1.intro),
            ("Ask Questions",self.manager.chapter5_2.intro)
        ])
    
class Chapter5_1:
    def __init__(self, manager):
        self.manager = manager

    def intro(self):
        scr("Chapter 5: An instinctive decision")
        return wait_for_choice([
            ("Continue", self.do)
        ])

    def do(self):
        scr("You wake up this day, trying to comprehend the situation you are in. Fed up with the continuous day loop, you decide to try things just to check the limits of this.")
        return wait_for_choice([
            ("Try out pain", self.pain)
        ])

    def pain(self):
        scr("You test the limits of pain you can mentally handle, from aggravating old aches to replaying many of your past accidents, almost reliving every injury from the previous times.")
        return wait_for_choice([
            ("Calm down", self.calma)
        ])

    def calma(self):
        scr("You calm down, breathing slowly and reinterpreting all the knowledge you have gathered so far. Almost anything you do still makes you wake up in the same day. You tried everything you can to hurt yourself but everything leads you back to this place, on the same day and time. You suddenly feel pain...")
        return wait_for_choice([
            ("Faint", self.faint)
        ])

    def faint(self):
        scr("You faint and wait for the moment to wake back up again, but that doesn't happen. Instead, you hear a man crying, someone with pain all over their body. You can sense it but cannot pinpoint how.")
        return wait_for_choice([
            ("Listen more", self.more_patience)
        ])

    def more_patience(self):
        scr("You patiently listen more. You hear the man describing all the pain in his body, which feels really uncomfortable. You cannot understand why, and you can't escape this moment. After what feels like a long time of effort, you finally wake up.")
        return wait_for_choice([
            ("Check others", self.others)
        ])

    def others(self):
        scr("You decide to check a few other theories you have. You want to do a lot of things now. You have a lot of ideas to test. You decide to...")
        return wait_for_choice([
            ("Check interactions", self.inter),
            ("Play with risks", self.risks)
        ])

    def inter(self):
        scr("You want to talk to people and find out what is causing all this, checking for clues, people who can help, anything at all. You decide to ask...")
        return wait_for_choice([
            ("Ask Mr.Juger", self.juger),
            ("Ask the homeless man", self.homeless),
            ("Check out the school", self.school)
        ])

    # ---- SCHOOL BRANCH ----

    def school(self):
        scr("You decide to wander back to the school, as it was the last place you had been in the previous renditions of this day. You enter the building, still as empty as ever, and walk back to the place where you had seen the TV. The TV is now off and gives no new clues, almost as if it never did anything in the first place.")
        return wait_for_choice([
            ("Go deeper", self.deep)
        ])

    def deep(self):
        scr("You search the school more and more, finding nothing on the way. You still look, not knowing what to find, searching through benches, locker rooms and other places. You find a few books with many names on them, but all of them have empty pages.")
        return wait_for_choice([
            ("Turn back", self.back)
        ])

    def back(self):
        scr("You decide to go back as you did not find anything anyway. But when you are about to walk out, you find a boy sitting alone in a classroom. You decide to...")
        return wait_for_choice([
            ("Talk", self.talk),
            ("Walk out", self.out)
        ])

    def talk(self):
        scr("You go to him and ask questions, trying to find some answers but find none, almost as if he is mute and deaf. You keep asking, trying to get any information out of him, but all he does is turn towards you and smile. Not creepy, not sad, just a normal smile and nothing else.")
        return wait_for_choice([
            ("Walk out", self.out)
        ])

    def out(self):
        scr("You walk out of the school and decide to...")
        return wait_for_choice([
            ("Ask Mr.Juger", self.juger)
        ])

    # ---- JUGER / INTERACTION BRANCH ----

    def juger(self):
        scr("You find Mr.Juger on the road again, in the same time and place as you usually do. You want to ask him a question, but what do you ask...")
        return wait_for_choice([
            ("Ask about loop", self.ask_loop),
            ("Ask about time", self.time)
        ])

    def ask_loop(self):
        scr("You ask him about a time loop, asking if it is possible, if it can actually happen, and if it is even practically possible. He replies that he has heard stories about time loops, of people living through the same day to fulfill a particular thing which finally frees them from the loop, but he also says he doesn't believe in anything like that and thinks it is all a fairy tale.")
        return wait_for_choice([
            ("Ask about time", self.time),
            ("Leave", self.out_juger)
        ])

    def time(self):
        scr("You ask him about the concept of time and how time could be looped—can time have a start and an end, or is it infinite? He laughs it off, telling you it is not very common to be talking about time like this, and that time is more of a philosophical topic which he cannot really answer.")
        return wait_for_choice([
            ("Leave", self.out_juger)
        ])

    def out_juger(self):
        scr("You decide to leave Mr.Juger be for now, his answers circling in your mind as you walk away, still trapped in the same day.")
        return wait_for_choice([
            ("Wake up?", self.manager.chapter6.intro)  # or whatever next scene you plan
        ])

    # ---- PLACEHOLDER: RISKS / HOMELESS (you can expand later) ----

    def risks(self):
        scr("You decide to play with risks instead, pushing yourself closer to dangerous situations to see if the world itself will finally change. For now, your choices still seem to lead you back to the very same day.")
        return wait_for_choice([
            ("Check interactions", self.inter),
            ("Go back", self.more_patience)
        ])

    def homeless(self):
        scr("You walk up to the homeless man you have seen before, hoping he might notice something different about this day. His answers are vague and fragmented, almost like he is repeating lines from a story you cannot fully read yet.")
        return wait_for_choice([
            ("Go back", self.others)
        ])
    

    def time(self):
        scr("You ask him about the concept of time and how time can be looped, like can time have a start and an end or is it infinite. He laughs it off, telling you it is not very common to be talking about time like this, and that time is a very philosophical thing which he cannot really answer.")
        return wait_for_choice([
            ("Leave", self.out_juger)
        ])

    def out_juger(self):
        scr("You decide to leave Mr.Juger for now. His words about time and stories of loops keep echoing in your mind as you walk away through the same streets yet again.")
        return wait_for_choice([
            ("Think about everything", self.end_reflect)
        ])

    def end_reflect(self):
        scr("You walk slowly, replaying this whole day inside your head. The pain you forced on yourself, the crying man you heard while you were gone, the empty school, the boy who only smiled, the blank books, and Mr.Juger's half-hearted answers all stack on top of each other. It feels less like a normal day and more like someone’s broken memory that you are stuck inside.")
        return wait_for_choice([
            ("Keep walking", self.end_walk)
        ])

    def end_walk(self):
        scr("As you keep walking, you suddenly feel light-headed again. The world around you starts to blur at the edges, sounds stretching and shrinking as if someone is messing with the volume. You try to focus on the present like Mr.Juger said, but the road tilts under your feet.")
        return wait_for_choice([
            ("Stop fighting it", self.end_faint)
        ])

    def end_faint(self):
        scr("Your legs give up and you fall, the sky spinning above you. For a moment, you hear the man in pain again, his voice overlapping with your own breathing. Then everything cuts to black. You expect the same alarm, the same room, the same clock waiting for you on the other side.")
        return wait_for_choice([
            ("Wake up", self.manager.chapter6.intro)
        ])



class Chapter5_2:
    def __init__(self, manager):
        self.manager = manager

    def intro(self):
        scr("Chapter 5: A questioning decision")
        return wait_for_choice([
            ("Continue", self.start)
        ])

    def start(self):
        scr("You wake up again in the same day, but this time the pain you put yourself through feels pointless. Instead of testing your body, you decide to test the world itself. If this is all some kind of loop, then the people in it should know something, even if they don't say it directly.")
        return wait_for_choice([
            ("Talk to people", self.choose_person)
        ])

    def choose_person(self):
        scr("You decide that today you will talk, listen and watch carefully. No more running into accidents on purpose. No more forcing pain. Just questions, answers and whatever slips through the cracks.")
        return wait_for_choice([
            ("Ask Mr.Juger", self.juger),
            ("Ask the homeless man", self.homeless),
            ("Watch people at the crossing", self.crossing)
        ])

    def juger(self):
        scr("You find Mr.Juger in the same spot as always, walking his usual path. This time you don't just greet him and move on. You stop him and decide to ask something that has been stuck in your mind, something you hope he cannot laugh off so easily.")
        return wait_for_choice([
            ("Ask about yesterday", self.ask_yesterday),
            ("Ask if he remembers you", self.ask_remember)
        ])

    def ask_yesterday(self):
        scr("You ask him what he did yesterday, hoping to catch any detail that doesn't match your own memories. He pauses for a little too long, then gives you a simple, safe answer. 'Same as always,' he says, but doesn't look you in the eye when he says it.")
        return wait_for_choice([
            ("Press him more", self.press_juger),
            ("Change topic", self.ask_remember)
        ])

    def ask_remember(self):
        scr("You ask him if he remembers seeing you yesterday at the exact same time and place. He frowns, thinking hard, then says that all days feel similar at his age. He calls you 'kid' again but uses a name that is not yours. When you correct him, he just laughs it off as a mistake.")
        return wait_for_choice([
            ("Press him more", self.press_juger),
            ("Leave him", self.back_to_choice)
        ])

    def press_juger(self):
        scr("You decide not to let it go. You ask him directly if he has ever felt like this day has happened before. For a moment his face goes blank, as if someone turned off his expression. Then he smiles again and asks you if you have been sleeping well, telling you not to overthink things.")
        return wait_for_choice([
            ("Listen carefully", self.juger_glitch),
            ("Leave him", self.back_to_choice)
        ])

    def juger_glitch(self):
        scr("As he speaks, some of his words feel wrong. You hear him say 'monitoring' and 'stable' in the middle of a normal sentence about the weather, and you are not sure if he actually said them or if your mind added them in. When you blink, the words are gone, replaced by something ordinary.")
        return wait_for_choice([
            ("Walk away", self.back_to_choice)
        ])

    def back_to_choice(self):
        scr("You walk away from Mr.Juger, feeling like you almost heard something important but lost it as soon as you noticed it. You decide to talk to someone else.")
        return wait_for_choice([
            ("Ask the homeless man", self.homeless),
            ("Watch people at the crossing", self.crossing)
        ])

    def homeless(self):
        scr("You walk up to the homeless man sitting near the corner, the same place you have seen him in before. This time you do not just pass by. You sit down a little distance away and start talking, asking him what he sees around here every day.")
        return wait_for_choice([
            ("Ask about accidents", self.homeless_accidents),
            ("Ask about time", self.homeless_time)
        ])

    def homeless_accidents(self):
        scr("You ask him if he has ever seen anyone get hurt on this road. His eyes cloud over for a second, and he says he has seen 'someone' fall, get hit, bleed, more than once. When you ask him when that happened, he only repeats 'today' as if the word itself is stuck in his mouth.")
        return wait_for_choice([
            ("Ask what they looked like", self.homeless_look),
            ("Change topic", self.homeless_time)
        ])

    def homeless_look(self):
        scr("You ask what the person looked like. He squints at you, looks you up and down, then looks away. He never really answers, but you feel his gaze linger on the bandaid marks and the tired look on your face, as if he is comparing you to someone he cannot fully remember.")
        return wait_for_choice([
            ("Leave him", self.after_homeless)
        ])

    def homeless_time(self):
        scr("You ask him what day it is. He answers '24th of July' without thinking, then looks confused when you ask him the same question again. The second time, he takes longer and says 'I only remember this one,' like no other date exists for him.")
        return wait_for_choice([
            ("Ask one last question", self.homeless_last),
            ("Leave him", self.after_homeless)
        ])

    def homeless_last(self):
        scr("You ask him if he ever feels like people disappear and then come back the same as before. He nods slowly and says, 'They go away. Then I hear a beep. Then they are back.' He does not explain what the beep is, and you are not sure you want to know.")
        return wait_for_choice([
            ("Leave him", self.after_homeless)
        ])

    def after_homeless(self):
        scr("You stand up and step away from the homeless man. His words about people going away and coming back, and the strange 'beep' he mentioned, stick to you like a shadow you cannot shake off.")
        return wait_for_choice([
            ("Watch people at the crossing", self.crossing)
        ])

    def crossing(self):
        scr("You decide to stop talking and just watch. You stand near the road, at the same crossing where you have been hit, stabbed or almost killed in other versions of this day. Now, you simply observe what everyone else does while you try your best to stay still.")
        return wait_for_choice([
            ("Watch closely", self.crossing_watch)
        ])

    def crossing_watch(self):
        scr("Cars drive by. People walk, talk, look at their phones. Everything looks normal at first, but small things start to feel off. A woman repeats the exact same sentence twice in the same tone. A man looks both ways, crosses, then somehow appears back at the curb again without you seeing him walk back.")
        return wait_for_choice([
            ("Focus on sounds", self.crossing_sounds),
            ("Focus on faces", self.crossing_faces)
        ])

    def crossing_sounds(self):
        scr("You close your eyes and focus only on the sounds. Steps, engines, distant voices. Underneath all of that, you start to notice a slow, steady pattern. A short tone, a pause, then another tone. Like a machine keeping count of something you cannot see.")
        return wait_for_choice([
            ("Open your eyes", self.end_build)
        ])

    def crossing_faces(self):
        scr("You keep your eyes open and stare at people's faces. Some look tired, some bored, some annoyed. For a split second, you see Mr.Juger among the crowd where he shouldn't be, facing the wrong direction, his mouth moving but no sound coming out. When you blink, he is gone, replaced by a stranger.")
        return wait_for_choice([
            ("Listen instead", self.crossing_sounds)
        ])

    def end_build(self):
        scr("The more you listen, the more the pattern of beeps and silence starts to feel familiar, like something you have heard in another life. Your heart begins to beat in time with it, and breathing suddenly feels like hard work. You realize you have been standing here for far too long.")
        return wait_for_choice([
            ("Try to steady yourself", self.end_fall)
        ])

    def end_fall(self):
        scr("Your legs feel weak. The voices around you stretch and bend, words turning into echoes. Someone bumps into you, but you are not sure if it is real or just your mind letting go. You try to ask one more question, but no sound comes out of your mouth.")
        return wait_for_choice([
            ("Let go", self.end_faint)
        ])

    def end_faint(self):
        scr("Your vision darkens from the edges inward. As you fall, you hear that same pattern again: tone, pause, tone, like a heart monitor trying to drag you back. You do not hit the ground in the way you expect. Instead, everything goes flat, empty, and waiting.")
        return wait_for_choice([
            ("Wake up", self.manager.chapter6.intro)
        ])

class Chapter6:
    def __init__(self,manager):
        self.manager = manager

    def intro(self):
        scr("Chapter 6: A Lot Of Thinking")
        return wait_for_choice([
            ("Start",self.start)
        ])
    
    def start(self):
        scr("You float in a colourless space, weightless and thin, like a thought that forgot it belonged to a body. There is no up, no down, just drifting. Memories circle you: cars, blood, a boy smiling, Mr. Juger laughing something off, a steady beep that never quite stops. You try to reach for any of them, but they slide away like mist.")
        return wait_for_choice([
            ("Think", self.dream_think)
        ])

    def dream_think(self):
        scr("You wonder if this place is inside your head, or outside of it. Were you the one screaming in pain, or just listening from far away? Every loop felt like your choice, your failure, your punishment—but here, floating in nothing, you feel less like a person and more like a story stuck on repeat. The question settles in: if you stopped fighting, would anything change at all?")
        return wait_for_choice([
            ("Wake up", self.wake)
        ])

    # WAKE + ROOM MONOLOGUE ----------------------------

    def wake(self):
        scr("Your eyes open to the dim ceiling of your room. No alarm. No digital numbers drilling into your brain. Just dust motes hanging in a slow column of light. Your body feels heavy, but not broken—an ache deep in the bones instead of sharp pain. You pull your knees close and rest your chin on them, staring at the same wall you have woken to a hundred times before.")
        return wait_for_choice([
            ("Stay and think", self.room_think),
            ("Force yourself up", self.room_check)
        ])

    def room_think(self):
        scr("You sit there in silence, listening to your own thoughts bump into each other. Images stack: the bandages, the accidents, the questions, the wrong names, the endless 24th of July. You whisper to yourself, asking if you deserve this, if this is some kind of trial, or if you are just the leftover noise of a brain that refuses to let go. No answer comes, but the weight of the day settles on your shoulders anyway.")
        return wait_for_choice([
            ("Look around the room", self.room_check)
        ])

    def room_check(self):
        scr("You finally stand, joints protesting with a dull stiffness. The room looks the same, but you search it like it's new. The bedside drawer yawns open to reveal nothing but scratches on the wood. The floor has a faint outline where furniture used to stand. Your bed sheet is wrinkled in the exact shape of your body, as if you never really moved at all. You realise you have to go outside, not to escape, but to finally look at everything without running.")
        return wait_for_choice([
            ("Leave the room", self.hub_start)
        ])

    # HUB: CHOOSE ORDER OF VISITS ----------------------------

    def hub_start(self):
        scr("You step out into the corridor and then onto the street, closing the door behind you with a soft click. The town feels quieter today, as if holding its breath. You decide that you will walk through every place that has shaped your days so far—slowly, deliberately. No rushing into pain. No chasing death. Just walking.")
        return wait_for_choice([
            ("Go to Mr.Juger", self.to_juger),
            ("Go to the accident road", self.to_road),
            ("Go to the homeless man", self.to_homeless),
            ("Go to the chain-snatching street", self.to_chainsnatch),
            ("Go to the school", self.to_school),
            ("Go back home", self.to_home_early)
        ])


    def to_juger(self):
        scr("You walk the familiar route toward where Mr. Juger usually stands. The path feels longer, not in distance but in memory, with every step echoing the questions you asked him before. When you finally see him ahead, your pace slows.")
        return wait_for_choice([
            ("Observe him quietly", self.juger_observe),
            ("Greet him", self.juger_greet),
            ("Walk past him", self.juger_past)
        ])

    def juger_observe(self):
        scr("You stop far enough away that he doesn't notice you and simply watch. Mr. Juger adjusts his glasses, checks his watch, glances down the road. For a heartbeat, his shape wavers: old man, doctor in a white coat, shadow with no face. Each blink snaps him back to normal. You realise that, whether he knows it or not, he is an anchor point in this fake day.")
        return wait_for_choice([
            ("Walk past him", self.juger_past),
            ("Return to the crossroads", self.hub_start)
        ])

    def juger_greet(self):
        scr("You call out to him with a soft 'Good morning.' He looks at you, smiles the same tired smile as always, and says your name—only this time, he gets it right. For a second that feels too long, you wonder if this is progress or just a new variation of the same script. He asks if you are feeling better than 'last time', but when you try to ask what he means, he changes the subject to the weather.")
        return wait_for_choice([
            ("Say nothing more", self.juger_past),
            ("Ask what he meant", self.juger_probe)
        ])

    def juger_probe(self):
        scr("You press him, asking what he meant by 'last time'. His eyes go distant, like he's listening to something far away that you can't hear. Then he shakes his head and tells you not to worry about it, that some days repeat themselves in the mind, and that's just how memory works. His words feel rehearsed, like a line read from a file.")
        return wait_for_choice([
            ("Walk past him", self.juger_past),
            ("Return to the crossroads", self.hub_start)
        ])

    def juger_past(self):
        scr("You walk past Mr. Juger without another word. You feel his gaze on your back for a few seconds, then it fades. Whether he is real, a neighbour, a doctor, or all of them at once, you decide not to demand an answer today. Today is for seeing, not breaking.")
        return wait_for_choice([
            ("Return to the crossroads", self.hub_start)
        ])


    def to_road(self):
        scr("You follow the path that your body knows too well, to the stretch of road where steel and bone have met too many times. Each step feels like walking through old film frames—flashes of headlights, the taste of blood, the sickening lurch of impact—overlaying the quiet morning.")
        return wait_for_choice([
            ("Stand in the road", self.road_stand),
            ("Watch from the side", self.road_side)
        ])

    def road_stand(self):
        scr("You walk to the exact spot where you remember falling. The asphalt under your shoes is rough and warm. No car approaches, no horn blares. You close your eyes and wait, half-expecting the familiar rush of terror. But nothing comes. The world refuses to repeat that moment on command.")
        return wait_for_choice([
            ("Step back to the side", self.road_side),
            ("Return to the crossroads", self.hub_start)
        ])

    def road_side(self):
        scr("You step back to the sidewalk and watch the empty lane. In some loops, this place was violent and sudden. Today, it is just a strip of road, cracked and sun-faded. You realise that without you throwing yourself into danger, it is only scenery. The loop doesn't hunt you; it waits for you to move.")
        return wait_for_choice([
            ("Return to the crossroads", self.hub_start)
        ])


    def to_homeless(self):
        scr("You turn toward the corner where the homeless man usually sits, his back pressed against a post like part of the structure. As you approach, the sounds of the town grow strangely muffled, as if someone turned the volume down on everything but your footsteps.")
        return wait_for_choice([
            ("Sit near him", self.homeless_sit),
            ("Just walk by", self.homeless_pass)
        ])

    def homeless_sit(self):
        scr("You lower yourself to the ground a short distance from him and sit in silence. His eyes are half closed, breathing slow and even. After a while, he opens one eye and looks at you, as if checking that you are still here. No questions pass between you this time. You simply share the quiet.")
        return wait_for_choice([
            ("Ask how he feels", self.homeless_feel),
            ("Leave in silence", self.homeless_leave)
        ])

    def homeless_feel(self):
        scr("You finally ask him how he feels today. He shrugs, says he feels 'the same as always, like today never really finishes.' The words land heavier than they should. Before you can ask more, he closes his eyes again, ending the conversation without cruelty. You understand that he has already said enough on other days.")
        return wait_for_choice([
            ("Stand up and go", self.homeless_leave)
        ])

    def homeless_pass(self):
        scr("You walk by without stopping, only glancing at him from the corner of your eye. He looks smaller than you remember, folded into himself like a crumpled note. You wonder what his loop looks like from the inside, or if he is just an echo in yours.")
        return wait_for_choice([
            ("Return to the crossroads", self.hub_start)
        ])

    def homeless_leave(self):
        scr("You stand and brush the dust from your clothes. As you step away, you hear a faint sound—one short tone, then silence, then another—as if something somewhere has just confirmed that you are still here. You don't look back.")
        return wait_for_choice([
            ("Return to the crossroads", self.hub_start)
        ])


    def to_chainsnatch(self):
        scr("You head into the busier street where crowds used to feel dangerous, where you once felt hands at your neck and the burn of metal ripped away. Today, the flow of people seems slower, like everyone is moving in half-speed, their lives stretched thin.")
        return wait_for_choice([
            ("Walk with the crowd", self.chain_walk),
            ("Watch from the side", self.chain_watch)
        ])

    def chain_walk(self):
        scr("You slip into the stream of bodies, matching their pace. No one bumps into you. No one reaches for you. You're just another shape drifting through, and for once, anonymity feels like mercy. You catch fragments of conversations, but the words blur into static before you can grasp them.")
        return wait_for_choice([
            ("Step aside", self.chain_watch),
            ("Return to the crossroads", self.hub_start)
        ])

    def chain_watch(self):
        scr("From the edge of the pavement, you scan the faces moving past. In one instant, you see a hand dart toward someone's neck—and then the scene skips, like a cut in a film, and the moment is gone. No one cries out. No one reacts. The world edits its own violence when you refuse to play your part.")
        return wait_for_choice([
            ("Return to the crossroads", self.hub_start)
        ])


    def to_school(self):
        scr("You follow the path back to the school, its walls looming like a memory of responsibility and failure. The gate creaks softly as you slip inside. The emptiness meets you like an old friend.")
        return wait_for_choice([
            ("Explore slowly", self.school_hall),
            ("Go straight to the boy", self.school_boy)
        ])

    def school_hall(self):
        scr("You wander the hallways without a goal, letting your feet choose the direction. Classrooms stand open, each one holding the same neat rows of desks and untouched boards. The building feels like a museum of other people's lives, perfectly preserved but long since abandoned.")
        return wait_for_choice([
            ("Go to the boy's classroom", self.school_boy),
            ("Leave the school", self.school_leave)
        ])

    def school_boy(self):
        scr("You reach the classroom where the boy sits alone. He is in the same seat, in the same pose, looking out of the window as if waiting for a cue. When you enter, he turns his head and gives you that familiar, neutral smile. Not happy. Not sad. Just there.")
        return wait_for_choice([
            ("Sit with him", self.boy_sit),
            ("Watch him from the door", self.boy_watch)
        ])

    def boy_sit(self):
        scr("You take a seat at a nearby desk and sit in silence. The room hums with old fluorescent lights, even though you can't see them. Minutes pass as the sunlight crawls along the floor. You don't ask him anything this time. Being here together, wordless, feels more honest than forcing him to break his script.")
        return wait_for_choice([
            ("Leave the classroom", self.school_leave)
        ])

    def boy_watch(self):
        scr("From the doorway, you study his face. Now and then, you think you see his lips move, shaping words you can't hear. Once, very faintly, you catch the outline of 'wake up' on his mouth before it softens back into the same small smile. You blink, and it might have been your imagination.")
        return wait_for_choice([
            ("Leave the classroom", self.school_leave)
        ])

    def school_leave(self):
        scr("You step back into the hallway, the echo of your footsteps trailing behind. The school offers no new answers today, only confirmation that some parts of this world are stuck in place until you walk away from them. You decide you have seen enough for now.")
        return wait_for_choice([
            ("Return to the crossroads", self.hub_start)
        ])

    def to_home_early(self):
        scr("You hesitate at the thought of going home already. Part of you feels you haven't seen enough; another part is just tired. In the end, you turn back toward your house, each step lighter and heavier at the same time.")
        return wait_for_choice([
            ("Go home anyway", self.home_arrive),
            ("Go back to explore", self.hub_start)
        ])

    def home_arrive(self):
        scr("By the time you reach your door, the light has softened into evening. You step inside and feel the familiar stillness wrap around you, not as a trap, but as a thin kind of safety. You go to your room, lie down on the bed, and stare at the ceiling one more time.")
        return wait_for_choice([
            ("Reflect on the day", self.home_reflect)
        ])

    def home_reflect(self):
        scr("You think about everything you saw: Juger half-real, half-someone-else; the harmless road without you throwing yourself into it; the homeless man's resignation; the street that edits its own cruelty; the boy frozen in his lonely classroom. For the first time, you finished the day without bleeding, without sirens, without blacking out mid-scream. You simply walked through it and came back alive.")
        return wait_for_choice([
            ("Let yourself rest", self.home_sleep)
        ])

    def home_sleep(self):
        scr("You pull the blanket over yourself and let your eyes close, not because your body is shutting down, but because you choose to. There is no crash, no knife, no forced reset. Only the soft slide into sleep. Somewhere far away, a quiet beep keeps time. When you wake, you already know what the clock will say—and somehow, that hurts less than it did before.")
        return wait_for_choice([
            ("Wake up", self.manager.chapter7.intro)
        ])
    

class Chapter7:
    def __init__(self, manager):
        self.manager = manager

    # ENTRY: BLACK VOID / NO WAKE ----------------------------

    def intro(self):
        scr("There is no ceiling, no bed, no clock. Only black. You become aware of yourself as a thin outline in the dark, like chalk drawn around a body. There is no floor, but you are standing. No walls, but nowhere to go. The silence feels like the world took a breath in and never let it out.")
        return wait_for_choice([
            ("Listen", self.first_voice)
        ])

    # CRYING / ANGRY MINDVOICE ----------------------------

    def first_voice(self):
        scr("Somewhere in the dark, you hear crying. It starts faint, then grows, then fades again, like waves that never reach a shore. You can’t tell if it’s a child or an adult. It could be you. It could be everyone you have been in every loop so far.")
        return wait_for_choice([
            ("Call out", self.call_out)
        ])

    def call_out(self):
        scr("You ask who is there, your voice feeling delayed, as if it has to swim through heavy water before reaching the air. The crying shifts, mixing with something sharper—anger layered over exhaustion.")
        return wait_for_choice([
            ("Listen closer", self.voice_merge)
        ])

    def voice_merge(self):
        scr("[VOICE - CRYING]: Please... it hurts... make it stop...\n[VOICE - ANGRY]: Why did you keep doing this?\nThe sound circles you without footsteps, moving everywhere and nowhere at once. You realise this voice has been with you in every accident, every loop, every reset.")
        return wait_for_choice([
            ("Stay still", self.stage_juger),
            ("Ask what it is", self.ask_what)
        ])

    def ask_what(self):
        scr("You ask the voice what it is. The reply comes back split, like a mirror cracked down the middle. One half shaking, one half furious.")
        scr("[VOICE]: I am the part that felt everything while you kept trying again. I am the one that never got to leave.")
        return wait_for_choice([
            ("Fall silent", self.stage_juger)
        ])

    # BLACK STAGE: JUGER ----------------------------

    def stage_juger(self):
        scr("The darkness shifts under your feet. A faint outline appears ahead: tall, familiar, wrong. Mr.Juger steps out of the black, but his edges flicker and bleed. Sometimes you see the neighbour. Sometimes a doctor in a white coat. Sometimes nothing but a hollow cut-out where a person should be.")
        return wait_for_choice([
            ("Talk to him", self.juger_talk),
            ("Just watch", self.juger_watch)
        ])

    def juger_watch(self):
        scr("You don’t speak at first. You only watch as his form twitches between shapes. His mouth is shut, but his voice still reaches you, out of sync with his body.")
        scr('"You\'re late again," he whispers, though his jaw never moves. "You should have listened," he adds, staring straight through you.')
        return wait_for_choice([
            ("Answer him", self.juger_talk)
        ])

    def juger_talk(self):
        scr("You ask if this is still the same day, if he is real here, if he is your neighbour or your doctor. His reply comes in broken layers: small talk glued to clinical notes.")
        scr('"It\'s always the twenty fourth... vitals steady... don\'t worry about it, kid... patient remains... just another morning..."')
        return wait_for_choice([
            ("Keep listening", self.juger_fade),
            ("Ask who the patient is", self.juger_patient)
        ])

    def juger_patient(self):
        scr("You ask him who the patient is. For a moment, his outline goes completely blank, like someone erased him. When he comes back, his voice is quieter.")
        scr('"You tell me," he says. Then he smiles, and the smile does not belong to either version of him you know.')
        return wait_for_choice([
            ("Say nothing", self.juger_fade)
        ])

    def juger_fade(self):
        scr("You try to step closer, but the more you move, the more transparent he becomes. His body fades into the dark, his voice stretching into a long, thin echo until there is nothing left of him at all.")
        return wait_for_choice([
            ("Look around", self.stage_road)
        ])

    # ROAD OF ACCIDENTS ----------------------------

    def stage_road(self):
        scr("With a blink, the black beneath you hardens into a strip of road floating in the void. No sky, no buildings—just white paint lines stretching into endless darkness. You know this place. This is where the car hit you. Where the truck did. Where so many endings began.")
        return wait_for_choice([
            ("Step into the middle", self.road_center),
            ("Stay at the edge", self.road_edge)
        ])

    def road_center(self):
        scr("You walk to the middle of the road and wait. No headlights. No engine noise. Instead, figures made of dim light appear along the asphalt—versions of you caught in mid-fall. One reaching out, one already curled on the ground, one thrown sideways in slow motion.")
        return wait_for_choice([
            ("Call to them", self.road_call),
            ("Watch in silence", self.road_watch)
        ])

    def road_edge(self):
        scr("You stay at the edge and watch as pale outlines of yourself replay the same half-second of impact over and over. None of them finish the fall. Each one resets just before hitting the ground, like broken clips on a loop.")
        return wait_for_choice([
            ("Call to them", self.road_call),
            ("Listen to the voice", self.road_voice)
        ])

    def road_call(self):
        scr("You shout for them to move, to get off the road, to stop doing this. None of the versions of you react. They are not people anymore, just recordings of decisions you already made and cannot unmake.")
        return wait_for_choice([
            ("Listen", self.road_voice)
        ])

    def road_watch(self):
        scr("You force yourself to keep watching. Each replay feels heavier, like your chest is filling with lead. You realise every impact you treated like a test was a real injury somewhere you couldn’t see.")
        return wait_for_choice([
            ("Listen", self.road_voice)
        ])

    def road_voice(self):
        scr("[VOICE - ANGRY]: You wanted to know what would happen.\n[VOICE - CRYING]: I felt every one of those.\nThe figures on the road freeze, then fade out, leaving you alone on the floating strip of asphalt in the dark.")
        return wait_for_choice([
            ("Let the road go", self.stage_homeless)
        ])

    # HOMELESS MAN REVEALED ----------------------------

    def stage_homeless(self):
        scr("The road dissolves beneath your feet. When the black settles, a single post rises up out of the void, and beside it sits the homeless man, just as he did at the corner in your loops. This time he is not blended into the background. He is sharp, solid, more real than the darkness around him.")
        return wait_for_choice([
            ("Approach him", self.homeless_approach),
            ("Keep your distance", self.homeless_distance)
        ])

    def homeless_approach(self):
        scr("You walk closer until you are standing right in front of him. His head lifts, and his eyes meet yours fully for the first time. There is no haze there, no confusion—only a tired kind of knowing.")
        return wait_for_choice([
            ("Ask who he is", self.homeless_who),
            ("Ask what he saw", self.homeless_saw)
        ])

    def homeless_distance(self):
        scr("You stay a few steps away, afraid that moving closer will break this strange clarity. Even from here, you feel his attention like a weight, settling on every bruise, every bandaid, every loop burned into you.")
        return wait_for_choice([
            ("Ask who he is", self.homeless_who),
            ("Ask what he heard", self.homeless_heard)
        ])

    def homeless_who(self):
        scr("You ask him who he really is. He huffs out a breath that might be a laugh, might be a sigh.")
        scr('"I\'m just the one who keeps count," he says. "Every time you \'go away\', I\'m the one who notices how long you take to come back."')
        return wait_for_choice([
            ("Ask what he means", self.homeless_heard)
        ])

    def homeless_saw(self):
        scr("You ask what he saw each time you got hurt. His shoulders sag a little more.")
        scr('"Saw you fall. Saw you bleed. Saw the world stitch itself back up around you like nothing happened," he says. "Then I waited for the beep."')
        return wait_for_choice([
            ("Ask about the beep", self.homeless_heard)
        ])

    def homeless_heard(self):
        scr("You ask him about the beep he mentioned before. His gaze drifts past you, into the black.")
        scr('"They go away," he says slowly. "Then I hear a beep. Then they\'re back. You thought you were the only one inside this, but someone else has been listening the whole time."')
        return wait_for_choice([
            ("Fall silent", self.homeless_fade)
        ])

    def homeless_fade(self):
        scr("You want to ask more, but the edges of his shape blur, as if the dark is pulling him back. His eyes stay clear for a heartbeat longer, then blink out like someone turned off a light. You are alone again.")
        return wait_for_choice([
            ("Let the corner go", self.stage_chain)
        ])

    # CHAIN-SNATCH STREET GLITCHED ----------------------------

    def stage_chain(self):
        scr("The empty corner peels away. Now you stand in the outline of the crowded street, but all the people are silhouettes cut out of deeper shadow. Their movements are wrong—too sharp, then too slow, like a broken animation trying to catch up with itself.")
        return wait_for_choice([
            ("Step into the crowd", self.chain_step),
            ("Watch from outside", self.chain_watch)
        ])

    def chain_step(self):
        scr("You move through the silhouettes, but they do not react. Their hands pass through you as if you are smoke. One figure reaches for another's neck, where a dull grey chain hangs. Just before contact, the scene snaps back a few frames and plays again. Over and over. A theft that never finishes, a wound that never opens.")
        return wait_for_choice([
            ("Try to interrupt", self.chain_interrupt),
            ("Let it loop", self.chain_listen)
        ])

    def chain_watch(self):
        scr("From the edge, you watch the same half-second of violence restart again and again. Grabbing hand, turning head, flash of chain—cut. Reset. Replay. Nothing changes, no matter how many times it runs.")
        return wait_for_choice([
            ("Try to interrupt", self.chain_interrupt),
            ("Listen to the voice", self.chain_listen)
        ])

    def chain_interrupt(self):
        scr("You throw yourself between the silhouettes, shouting, pushing, waving your arms. Your hands pass straight through them. The loop does not even flicker. It has never needed you to complete itself; it exists as a pattern, not a memory.")
        return wait_for_choice([
            ("Listen", self.chain_listen)
        ])

    def chain_listen(self):
        scr("[VOICE - ANGRY]: You wanted to see what would happen.\n[VOICE - CRYING]: You never asked what it was doing to me.\nEvery silhouette on the street turns its empty head toward you at once. For a moment, a hundred featureless faces stare straight into you, and you feel the weight of every reckless choice you turned into an experiment.")
        return wait_for_choice([
            ("Look away", self.chain_fade)
        ])

    def chain_fade(self):
        scr("When you can’t bear it anymore, you shut your eyes. When you open them again, the crowd is gone. The street, the buildings, even the ground under your feet have all melted back into pure black.")
        return wait_for_choice([
            ("Let the street go", self.stage_boy)
        ])

    # BOY IN CLASSROOM / STILL SELF ----------------------------

    def stage_boy(self):
        scr("Desks rise out of the dark, neat rows floating on nothing. At the far end sits the boy from the classroom, his chair and table anchored to an invisible floor. This time, he is not smiling.")
        return wait_for_choice([
            ("Go to him", self.boy_approach),
            ("Stay at the door", self.boy_door)
        ])

    def boy_approach(self):
        scr("You walk up to him and see the change clearly. His face is no longer blank or gently kind. His eyes are heavy, rimmed with a tiredness that feels older than you. He taps his fingers on the desk, and each tap echoes like a distant medical beep.")
        return wait_for_choice([
            ("Ask who he is", self.boy_who),
            ("Sit beside him", self.boy_sit)
        ])

    def boy_door(self):
        scr("You stand where a doorway should be, watching him from a distance. Every so often, his lips move in tiny shapes without sound. Once, you are sure you see the words 'wake up' form on his mouth before they smooth back into a straight line.")
        return wait_for_choice([
            ("Step closer", self.boy_approach)
        ])

    def boy_who(self):
        scr("You ask him who he really is. The answer comes from everywhere at once, not from his mouth, but from the space around you.")
        scr('"I\'m the part of you that stayed still," the voice says. "The part that watched you run into every wall and couldn\'t make you stop."')
        return wait_for_choice([
            ("Apologise", self.boy_apologise)
        ])

    def boy_sit(self):
        scr("You sit down at the next desk. Neither of you speaks for a while. The dark around the classroom hums softly, like lights you can\'t see. You think about every time you hesitated, every time you froze instead of acting. They all feel like they live in him.")
        return wait_for_choice([
            ("Ask who he is", self.boy_who)
        ])

    def boy_apologise(self):
        scr("You tell him you’re sorry—for not listening, for pushing, for ignoring the warnings you gave yourself. The boy tilts his head, considering your words with an unreadable expression.")
        scr('"You\'re not finished yet," he says quietly. "That\'s the problem."')
        return wait_for_choice([
            ("Let him go", self.boy_fade)
        ])

    def boy_fade(self):
        scr("You blink, and the desks are empty. The boy is gone. Only the echo of his last word hangs in the dark like a note that refuses to die: yet.")
        return wait_for_choice([
            ("Stand alone", self.mindvoice_final)
        ])

    # FINAL MINDVOICE / NO WAKE YET ----------------------------

    def mindvoice_final(self):
        scr("The black closes in, tighter than before, until even the suggestion of floor and furniture disappears. You are nowhere and everywhere, and you are not alone. The crying and the anger finally settle into one presence standing right behind you.")
        return wait_for_choice([
            ("Don’t turn around", self.mindvoice_talk)
        ])

    def mindvoice_talk(self):
        scr("[VOICE]: Why won\'t you wake up?\n[VOICE]: Why do you keep dragging us back here?\nYou speak to it like another person, but you know now that it isn\'t. It is you. Or rather, the part of you that never leaves the bed, never escapes the machines, never gets to pretend the pain is a puzzle to solve.")
        return wait_for_choice([
            ("Ask what it wants", self.mindvoice_want)
        ])

    def mindvoice_want(self):
        scr("You ask what it wants from you. The answer arrives in jagged pieces, every shard a different version of your reflection.")
        scr('"I want you to listen," it says. "I want you to stop using my pain as your playground. I want you to understand that this story you keep living is built on a body that is still lying there, trying to breathe."')
        return wait_for_choice([
            ("Fall silent", self.mindvoice_end)
        ])

    def mindvoice_end(self):
        scr("The dark around you tightens like closing curtains. Shapes flicker at the edges—Mr.Juger, the homeless man, the crowd of silhouettes, the boy at his desk—all of them overlaid with something colder: gloves, monitors, white coats, metal rails. None of them step closer. They only watch as the stage closes on you.")
        scr("[VOICE]: Next time... listen.\nThere is no rush of waking, no jolt, no alarm. You don\'t open your eyes. You just hang there, between the loop and the body it belongs to, knowing that when you finally surface, the date will still be the twenty fourth of July—and that you are not the only one trapped inside it.")
        return wait_for_choice([
            ("...", self.manager.chapter8.intro)
        ])
    

class Chapter8:
    def __init__(self, manager):
        self.manager = manager

    # ENTRY: MORNING WITH NEW CLARITY ----------------------------

    def intro(self):
        scr("Chapter 8: Walking with Clarity")
        return wait_for_choice([
            ("Continue", self.wake)
        ])

    def wake(self):
        scr("You wake up to the same ceiling, the same faded paint and hairline cracks, but this time your mind feels different. The black stage of yesterday still hangs in your thoughts—Mr.Juger flickering between neighbour and doctor, the homeless man counting beeps, the boy in the classroom calling himself the part of you that stayed still, and the mindvoice admitting it is the one that feels everything. The clock still reads 7:00 AM, 24th of July, but the numbers feel less like a prison and more like a label on a test tube: this is the day you are in, and this is the day you are going to study.")
        return wait_for_choice([
            ("Sit and think", self.morning_think),
            ("Get up immediately", self.morning_rise)
        ])

    def morning_think(self):
        scr("You sit on the edge of your bed, feet not quite touching the floor, and let your thoughts settle instead of trying to outrun them. You go over what you know now, quietly, almost like reciting a set of instructions to yourself. The loop always snaps back to this morning. Pain here echoes somewhere else. The people might not just be neighbours or strangers, but masks over something you still cannot fully see. You are not the only one trapped in this.")
        return wait_for_choice([
            ("Stand up", self.morning_rise)
        ])

    def morning_rise(self):
        scr("You stand, feeling the stiffness in your body like rust in your joints. There is no rush this time. You move slowly, deliberately, as if every action is being recorded and will be watched again later. The alarm has already been silenced. The digital clock still shows 7:00 AM, 24th July, but you choose not to stare at it with fear. Instead, you take one slow breath and decide that today is not about breaking the loop. Today is about understanding it.")
        return wait_for_choice([
            ("Check your body", self.check_body),
            ("Look around the room", self.check_room)
        ])

    # ROOM / BODY AWARENESS ----------------------------

    def check_body(self):
        scr("You roll up your sleeves and look at your arms more carefully than you have in a long time. Faint scars trace over older wounds, small pale lines crossing each other like a map of every test you put yourself through. Some bandaids are fresh, some are ghosts of bandaids that once were. Underneath, you feel that dull ache again—the kind that belongs to a body that has been hurt too often to fully recover between blows. You know now these marks mean something in a world far away from this room.")
        return wait_for_choice([
            ("Look around the room", self.check_room)
        ])

    def check_room(self):
        scr("You look at your room like it’s a crime scene or a stage set. The bedside table holds nothing new, but the scratches on its surface remind you of how many times you’ve opened that drawer looking for something that was never there. The walls are the same, but now you notice the way the shadows fall, as if light is coming from a place you cannot point to. Even the air feels curated, thick enough to slow you down but thin enough to carry sound from somewhere beyond this loop.")
        return wait_for_choice([
            ("Review what you know", self.review_knowledge)
        ])

    def review_knowledge(self):
        scr("You whisper a list to yourself, like you are trying to pin your thoughts in place: The day repeats, but the details sometimes don’t. Pain here seems to belong to someone else as well. Mr.Juger is more than he appears. The homeless man hears beeps that don’t belong to this street. The boy in the classroom is a part of you, and the mindvoice is the one truly suffering. The city is not neutral—it reacts. Saying it all out loud doesn’t fix anything, but it steadies you.")
        return wait_for_choice([
            ("Leave the house", self.leave_house)
        ])

    # LEAVING HOME / START OF DAY ----------------------------

    def leave_house(self):
        scr("You open the door and step outside into the familiar morning. The light feels softer than usual, but you can’t tell if that’s new or if you simply never paid attention. The road ahead waits in its usual stillness, but you sense something layered under it now—like a quiet humming beneath a song. You decide that today you will walk through the loop from start to finish, not to trigger every event again, but to see what the world does when you simply watch.")
        return wait_for_choice([
            ("Head toward school first", self.to_school_early),
            ("Take the usual street route", self.to_streets_early)
        ])

    # PATH 1: SCHOOL EARLY ----------------------------

    def to_school_early(self):
        scr("You choose to go to the school earlier than usual, just to see if the world allows it. The path feels familiar, but you take it slower, counting steps, paying attention to how the buildings sit against the sky. Nothing jumps out at you, but your mind is sharper now, catching small things like a shop sign you swear you’ve never seen, or a crack in the pavement that looks like a branching river. The school gates loom ahead, just as they always do.")
        return wait_for_choice([
            ("Enter the school", self.school_entry),
            ("Circle around it first", self.school_circle)
        ])

    def school_entry(self):
        scr("You push the gate open with a soft creak and step inside. The hallways are empty, their polished floors reflecting a dim light from windows that don’t show much of the outside. You walk past the classrooms, each door slightly ajar, each room frozen in a perfect arrangement of desks and chairs. The air smells faintly of chalk and something else—something metallic and sterile, like a hospital corridor superimposed on the memory of a school.")
        return wait_for_choice([
            ("Go to the boy's classroom", self.school_boy),
            ("Explore other rooms first", self.school_explore)
        ])

    def school_circle(self):
        scr("Instead of going straight in, you walk a slow circle around the outside walls. The building feels heavier from here, like a solid block of all your repeated days compressed into one structure. You pause once, noticing how one of the windows seems to flicker, as if it’s showing two different rooms at once. When you blink, it becomes normal again. You know then that avoiding the school will not dissolve it—you have to go inside.")
        return wait_for_choice([
            ("Enter the school", self.school_entry)
        ])

    def school_explore(self):
        scr("You wander into classrooms you rarely visited. Each one is eerily neat, as if waiting for students who never arrive. You trail your fingers along the edges of desks, half expecting them to glitch or disappear. On one chalkboard, faint writing appears only when you stare: words like 'observation', 'response', '24 hours'. When you blink, the board is blank. You realise the world shows you more now because you’re finally looking for it.")
        return wait_for_choice([
            ("Now go to the boy", self.school_boy)
        ])

    def school_boy(self):
        scr("You arrive at the familiar classroom. The boy is there, sitting in the same seat, looking out of the same window. When you step in, he turns and gives you the same small, neutral smile, but now you can’t help seeing the weight behind it—the tired eyes you saw in the black world. You sit down nearby and speak to him, gently, asking about the day, about the time, about whether he ever feels like he has been here too long. Some of his answers sound normal. Others carry a faint echo, as if another voice is layered underneath his.")
        return wait_for_choice([
            ("Stay a while longer", self.school_stay),
            ("Leave the school", self.school_leave)
        ])

    def school_stay(self):
        scr("You stay longer than you ever have before, just sharing the quiet. There are no jump scares, no sudden changes, just the slow drag of time that may not be real but feels real enough. You remember what his other self told you: 'I’m the part of you that stayed still.' You decide not to force more answers out of him today. Being here, acknowledging him, feels like progress in itself.")
        return wait_for_choice([
            ("Leave the school", self.school_leave)
        ])

    def school_leave(self):
        scr("You stand and say you’ll see him again, even if you don’t know what that really means. The boy nods once, returning his gaze to the window as you step out. In the hallway, your footsteps echo in a way that reminds you of the monitor beeps—regular, spaced, too precise to be an accident. You walk back toward the gate, feeling like you’ve honoured this part of your mind instead of using it.")
        return wait_for_choice([
            ("Head into the city", self.city_hub)
        ])

    # PATH 2: STREETS FIRST ----------------------------

    def to_streets_early(self):
        scr("You choose to take the usual streets first, retracing the familiar routes with a new kind of patience. The road where the accident once took place lies ahead, quiet and almost innocent in the morning light. You pass the spot without stepping into danger, noting how normal it looks when you don’t force it to do anything dramatic.")
        return wait_for_choice([
            ("Visit Mr.Juger", self.street_juger),
            ("Visit the homeless man", self.street_homeless),
            ("Skip straight to exploring deeper", self.city_hub)
        ])

    def street_juger(self):
        scr("You approach the place where Mr.Juger usually appears. As expected, he’s there, walking along his usual path. When he sees you, he offers the same gentle greeting, but you catch small differences now—the tilt of his head, the exact words he uses, the way his concern slips into something almost clinical for a second before smoothing out again. You speak with him, but this time, you are not looking for big answers, just small changes, hints that even he cannot keep the script perfectly the same.")
        return wait_for_choice([
            ("Let him go", self.after_juger),
            ("Ask about the day again", self.street_juger_day)
        ])

    def street_juger_day(self):
        scr("You ask him how his day has been so far. His response is simple, but there is a tiny stumble when he mentions the date. He corrects himself quickly, but you heard it—the moment where his tongue almost slipped into something else. It’s enough to remind you that what you see of him is only the surface.")
        return wait_for_choice([
            ("End the talk", self.after_juger)
        ])

    def after_juger(self):
        scr("You say goodbye and walk away at your own pace, not because the scene pushed you out, but because you decide that is enough. You have confirmed what you needed: even the most stable parts of this loop have seams showing if you look closely.")
        return wait_for_choice([
            ("Visit the homeless man", self.street_homeless),
            ("Head toward the school", self.to_school_early),
            ("Go deeper into the city", self.city_hub)
        ])

    def street_homeless(self):
        scr("You head to the corner where the homeless man sits. Today, he seems quieter, but more focused. When you greet him, he looks up with eyes that seem less clouded than before, like he’s slowly waking up along with you. You ask how he is, and he gives a small shrug, saying he feels 'the same, but not the same'—words that sound exactly like your own thoughts.")
        return wait_for_choice([
            ("Ask another question", self.street_homeless_more),
            ("Move on", self.after_homeless)
        ])

    def street_homeless_more(self):
        scr("You ask if he ever notices things changing, little details that don’t match from one 'today' to the next. He scratches his cheek, thinking, then says that sometimes he thinks a building used to be taller, or a sign used to say something else, but he’s never sure if that’s memory or imagination. Hearing it from him makes your own suspicions feel less like paranoia and more like observation.")
        return wait_for_choice([
            ("Thank him", self.after_homeless)
        ])

    def after_homeless(self):
        scr("You thank him for talking and step away, feeling less alone in your noticing. The corner behind you feels like it fades slightly as you walk, as if it only fully exists when you are looking at it. The idea that the city responds to your awareness settles deeper in your mind.")
        return wait_for_choice([
            ("Head toward the school", self.to_school_early),
            ("Go deeper into the city", self.city_hub)
        ])

    # CITY EXPLORATION HUB ----------------------------

    def city_hub(self):
        scr("With the school visited and the usual landmarks revisited, you decide to go further than you usually do. The city stretches ahead, not as a maze of streets, but as a patchwork of memories and half-understood details. Today, you are not looking for danger. You are looking for clues—text that flickers, words that don’t belong, places that only sharpen when you pay attention to them.")
        return wait_for_choice([
            ("Explore side streets", self.city_side),
            ("Watch people closely", self.city_people),
            ("Study signs and posters", self.city_signs)
        ])

    def city_side(self):
        scr("You turn into narrower side streets you rarely walked before. The buildings here feel less defined, like sketches that were never fully inked. Windows are dark, doors are plain, but if you stare too long, you catch the edges of something else—frames that look like curtain rails, shadows shaped like hanging cables. It’s as if the city didn’t bother to finish these parts unless you insisted on seeing them.")
        return wait_for_choice([
            ("Go back to main roads", self.city_hub),
            ("Venture further in", self.city_edge)
        ])

    def city_edge(self):
        scr("The further you walk, the less real things feel. At the far edge of the street, the world seems to fade into a soft blur, like an unfinished drawing. When you reach out, your hand meets nothing, like the set ends here and there is no backstage. You realise the loop doesn’t need an entire world—it only renders what you insist on touching.")
        return wait_for_choice([
            ("Return to busier areas", self.city_hub)
        ])

    def city_people(self):
        scr("You stand in a busier area and simply watch people move. They walk, talk, gesture, but now you are looking for patterns. You notice that some people have full, detailed movements, while others feel like background loops, repeating the same small sequence every time you look back at them. Occasionally, a phrase from a passing conversation snaps into focus: '…monitoring…', '…stable for now…', '…24 hours under observation…' Then the voices dissolve back into ordinary chatter.")
        return wait_for_choice([
            ("Keep watching", self.city_people_more),
            ("Change focus", self.city_hub)
        ])

    def city_people_more(self):
        scr("The longer you watch, the clearer it becomes: not everyone here has the same weight. Some are like solid characters. Others are like ghosts filling space. You realise that the world around you might be a mix of real memories and filler, built to make this loop feel full while only truly caring about a few fixed points. It’s less a city and more a carefully arranged stage.")
        return wait_for_choice([
            ("Change focus", self.city_hub)
        ])

    def city_signs(self):
        scr("You decide to read everything you can: shop names, posters, street signs, stray notes stuck to walls. At first, everything looks normal. But when you double back and read something again, you notice small differences—a word that changed order, a phrase that now includes a number that wasn’t there before, or a date that flickers between formats like it can’t quite decide what world it belongs to.")
        return wait_for_choice([
            ("Stare at one sign", self.city_sign_focus),
            ("Move on", self.city_hub)
        ])

    def city_sign_focus(self):
        scr("You pick one sign and stare at it until your eyes blur. The longer you look, the more unstable it becomes. Letters seem to wobble, some lines swapping out for others: 'OPEN 24/7' becomes 'UNDER 24H CARE' for a heartbeat before snapping back. It’s subtle, easy to miss, but you are not the same distracted person you were at the start of all this. You see it. You know now that the text of this world is not fixed.")
        return wait_for_choice([
            ("Step back", self.city_hub)
        ])

    # END OF DAY / CALMER RESOLVE ----------------------------

    def end_day(self):
        scr("By the time the light begins to soften and the shadows grow longer, you feel tired, but not from running or bleeding. This is the weariness that comes from thinking hard, from noticing too much. You have seen enough today to confirm what Chapter 7 hinted at: this world is not a clean, external loop. It bends around you, rewrites itself in small ways, and reveals more when you demand to see more.")
        return wait_for_choice([
            ("Go home", self.go_home)
        ])

    def go_home(self):
        scr("You walk back home, retracing your steps with a strange mix of familiarity and new understanding. The door feels lighter when you open it, like it’s just a prop instead of a barrier. You sit in your room under the same roof, at the same time, and go over the day in your head—the school, the boy, Juger’s slips, the homeless man’s agreement, the city’s shifting details. You realise you are not just surviving the loop anymore. You are starting to read it.")
        return wait_for_choice([
            ("Let yourself rest", self.sleep)
        ])

    def sleep(self):
        scr("You lie down, not from injury or collapse, but because you choose to end this version of the 24th of July on your own terms. Sleep comes slowly, but without violence—no car crash, no knife, no forced blackout. Somewhere beyond this room, a quiet beep continues its patient counting. You already know what the clock will say when you open your eyes again. For once, that thought does not crush you. It simply means you will have another chance to look closer.")
        return wait_for_choice([
            ("Wake up", self.manager.chapter9.intro)
        ])

class Chapter9:
    def __init__(self, manager):
        self.manager = manager

    # ENTRY: SAME MORNING, NEW SUSPICION ----------------------------

    def intro(self):
        scr("Chapter 9: The City That Never Repeats")
        return wait_for_choice([
            ("Continue", self.wake)
        ])

    def wake(self):
        scr("You wake up again to the same ceiling, the same cracks, the same faint stain in the corner. The clock still insists it is 7:00 AM, 24th of July, like it has for what feels like forever. But after yesterday, something feels off—not in the time itself, but in the way the day sits on you. It is like putting on a shirt you have worn a hundred times and suddenly realising the fabric isn’t quite the same.")
        return wait_for_choice([
            ("Check the details", self.morning_check),
            ("Ignore it and stand up", self.morning_rise)
        ])

    def morning_check(self):
        scr("You stay in bed a little longer and let your eyes rove over the room. The alarm sounds just like it always has—or does it? You listen closer, wondering if the pitch is slightly different, if one of the beeps at the end is new. The note near your bandages looks familiar, but when you skim it, a word feels out of place, like it has swapped positions with another one in the night. None of this is proof. But all of it feels wrong in tiny, precise ways.")
        return wait_for_choice([
            ("Stand up", self.morning_rise)
        ])

    def morning_rise(self):
        scr("You swing your legs over the side of the bed and stand. The routine tries to pull you into its usual rhythm—wash, dress, stare at the clock—but your mind is sharper now. You go through the motions, but you keep one thought at the centre of everything: if this really is the exact same day repeating, then nothing, not even the smallest detail, should change. Today, you are going to test that.")
        return wait_for_choice([
            ("Leave the room", self.leave_room)
        ])

    def leave_room(self):
        scr("You open the door and step into the corridor, then out into the same small world you have walked so many times. The air tastes familiar, the light falls in familiar angles, but there is a tension sitting just beneath it all, like the set is holding itself together a little too tightly. You decide to start with something simple—a person you have seen more than anyone else in this loop.")
        return wait_for_choice([
            ("Go to Mr.Juger", self.to_juger),
            ("Check the road first", self.to_road)
        ])

    # MR. JUGER: FIRST CLEAR CHANGE ----------------------------

    def to_juger(self):
        scr("You walk the route toward where Mr.Juger usually stands. Your feet know the path better than your conscious mind does, carrying you past the same houses, the same cracks in the sidewalk, the same uneven fence. When you finally see him, in his usual place, you slow down and pay attention to every detail.")
        return wait_for_choice([
            ("Greet him", self.juger_greet),
            ("Observe quietly", self.juger_watch)
        ])

    def juger_watch(self):
        scr("You hang back and watch him before saying anything. He checks his watch, shifts his weight from one foot to the other, glances down the road. It is all so ordinary—but then you notice his lips moving, practising a sentence before he speaks it. The words don’t reach you, but the pattern of them does, like he is rehearsing his role in this day.")
        return wait_for_choice([
            ("Now greet him", self.juger_greet)
        ])

    def juger_greet(self):
        scr("You step forward and say, 'Good morning.' He looks up and smiles with the same tired warmth as always, but when he answers, you hear it—the difference. Maybe he uses a nickname he has never used. Maybe he adds a word like he has known you longer than he ever has before. The sentence is almost right, a near-perfect copy of what he has said on other days, but not exact. The loop has slipped.")
        return wait_for_choice([
            ("Ask him about the day", self.juger_day),
            ("End the talk and move on", self.after_juger)
        ])

    def juger_day(self):
        scr("You ask him how his day has been. He starts to answer on autopilot, then stumbles for a fraction of a second. 'Same as always,' he says, but you catch a glitch buried in the pause, a flicker in his eyes like he is comparing two different versions of the same memory. He recovers quickly, changing the subject like nothing happened. Once, you wouldn’t have noticed. Now, you do.")
        return wait_for_choice([
            ("End the talk and move on", self.after_juger)
        ])

    def after_juger(self):
        scr("You say goodbye and walk away, heart beating a little faster—not from fear, but from confirmation. If this were a flawless reset of the same day, his words would be identical every time. They aren’t. The script is drifting, and that means something is writing, or rewriting, this place as you go.")
        return wait_for_choice([
            ("Go to the accident road", self.to_road),
            ("Visit the homeless man", self.to_homeless)
        ])

    # ACCIDENT ROAD: EVENTS SHIFT ----------------------------

    def to_road(self):
        scr("You follow the route to the stretch of road that has been the stage for so many of your deaths. You know exactly where you have stood before, where the car hit you, where the truck didn’t give you time to think. Today, you stop at the edge first, watching the flow of traffic—or the lack of it.")
        return wait_for_choice([
            ("Step into the road", self.road_step),
            ("Stay on the sidewalk", self.road_watch)
        ])

    def road_watch(self):
        scr("You stand on the sidewalk and just observe. On some days, a car would have already rushed by, horn blaring, forcing you into a split-second choice. Today, the lane is oddly calm. A car rolls by, slower than you remember. A cyclist passes later than you expect. The beats of the scene are out of time with your memory.")
        return wait_for_choice([
            ("Test it by stepping in", self.road_step),
            ("Move on without testing", self.after_road)
        ])

    def road_step(self):
        scr("You step into the middle of the lane at the same spot where you once felt metal crush bone. You wait, counting breaths, expecting the world to snap into its old rhythm—engine roar, shock, impact. Instead, a car slows down well before it reaches you, stopping with an almost unnatural smoothness. The driver doesn’t lean on the horn. They simply stare, as if waiting for you to move first.")
        return wait_for_choice([
            ("Step back to safety", self.road_safe),
            ("Stay and test the driver", self.road_test_driver)
        ])

    def road_safe(self):
        scr("You step back to the edge, and the car eases forward again, the danger never fully forming. The scene feels like a rehearsal that didn’t commit to the final performance. You realise then that even this big, violent moment depends on how you choose to move. The loop isn’t forcing you into the same accident—your own actions are.")
        return wait_for_choice([
            ("Move on", self.after_road)
        ])

    def road_test_driver(self):
        scr("You stay in place longer than any sane person would. The driver’s face blurs at the edges, never quite sharpening into a real person. They lower the window, but no sound comes out. It is like the world never wrote this part of the script clearly, because it expected you to be unconscious by now. You step back eventually, and the car glides away, leaving you with the unsettling sense that this street only knows how to kill you, not how to talk to you.")
        return wait_for_choice([
            ("Move on", self.after_road)
        ])

    def after_road(self):
        scr("You leave the road with a new line on your list: some events happen only when you push for them. Without you walking into the danger, the day doesn’t arrange itself to hurt you automatically. The loop is not an all-powerful force—it’s a structure that reacts to you.")
        return wait_for_choice([
            ("Visit the homeless man", self.to_homeless),
            ("Head toward the school", self.to_school)
        ])

    # HOMELESS MAN: CONFIRMING DRIFT ----------------------------

    def to_homeless(self):
        scr("You walk toward the corner where the homeless man usually sits. The path feels familiar, but your attention is different. You are listening for the rhythm of his words before he even speaks them, ready to catch any slip, any variation, any proof that the day is not a perfect loop.")
        return wait_for_choice([
            ("Talk to him", self.homeless_talk),
            ("Observe silently", self.homeless_watch)
        ])

    def homeless_watch(self):
        scr("You stop a short distance away and watch him from the side. His posture looks almost identical to other days, but then you notice a small detail—a different way he holds his hands, a twitch in his leg that you’ve never seen. These could be nothing. They could be everything. Either way, you don’t dismiss them anymore.")
        return wait_for_choice([
            ("Talk to him", self.homeless_talk)
        ])

    def homeless_talk(self):
        scr("You sit near him and say hello. He opens his eyes and looks at you with a recognition that feels slightly stronger than before, like each loop has added one more layer of memory to his gaze. You ask what day it is, expecting the usual answer. He says, 'Twenty fourth of July,' but this time there is a pause before he adds, 'Again.' That word has never been there before.")
        return wait_for_choice([
            ("Ask about 'again'", self.homeless_again),
            ("Leave it and move on", self.after_homeless)
        ])

    def homeless_again(self):
        scr("You ask him what he means by 'again'. He frowns, rubbing his forehead as if it hurts to think about it. He says some days feel like they blur into each other, that sometimes he thinks he has already had this conversation with you, but he can’t tell if that’s real or just his mind replaying itself. Hearing your own experience come out of his mouth, even half-formed, makes your skin prickle.")
        return wait_for_choice([
            ("Thank him", self.after_homeless)
        ])

    def after_homeless(self):
        scr("You thank him and stand up. As you step away, you realise something important: if he was just a flat piece of scenery, his answers would never drift. The fact that his words change, even slightly, means he is more than a static prop. The city isn’t just looping—it is remembering, forgetting, and improvising.")
        return wait_for_choice([
            ("Go to the school", self.to_school),
            ("Explore deeper into the city", self.city_hub)
        ])

    # SCHOOL AGAIN: CONFIRMING THE MINDSPACE FEEL ----------------------------

    def to_school(self):
        scr("You head toward the school, feeling the shape of the day rearrange itself around you. The building rises ahead, the same as always, yet you can’t shake the sense that it is less a physical place and more an organised cluster of memories. Classrooms filled with stillness, hallways echoing with steps that don’t always belong to you.")
        return wait_for_choice([
            ("Enter the school", self.school_entry),
            ("Avoid it and keep walking", self.city_hub)
        ])

    def school_entry(self):
        scr("You step through the gate and into the quiet halls. The pattern is familiar—rows of desks, clean boards, empty chairs—but you are not here to repeat actions. You are here to see what the school reveals now that you know it is built from pieces of you. In one room, a poster on the wall has different text than you remember. In another, a clock ticks even though the hands never move.")
        return wait_for_choice([
            ("Visit the boy again", self.school_boy),
            ("Explore other rooms", self.school_rooms)
        ])

    def school_rooms(self):
        scr("You wander into new rooms and revisit old ones, noting how some feel fully realised while others are vague, like afterthoughts. In one class, you spot a notebook with your handwriting inside, but when you flip through it, all the pages are blank. In another, the windows show a cityscape that doesn’t match the streets outside. The school feels less like a real building and more like a filing cabinet for different versions of you.")
        return wait_for_choice([
            ("Now see the boy", self.school_boy)
        ])

    def school_boy(self):
        scr("You return to the boy’s classroom. He sits in his usual place, but when you enter, it feels like he has been waiting. His smile is smaller today, almost cautious. You sit nearby and talk to him again. His answers are simple, but a few of them are new—new phrasing, new pauses, new small mistakes. If he were a perfect recording, he would never change. Instead, he adapts, like he is learning along with you.")
        return wait_for_choice([
            ("Leave the school", self.after_school)
        ])

    def after_school(self):
        scr("You step back out into the hall and then out of the building, the idea solidifying in your mind: this isn’t a static snapshot of your life. It is a constructed space that responds to where you look and what you ask. The more you return, the more it shifts, not randomly, but in tune with your attention.")
        return wait_for_choice([
            ("Explore deeper into the city", self.city_hub)
        ])

    # CITY HUB: SEEING THE PATTERN ----------------------------

    def city_hub(self):
        scr("You move away from the usual paths and into streets you never bothered to explore properly. With every step, your suspicion grows stronger. Shops you never focused on before look half-finished, as if the world never expected you to come this far. People you haven’t seen in earlier loops appear now, but their faces are oddly generic, like placeholders filling gaps.")
        return wait_for_choice([
            ("Watch people closely", self.city_people),
            ("Study signs and text", self.city_text),
            ("Push toward the edge of the map", self.city_edge)
        ])

    def city_people(self):
        scr("You stop on a busy corner and let the world flow around you. Some people move with full, natural complexity—adjusting bags, checking their phones, reacting to bumps and obstacles. Others feel like they are running on a short loop, repeating the same few gestures whenever they re-enter your field of view. A woman repeats the same sentence twice in exactly the same tone. A man walks past, then somehow appears again from the same direction without having time to turn around.")
        return wait_for_choice([
            ("Keep watching", self.city_people_more),
            ("Change focus", self.city_hub)
        ])

    def city_people_more(self):
        scr("You realise that not everyone here is carrying the same weight in this world. Some feel like fully rendered people. Others feel like background processes, doing just enough to make the city seem alive. The more carefully you look, the more the illusion of a full, objective reality thins. This is not a complete world. It is a carefully arranged crowd scene in someone’s mind.")
        return wait_for_choice([
            ("Change focus", self.city_hub)
        ])

    def city_text(self):
        scr("You start reading everything you can: shop signs, bus route boards, flyers stuck onto walls. On the first pass, they read like ordinary text. But when you double back and read them a second time, you catch tiny changes: a number added where none was before, a word that looks suspiciously like 'monitoring' where you swear it used to say 'morning', a poster date that flickers between formats, unsure of which calendar it belongs to.")
        return wait_for_choice([
            ("Focus on one sign", self.city_text_focus),
            ("Move on", self.city_hub)
        ])

    def city_text_focus(self):
        scr("You pick one sign and stare. At first it says something simple, forgettable. The longer you look, the more unstable it feels. Letters shimmer and rearrange themselves. 'OPEN 24/7' shifts into 'UNDER 24H CARE' for a heartbeat before snapping back. It would be easy to dismiss as eye strain—if you hadn’t seen similar things on black monitors and white ceilings in another world.")
        return wait_for_choice([
            ("Step back", self.city_hub)
        ])

    def city_edge(self):
        scr("You keep walking until the city itself seems to lose confidence. Buildings at the far edge feel like unfinished sketches, with fewer details the closer you get. When you reach out toward a distant structure, your hand meets nothing, like you’ve found the end of the rendered space. There is no beyond—only blur. The world only fully exists where you insist on putting your mind.")
        return wait_for_choice([
            ("Return toward home", self.end_day)
        ])

    # END OF CHAPTER: REALISATION ABOUT THE LOOP ----------------------------

    def end_day(self):
        scr("By the time you start walking back home, the sky looks the same as every other evening you’ve survived—but you are not the same. You have seen enough small differences to know this is not a flawless rewind of a universal day. The city does not reset into a perfect copy. It changes with you. Mr.Juger’s words shift. The timing of events drifts. The homeless man’s answers evolve. The signs rewrite themselves under your gaze. This loop isn’t the world’s prison; it’s a personal construction.")
        return wait_for_choice([
            ("Go home", self.go_home)
        ])

    def go_home(self):
        scr("You reach your door and step inside, carrying one crucial realisation like a weight in your chest: you are not exploring a fixed, external reality. You are moving through a psychological space—a mind trying to make sense of pain, monitors, and days that never end. Each loop is not a copy, but a new draft of the same story, adjusted by what you noticed before.")
        return wait_for_choice([
            ("Rest for now", self.sleep)
        ])

    def sleep(self):
        scr("You lie down on your bed, not because you are being forced into unconsciousness by an accident, but because the day has given you what it could. The clock will still say 7:00 AM, 24th of July, the next time you open your eyes. But now you understand that the power of this loop does not lie in its sameness—it lies in its ability to change with your imagination and fear. The story is not universal fate. It is intimately, painfully yours.")
        return wait_for_choice([
            ("Wake up", self.manager.chapter10.intro)
        ])

class Chapter10:
    def __init__(self, manager):
        self.manager = manager

    def intro(self):
        scr("Chapter 10: Deliberate Breaks")
        return wait_for_choice([
            ("Continue", self.wake)
        ])

    def wake(self):
        scr("You wake up again to the same ceiling and the same quiet room, but this morning your mind feels sharper than ever. The black stage, the hospital flashes, the changing city—all of it stacks into one clear idea: this world is not normal. It bends with you. It hurts with you. And today, you decide to see how far it will bend when you push it on purpose.")
        return wait_for_choice([
            ("Think it through", self.plan),
            ("Get up immediately", self.stand)
        ])

    def plan(self):
        scr("You lie still and lay out a plan in your head. No more random flailing, no more accidents just to see if you survive. You will repeat some things exactly, change others completely, and watch what the world does in response. For once, the loop is not just happening to you—you are going to treat it like an experiment.")
        return wait_for_choice([
            ("Stand up", self.stand)
        ])

    def stand(self):
        scr("You sit up and stand, feeling the familiar heaviness in your limbs. The clock still claims it is 7:00 AM, 24th of July, but you don’t stare at it like a threat this time. You nod at it like a label on a folder. Today’s file. Today’s test. You take a breath and decide where to go first.")
        return wait_for_choice([
            ("Go to Mr.Juger", self.to_juger),
            ("Go to the road", self.to_road_first)
        ])

    def to_juger(self):
        scr("You walk the familiar path toward where Mr.Juger usually stands. The houses, the fence, the uneven pavement all slide by like scenery you’ve memorised. This time you are not just going to greet him and move on. This time you are bringing hospital words into the street.")
        return wait_for_choice([
            ("Watch him first", self.juger_watch),
            ("Greet him directly", self.juger_greet)
        ])

    def juger_watch(self):
        scr("You stop before he notices you and simply watch. Mr.Juger checks his watch, shifts his weight, glances down the road. For a second, his outline flickers, like you’re seeing him from two angles at once—neighbour on the street and man under harsh white lights. You decide it’s time to talk.")
        return wait_for_choice([
            ("Greet him", self.juger_greet)
        ])

    def juger_greet(self):
        scr("You step forward and say, 'Good morning.' He looks up and smiles in that tired, familiar way, answering with almost the same line he always uses. Almost. There is a small extra word there, a hint that the script is drifting. Before he can settle, you push.")
        return wait_for_choice([
            ("Ask about vitals", self.juger_vitals),
            ("Ask about the night", self.juger_night)
        ])

    def juger_vitals(self):
        scr("You ask him, as casually as you can, how your vitals looked yesterday. The street should not be able to hold that sentence, but it does. For a heartbeat, his whole body goes still, and when he answers, his tone is wrong—too calm, too practiced, like a doctor giving a report. Then he blinks and laughs it off, trying to fold it back into a neighbour’s small talk.")
        return wait_for_choice([
            ("Press him more", self.juger_press),
            ("Leave him for now", self.after_juger)
        ])

    def juger_night(self):
        scr("You ask him if the beeps kept going all night. The word hangs in the air heavier than it should. Mr.Juger opens his mouth, closes it once, then says something safe about sleeping badly, about old age and restless nights. Beneath his voice, you hear an echo that doesn’t belong to this street at all—someone checking a monitor, watching a line on a screen.")
        return wait_for_choice([
            ("Press him more", self.juger_press),
            ("Leave him for now", self.after_juger)
        ])

    def juger_press(self):
        scr("You push a little harder, asking if he feels like he has done this morning before. His eyes unfocus for a moment, like he’s listening to a sound only he can hear. For that moment, he looks more like the doctor you glimpsed than the neighbour you know. Then he shakes his head and tells you not to think too much, that some days just blend together. The words feel rehearsed.")
        return wait_for_choice([
            ("Walk away", self.after_juger)
        ])

    def after_juger(self):
        scr("You walk away from him, heart beating faster. He changed. Not much, not obviously, but enough. A new word here, a stumble there, a tone that didn’t belong. The loop isn’t perfectly copying his lines anymore. It is rewriting them with you.")
        return wait_for_choice([
            ("Go to the road", self.to_road),
            ("Visit the homeless man", self.to_homeless)
        ])

    def to_road_first(self):
        scr("You decide to begin with the road where so many of your days have ended in metal and blood. The path there feels burned into your muscles by now. You follow it without thinking, but your mind stays sharp, ready to see what happens when you change your part in the scene.")
        return wait_for_choice([
            ("Continue", self.to_road)
        ])

    def to_road(self):
        scr("You reach the familiar stretch of asphalt. The place where cars hit you, where trucks didn’t slow down, where you tested how far you could push pain. Today, you stand at the edge first, watching. The traffic feels lazy, slightly out of sync with your memory, like the scene is waiting for your cue.")
        return wait_for_choice([
            ("Repeat old pattern", self.road_repeat),
            ("Break it completely", self.road_break)
        ])

    def road_repeat(self):
        scr("You decide to repeat an older choice as closely as you can. You wait until about the time you remember the car appearing, then step into the road at the same angle, in the same place. Your chest tightens, expecting the impact. A car does appear, but this time it slows earlier, brakes softer, and stops before reaching you. The scene lines up almost right, but not perfectly.")
        return wait_for_choice([
            ("Step back", self.after_road),
            ("Stay and test more", self.road_test_driver)
        ])

    def road_break(self):
        scr("Instead of stepping into the lane, you turn your back on the road at the exact moment you used to walk into it. You hear a car rush by behind you, feeling the wind on your skin, but there is no impact, no shattering glass, no crunch of bones. The danger passes like a missed beat in a song. The scene rewrote itself around your refusal.")
        return wait_for_choice([
            ("Look back once", self.after_road),
            ("Move on quickly", self.after_road)
        ])

    def road_test_driver(self):
        scr("You stand in front of the stopped car longer than you should, staring at the driver. Their face feels wrong, unfinished around the edges, like a sketch the world never expected you to stare at this closely. When they lower the window, their mouth moves, but no sound comes out at first. Eventually a generic scolding line pushes through, flat and flavourless, as if the script only remembered it at the last second.")
        return wait_for_choice([
            ("Step aside", self.after_road)
        ])

    def after_road(self):
        scr("You step back to the sidewalk, your heart still pounding, but not from fear of dying. It is the fear of what you are doing to this place. The more precisely you repeat your old mistakes, the more the world tries to replay them. The more sharply you deviate, the more it scrambles to keep up.")
        return wait_for_choice([
            ("Visit the homeless man", self.to_homeless),
            ("Go to the school", self.to_school)
        ])

    def to_homeless(self):
        scr("You turn toward the corner where the homeless man sits, the one who spoke of people going away and coming back with the sound of a beep. Today, you aren’t coming to ask about the day or the weather. You’re coming to ask about the frame around all of this.")
        return wait_for_choice([
            ("Approach him", self.homeless_talk)
        ])

    def homeless_talk(self):
        scr("You sit near him, close enough to hear him breathe. He opens one eye and looks at you, recognition deeper now than in the early loops. You don’t waste time. You ask if he heard the beeps last night again, if he noticed how long you were gone.")
        return wait_for_choice([
            ("Listen to his answer", self.homeless_answer)
        ])

    def homeless_answer(self):
        scr("He frowns, like you are asking him to remember something heavy. He says he heard them, yes, softer than before but still there. Says sometimes it feels like hours between the beeps, sometimes only seconds, but he always knows when 'you' are gone and when 'you' are back. He taps his temple when he says you, as if he is talking about more than one version of you at once.")
        return wait_for_choice([
            ("Ask what he sees", self.homeless_see),
            ("Leave it be", self.after_homeless)
        ])

    def homeless_see(self):
        scr("You ask what he sees when you are gone. He looks past you, into some middle distance, and says he doesn’t see you anywhere on the street. Just hears the beeps and the voices talking over them. The more he speaks, the more his words tilt toward places that don’t exist in this city—rooms with white walls, shoes that squeak on polished floors, machines that sigh.")
        return wait_for_choice([
            ("Thank him", self.after_homeless)
        ])

    def after_homeless(self):
        scr("You thank him and stand, feeling a strange guilt settle in your chest. Every time you 'tested' a death here, he was somewhere in the background, listening to the aftermath in another world. He is not just scenery; he has been counting your disappearances.")
        return wait_for_choice([
            ("Go to the school", self.to_school),
            ("Head into the city", self.city_hub)
        ])

    def to_school(self):
        scr("You make your way to the school again, the place where the boy waits in his frozen classroom. Today, you are not here to pull secrets out of him. You are here to acknowledge him as part of the system you’ve been pulling apart.")
        return wait_for_choice([
            ("Enter the school", self.school_entry)
        ])

    def school_entry(self):
        scr("The halls greet you with the same echo, the same stillness, but now you read them differently. You see them as corridors inside your own head, lined with rows of desks holding versions of yourself that never got up. You walk to the familiar doorway and find the boy exactly where he always is, sitting, watching the window.")
        return wait_for_choice([
            ("Talk to him", self.school_boy_talk),
            ("Sit in silence", self.school_boy_sit)
        ])

    def school_boy_talk(self):
        scr("You sit near him and ask if he ever gets tired of watching you run into the same walls. His eyes flick to you, then back to the window. He says that he knew you would stop eventually, or break trying. When you ask what he means, he just says he is the part that waits to see which one you choose.")
        return wait_for_choice([
            ("Stay a bit longer", self.school_boy_stay)
        ])

    def school_boy_sit(self):
        scr("You sit down at the next desk without saying anything. The two of you share a silence that feels heavier than most conversations. You realise you have spent so many loops moving, testing, dying, that you rarely just sat still with yourself. In that quiet, you feel the ache of all the times you forced the story forward when it could have rested.")
        return wait_for_choice([
            ("Say something", self.school_boy_talk)
        ])

    def school_boy_stay(self):
        scr("You stay until the room feels too full of all the words you are not ready to hear. When you finally stand, the boy does not ask you to stay or go. He only tells you not to forget that staying still is also a choice, and sometimes the only one that doesn’t make things worse.")
        return wait_for_choice([
            ("Leave the school", self.after_school)
        ])

    def after_school(self):
        scr("You leave the school with your steps echoing behind you, each one a reminder that your movement drives this place. The experiments you ran today have taught you something you didn’t expect: you are not powerless here, but your power cuts both ways. Every forced glitch, every test of pain, lands on someone real.")
        return wait_for_choice([
            ("Explore the city more", self.city_hub),
            ("Go home early", self.end_day)
        ])

    def city_hub(self):
        scr("You wander deeper into the city, testing smaller things now instead of big ones. You repeat a path exactly and see some details line up like they have before. You change your route sharply and feel the world wobble to fill in the gaps. Shop signs twitch between messages. Background people glitch for a heartbeat when you stare too long. The city behaves less like a place and more like a story trying to keep up with you.")
        return wait_for_choice([
            ("Test one more thing", self.city_test),
            ("Stop experimenting", self.end_day)
        ])

    def city_test(self):
        scr("You pick one small, meaningless detail—a bench, a sign, a doorway—and force yourself to pass it three times in the same way. Each time, something about it shifts. A word changes, a crack in the wood moves, the angle of the light tilts. The loop is not an exact copy machine. It is an active process, redrawing the day again and again.")
        return wait_for_choice([
            ("Enough for today", self.end_day)
        ])

    def end_day(self):
        scr("By the time you start walking back home, your head is heavy with observations and a tight, low guilt. You proved that you can bend this place, that nothing here is perfectly fixed, that people and streets and signs all drift when you press them. But you also proved that every pressure you apply pulls on the nerves of someone lying under real lights, breathing real air, feeling real pain.")
        return wait_for_choice([
            ("Go home", self.go_home)
        ])

    def go_home(self):
        scr("You step back into your room, the same four walls, the same ceiling, the same bed that has caught you after so many bad endings. Tonight, you don’t throw yourself into another test. You sit on the edge of the mattress and realise that experimenting with your own suffering might not be progress at all—it might just be a new way to hurt the part of you that never gets to leave the hospital bed.")
        return wait_for_choice([
            ("Lie down", self.sleep)
        ])

    def sleep(self):
        scr("You lie back and let the day replay in your mind. The changed words, the hesitant answers, the strained edges of the world. You know now that you can keep pushing for glitches and glimpses, but every time you do, something real has to hold that strain. As your eyes close, not from injury but from sheer exhaustion, you understand that tomorrow’s choice won’t just be about surviving the loop. It will be about deciding how much more of this you are willing to force yourself through.")
        return wait_for_choice([
            ("...", self.manager.chapter11.intro)
        ])

class Chapter11:
    def __init__(self, manager):
        self.manager = manager

    def intro(self):
        scr("Chapter 11: The Frayed Edge")
        return wait_for_choice([
            ("Continue", self.wake)
        ])

    def wake(self):
        scr("You wake up again to the same ceiling and the same quiet, but the sharp edge of curiosity from yesterday has dulled into a deep, bone-heavy tiredness. The memory of the experiments you ran weighs on you—the pushed glitches, the forced answers, the way the world strained to keep up. For the first time, you are not excited to see what you can break. You are afraid of how much more breaking there is left to do.")
        return wait_for_choice([
            ("Stay in bed a moment", self.still),
            ("Get up slowly", self.rise)
        ])

    def still(self):
        scr("You stay lying down, staring at the ceiling cracks that you’ve traced a hundred times. You think about the flashes of white, the hints of metal and straps, the wordless presence of a body that felt every crash you turned into an experiment. The thought that your curiosity might be hurting that body sinks in, heavy and cold.")
        return wait_for_choice([
            ("Sit up", self.rise)
        ])

    def rise(self):
        scr("You sit up and swing your legs over the side of the bed. The clock is there, as always, repeating its line: 7:00 AM, 24th of July. You look at it only long enough to confirm what you already knew, then let your eyes drift away. Today is not a day for new tests. Today is a day for seeing what happens when you do as little as possible.")
        return wait_for_choice([
            ("Leave the room", self.leave_room)
        ])

    def leave_room(self):
        scr("You open the door and step into the hallway, then out into the street. The air feels thinner, the light flatter, as if the world is tired too. You decide you will walk, but not chase. Watch, but not poke. If this loop wants to show you something, it will have to do it without you dragging it into the open.")
        return wait_for_choice([
            ("Go toward Mr.Juger", self.to_juger),
            ("Go to the bench near the crossing", self.to_bench)
        ])

    def to_juger(self):
        scr("You walk toward the place where Mr.Juger usually appears. Your feet know the way, even if your mind is slower than usual. When you spot him, standing in his familiar spot, you feel less like confronting him with questions and more like seeing how he behaves when you don’t pull him off script.")
        return wait_for_choice([
            ("Approach him", self.juger_meet),
            ("Watch from a distance", self.juger_watch)
        ])

    def juger_watch(self):
        scr("You hang back and watch as he adjusts his glasses, checks his watch, and glances down the road. It all looks ordinary on the surface, but now you notice the stiffness in his shoulders, the way his head turns as if listening for something far away. Even without your interference, there is a tension humming beneath his movements.")
        return wait_for_choice([
            ("Approach him", self.juger_meet),
            ("Leave him alone", self.after_juger)
        ])

    def juger_meet(self):
        scr("You walk up and greet him with a simple 'Good morning.' This time, you don’t shove hospital words into the conversation. He responds with a normal line about the day, but buried under it you hear a faint echo—a calmer, more clinical version of his voice asking a question you can’t quite catch. For a moment, it feels like two people are speaking through his mouth at once.")
        return wait_for_choice([
            ("Answer simply", self.juger_simple),
            ("Say nothing more", self.after_juger)
        ])

    def juger_simple(self):
        scr("You tell him you are 'managing' and leave it at that. He nods with a look that sits somewhere between neighbourly concern and professional assessment. It is the first time you feel like maybe he is watching over more than just this street, and you are not sure if that comforts you or scares you.")
        return wait_for_choice([
            ("Walk away", self.after_juger)
        ])

    def after_juger(self):
        scr("You walk away without forcing the scene to crack open. Even without your prodding, his words and presence are heavy with things unsaid. The city does not need you to shout at it to show its seams anymore. They are starting to show on their own.")
        return wait_for_choice([
            ("Go sit by the crossing", self.to_bench),
            ("Wander aimlessly", self.wander)
        ])

    def to_bench(self):
        scr("You head to the bench near the crossing, the place where so many of your violent endings began. The road lies ahead, quiet for now, the crossing light blinking its familiar pattern. Instead of stepping into the flow, you sit down and decide not to move for a while.")
        return wait_for_choice([
            ("Stay seated", self.bench_still)
        ])

    def bench_still(self):
        scr("You sit and watch the world try to run around you. A car passes. A cyclist glides by. A few people cross the street. At first it all seems normal, but then you notice gaps—moments where everything pauses for a fraction of a second, like the scene forgot what to do next. The beeping rhythm, once buried in the noise, rises to the surface, steady and patient.")
        return wait_for_choice([
            ("Close your eyes", self.bench_close),
            ("Keep watching", self.bench_watch)
        ])

    def bench_watch(self):
        scr("You keep your eyes open and track every small glitch. A man lifts his hand to check his watch, then resets to that pose again when you look away and back. A woman’s lips move in conversation, but the words reach your ears a heartbeat late. The world feels like a film reel slipping on the projector.")
        return wait_for_choice([
            ("Close your eyes", self.bench_close)
        ])

    def bench_close(self):
        scr("You close your eyes and let the visual noise drop away. Without it, the soundscape sharpens. Footsteps blur into a distant murmur, and underneath it all, the beep comes into focus. A short tone, a pause, another tone. It is no longer pretending to be anything else. Your breathing starts to fall into sync with it whether you want it to or not.")
        return wait_for_choice([
            ("Listen", self.bench_listen)
        ])

    def bench_listen(self):
        scr("As you listen, other sounds slip in at the edges. A voice says something about 'stability.' Another asks how long it has been. A third voice—calm, professional—mentions your name followed by numbers you don’t recognise. The bench under you feels less like wood now and more like something narrow and hard, like a bed with rails.")
        return wait_for_choice([
            ("Open your eyes", self.fracture_start)
        ])

    def fracture_start(self):
        scr("You open your eyes, but for a split second, you do not see the street. You see white. A ceiling with harsh rectangular lights. The outline of machines standing guard. The ghost of straps around wrists that are not moving. Then the image snaps back to the crossing, colours wrong for a moment before they settle.")
        return wait_for_choice([
            ("Try to hold onto it", self.fracture_pull),
            ("Let it pass", self.fracture_pass)
        ])

    def fracture_pull(self):
        scr("You try to hold onto the image, to drag yourself back into that white room, but the harder you pull, the more the world around you judders. Cars freeze mid-roll. People hang mid-step. The bench feels like it is tilting under you. A sharp pain stabs through your chest, as if some invisible wire has been pulled too tight.")
        return wait_for_choice([
            ("Stop fighting", self.fracture_drop)
        ])

    def fracture_pass(self):
        scr("You let the image drift away instead of chasing it. The street reasserts itself, but imperfectly. The colours feel oversaturated, the movements slightly too smooth. You realise that maybe this world is not meant to carry the full weight of the place you glimpsed, and every time you force it to, something fragile strains.")
        return wait_for_choice([
            ("Sit very still", self.fracture_drop)
        ])

    def fracture_drop(self):
        scr("Everything goes unnaturally quiet. The cars, the people, even the wind seem to pause. For a heartbeat, you exist in a space between—no street, no hospital, just a weightless awareness that you are suspended over something you don’t fully understand. Then the sound rushes back in, the scene unfreezes, and life in the loop pretends nothing happened.")
        return wait_for_choice([
            ("Stand up", self.after_bench)
        ])

    def after_bench(self):
        scr("You stand on shaky legs and step away from the bench. Your heart is pounding, but not from an external threat. It is from the knowledge that you were closer than ever to the real room, the real body, the real situation—and you still don’t know if you want to live there or here.")
        return wait_for_choice([
            ("Walk without a goal", self.wander),
            ("Head toward the school", self.to_school)
        ])

    def wander(self):
        scr("You walk with no destination, letting your feet choose the path. The city flows around you in a daze of almost-normality. Conversations almost make sense, then tilt sideways into words that belong to charts and procedures. The more you listen, the more you hear phrases like 'unresponsive' and 'we’ll wait and see' tucked between talk of groceries and traffic.")
        return wait_for_choice([
            ("Keep wandering", self.wander_more),
            ("Go home", self.end_day_prompt)
        ])

    def wander_more(self):
        scr("You start to feel as if you are walking through layers of transparent worlds stacked on top of each other. In one, this is just a street and you are just a person walking. In another, this is a corridor and someone is being wheeled past rooms you can’t see inside. The two realities rub against each other, sparks flying where they don’t quite align.")
        return wait_for_choice([
            ("Go home", self.end_day_prompt),
            ("Head toward the school", self.to_school)
        ])

    def to_school(self):
        scr("You drift back toward the school without entirely meaning to. The building looms like a memory you haven’t finished processing. You don’t go deep this time. You only stand by the gate, looking in at the quiet halls, feeling the weight of all the versions of you that walked through them in other loops.")
        return wait_for_choice([
            ("Leave it alone today", self.end_day_prompt),
            ("Step inside briefly", self.school_brief)
        ])

    def school_brief(self):
        scr("You step inside just long enough to smell the chalk and hear your footsteps echo once against the walls. The boy is somewhere inside, you can feel it, but you don’t go to him. Today, you aren’t here to look for more pieces. You are here to admit that every piece you already have is heavier than you know what to do with.")
        return wait_for_choice([
            ("Leave the school", self.end_day_prompt)
        ])

    def end_day_prompt(self):
        scr("By now, the light has shifted in that familiar way that tells you this version of the day is winding down. Your head buzzes with the memory of white ceilings and strapped arms, of words about stability and waiting, of a world that exists just beyond the painted walls of this one. You are too tired to pull at those walls any more today.")
        return wait_for_choice([
            ("Go home", self.go_home)
        ])

    def go_home(self):
        scr("You return to your room, the one constant stage that has welcomed you at the end of every path. You sit on the bed and feel the day settle on your shoulders. You think about how easily you could spend the next loops doing nothing but forcing more fractures, demanding more glimpses, dragging the hospital world into this one. You also think about the body that has to pay for every forced glitch.")
        return wait_for_choice([
            ("Lie down", self.sleep)
        ])

    def sleep(self):
        scr("You lie back and close your eyes, not because you were knocked down or stabbed or crushed, but because you are simply done for today. Done with experiments. Done with pulling. Done with trying to solve something that might not want to be solved by force. As the beep drifts in from somewhere far away, softer than before, you let the thought pass through you: maybe the kindest thing you can do for both worlds is to move more gently, or not at all.")
        return wait_for_choice([
            ("...", self.manager.chapter12.intro)
        ])


class Chapter12:
    def __init__(self, manager):
        self.manager = manager

    def intro(self):
        scr("Chapter 12: Giving In to Tiredness")
        return wait_for_choice([
            ("Continue", self.wake)
        ])

    def wake(self):
        scr("You wake up again, but this time there is no rush of panic, no surge of plans. The ceiling above you looks the same, the cracks in the paint follow the same paths, and the clock, if you chose to look at it, would still say 7:00 AM, 24th of July. You don’t look. You lie there in the quiet and feel how heavy your body and thoughts have become after everything you’ve tried.")
        return wait_for_choice([
            ("Stay still a bit longer", self.stay),
            ("Sit up slowly", self.sit)
        ])

    def stay(self):
        scr("You stay on your back, letting the familiar weight of the blanket and the pressure of the mattress hold you in place. Memories drift through you without urgency: the black stage, the hospital flashes, Mr.Juger’s half-slips, the homeless man’s beeps, the boy’s tired gaze. You don’t chase any of them. They pass through your mind like clouds.")
        return wait_for_choice([
            ("Sit up", self.sit)
        ])

    def sit(self):
        scr("You sit up, moving carefully as if sudden motions might tear something fragile. You do not check the time. You already know what it will say, and for once that knowledge doesn’t sting as sharply. Instead, you think a simple thought: you are tired. Not just in this loop, but in all the loops behind it. And maybe you don’t have to fight every second of this day.")
        return wait_for_choice([
            ("Stand up", self.stand)
        ])

    def stand(self):
        scr("You stand and let your eyes pass over the room without inspecting every corner. The bandages and scars are there if you want to look at them, but you choose not to add more today. You decide that this loop will be smaller, softer. No experiments. No forced cracks. Just a day walked without trying to break it open.")
        return wait_for_choice([
            ("Leave the room", self.leave_room)
        ])

    def leave_room(self):
        scr("You open the door and step outside. The corridor, the stairs, the entrance, the street—each part of the morning feels like a scene you have rehearsed too many times. Instead of scanning for glitches, you simply move through it, letting the world be what it is without demanding more. The air is cool. Your steps are steady. There is nowhere you urgently need to be.")
        return wait_for_choice([
            ("Go toward Mr.Juger", self.to_juger),
            ("Head toward the school", self.to_school),
            ("Take a slow walk through the streets", self.to_city)
        ])

    def to_juger(self):
        scr("You follow the path to where Mr.Juger usually stands, not to test him, but to see how it feels to meet him without a hidden agenda. When you spot him ahead, his familiar shape waiting in its familiar place, you feel less like confronting him and more like acknowledging that he has been here, loop after loop, whether you wanted him to be or not.")
        return wait_for_choice([
            ("Greet him", self.juger_meet),
            ("Just walk past today", self.after_juger)
        ])

    def juger_meet(self):
        scr("You walk up and say, 'Good morning,' with no trick in your voice. He replies with an uncomplicated line, asking how you are, telling you to take care. You answer simply that you are tired but managing. For a split second, you hear something else under his words—a gentler note, a professional cadence—but you don’t trap it, don’t demand he repeat it. You let it drift away.")
        return wait_for_choice([
            ("Say goodbye", self.after_juger)
        ])

    def after_juger(self):
        scr("You leave him where he is, the moment small and almost ordinary. You don’t turn around to see if his outline flickers or if his eyes follow you too long. If there is a doctor inside that shadow, you choose not to drag him to the surface today. You keep walking.")
        return wait_for_choice([
            ("Head toward the school", self.to_school),
            ("Wander the streets", self.to_city)
        ])

    def to_school(self):
        scr("You walk toward the school without urgency. The building rises ahead, a stack of old routines and unfinished thoughts. In other loops, you came here to pry something out of it. Today, you come simply because it is part of your day, and avoiding it would be the same as pretending you never went to school at all.")
        return wait_for_choice([
            ("Enter the school", self.school_entry),
            ("Walk past it this time", self.after_school)
        ])

    def school_entry(self):
        scr("You step through the gate and into the quiet halls. The echo of your footsteps sounds familiar, but you don’t listen for hidden beeps in it. Classrooms sit open, neat and motionless. You go to the boy’s classroom almost by instinct, not to interrogate him, but to see him again.")
        return wait_for_choice([
            ("Sit with the boy", self.school_boy),
            ("Glance in and leave", self.school_glance)
        ])

    def school_boy(self):
        scr("You enter and take your usual place at a nearby desk. The boy turns, gives you his small, neutral look, then returns his gaze to the window. You sit in silence with him, sharing the same air, the same light, the same moment. You don’t ask who he is or what he wants from you. You simply let him exist alongside you, the still part of you keeping company with the restless part that is finally learning how to rest.")
        return wait_for_choice([
            ("Leave the classroom", self.after_school)
        ])

    def school_glance(self):
        scr("You pause at the doorway just long enough to see him there, in his seat, exactly where you expect him to be. He doesn’t look up this time, and you don’t step in. Knowing he is there is enough. You let the classroom be his space and turn away.")
        return wait_for_choice([
            ("Leave the school", self.after_school)
        ])

    def after_school(self):
        scr("You step back out into the hall and then out of the building. The school remains behind you, full of versions of you that studied, hid, waited, and watched. For the first time in a long time, you let it stay a memory instead of a problem to be solved.")
        return wait_for_choice([
            ("Walk through the city", self.to_city),
            ("Head home early", self.to_home)
        ])

    def to_city(self):
        scr("You walk the streets without a target, letting the city unfold at its own pace. People move along their paths, some with the depth of real lives, others with the simplicity of background loops. Signs hang where they always have, their words stable enough if you don’t stare too long. You notice small oddities out of the corner of your eye, but you don’t stop to force them into focus.")
        return wait_for_choice([
            ("Keep wandering", self.city_wander),
            ("Start heading home", self.to_home)
        ])

    def city_wander(self):
        scr("You take turns without thinking too hard about them, drifting past corners you have seen and ones you barely remember. At the edge of your hearing, fragments of phrases float by—'monitoring', 'no worse', 'give it time'—but they feel less like clues and more like background noise now. You acknowledge them and keep moving. Not every echo has to become a door.")
        return wait_for_choice([
            ("Head home now", self.to_home)
        ])

    def to_home(self):
        scr("Eventually, the weight in your legs and behind your eyes convinces you that today does not need any more walking. You turn back toward home, retracing familiar steps. The streets feel a little less like traps and a little more like worn paths through a story you have told yourself too many times.")
        return wait_for_choice([
            ("Enter your home", self.home_enter)
        ])

    def home_enter(self):
        scr("You open your door and step inside. The quiet of your room greets you like a tired friend. The same furniture, the same bed, the same four walls—nothing here has changed in any dramatic way. The difference sits inside you: the absence of a plan to twist this place into giving you more than it already has.")
        return wait_for_choice([
            ("Sit on the bed", self.home_sit)
        ])

    def home_sit(self):
        scr("You sit on the edge of your bed and let your mind skim over the day. You saw Mr.Juger and chose not to pull him apart. You went to the school and chose not to demand anything from the boy. You walked the city and didn’t tear at its edges. You did not test the road, did not chase the beeps, did not try to force another fracture.")
        return wait_for_choice([
            ("Lie down", self.home_lie)
        ])

    def home_lie(self):
        scr("You lie back and stare at the ceiling one more time. The tiredness that rolls over you now is not the shock of impact or the numbness after blood loss. It is the dull, honest exhaustion of someone who has been carrying too many questions for too long. You realise you don’t have to find every answer today. Maybe not ever.")
        return wait_for_choice([
            ("Close your eyes", self.sleep)
        ])

    def sleep(self):
        scr("You close your eyes, not because the loop has forced you to, but because you are choosing to stop for now. The distant beep is still there, faint and steady, but you don’t strain to match your breathing to it. You do not reach out to the hospital world or drag the city into another test. You let yourself drift, sinking into the tiredness without fighting it, without promising yourself that tomorrow you will do more. For the first time, resting feels like enough.")
        return wait_for_choice([
            ("...", self.manager.chapter13.intro)
        ])

class Chapter13:
    def __init__(self, manager):
        self.manager = manager

    def intro(self):
        scr("Chapter 13: The Day That Might Be Different")
        return wait_for_choice([
            ("Continue", self.wake)
        ])

    def wake(self):
        scr("You drift up toward awareness, but it feels slower this time, like floating instead of rising. There is fabric under your hands, a familiar weight on your chest, a thickness in the air that could be your room or somewhere else entirely. You know, without looking, that if you checked the clock it would still say 7:00 AM, 24th of July. You choose not to check. For once, the number doesn’t matter as much as the simple fact that you are here.")
        return wait_for_choice([
            ("Sit up", self.sit),
            ("Stay lying down a moment", self.stay)
        ])

    def stay(self):
        scr("You stay on your back, eyes half-open, watching the ceiling blur at the edges. Your mind feels dull and soft, like it has finally stopped trying to run ahead of itself. Thoughts of experiments, fractures, beeps and white ceilings drift across your mind’s surface, but none of them stick. You are tired, and your tiredness is bigger than any question you could ask right now.")
        return wait_for_choice([
            ("Sit up", self.sit)
        ])

    def sit(self):
        scr("You sit up slowly, letting your feet find the floor. The room feels distant and close at the same time, like a memory you haven’t decided to keep or let go of. You don’t scan for changes. You don’t recite lists of clues. You pause, breathe, and accept that you have nothing new to prove today.")
        return wait_for_choice([
            ("Stand up", self.stand)
        ])

    def stand(self):
        scr("You stand and move through your small morning without thinking too hard about it. Your hands know where everything is. Your body knows the order of movements. There is comfort in the automatic nature of it. You aren’t trying to optimise the loop or test its rules anymore. You are just letting it play out, one small action at a time.")
        return wait_for_choice([
            ("Step outside", self.leave_home)
        ])

    def leave_home(self):
        scr("You open the door and step onto the street. The air feels familiar against your skin. The world around you has the same outline as every other day, but you are not peering at the edges, not pulling at the seams. You walk without a destination, letting your feet decide where to go, like muscle memory is telling the story for you now.")
        return wait_for_choice([
            ("Walk your usual path", self.path_usual),
            ("Take a different turn", self.path_drift)
        ])

    def path_usual(self):
        scr("You follow the route your body has worn into this world—past the place where Mr.Juger often stands, past the road that has held so many of your endings, past the corner where the homeless man sits. You see shapes, colours, familiar outlines, but you do not sharpen them into scenes. You let them remain background, just this once.")
        return wait_for_choice([
            ("Keep walking", self.walk_on)
        ])

    def path_drift(self):
        scr("You turn down a side street, not one of the important ones, just a path that has always been there without ever being the centre of anything. The buildings here are quiet, the windows still. It feels like walking through an unwritten part of your own memory, a place that exists because it might have, not because it ever did.")
        return wait_for_choice([
            ("Keep walking", self.walk_on)
        ])

    def walk_on(self):
        scr("As you walk, you catch small overlaps without reaching for them. A shop window reflects the sky, and for a heartbeat the blue turns sterile white before becoming sky again. A passing voice says something about 'today' and 'no change', but the words slide off you before they can root. The distant beep is still there somewhere, but it sounds farther away, like a hallway down you’re no longer walking.")
        return wait_for_choice([
            ("Head back home", self.head_home),
            ("Pause and look around once", self.pause_once)
        ])

    def pause_once(self):
        scr("You stop and turn on the spot, taking in the city as a whole instead of in pieces. Streets, signs, people, buildings—all of it hangs together like a painting you’ve stared at too long. You feel no urge to step into traffic, no desire to chase a glitch, no need to interrogate every shadow for answers. You simply nod at the world that has held you this long, a quiet acknowledgement between you and whatever built it.")
        return wait_for_choice([
            ("Go home now", self.head_home)
        ])

    def head_home(self):
        scr("You make your way back toward your house, your steps feeling heavier and lighter at the same time. Heavier with accumulated loops and memories; lighter because, for once, you are not trying to outrun or outthink them. You reach your door without incident, without drama, and go inside as if you have done this a thousand times—which you have.")
        return wait_for_choice([
            ("Go to your room", self.room)
        ])

    def room(self):
        scr("You enter your room and are met with the same four walls, the same bed, the same familiar shapes. It feels smaller than the city, but more honest. This is where every day has begun and ended. This is where you have woken, and collapsed, and tried again. You sit down on the edge of the bed and let the quiet settle in around you.")
        return wait_for_choice([
            ("Lie down", self.lie),
            ("Sit for a while", self.sit_longer)
        ])

    def sit_longer(self):
        scr("You sit a little longer, elbows on your knees, head lowered. If you wanted to, you could replay the entire story in your mind—the accidents, the voices, the loops, the tests, the glimpses of white. Instead, you let the memories blur at the edges. You accept that you have seen enough to know things are wrong and unfinished, and that you may never know exactly how they end.")
        return wait_for_choice([
            ("Lie down", self.lie)
        ])

    def lie(self):
        scr("You lie back on the bed and stare at the ceiling one last time. The cracks no longer look like clues, just cracks. The air no longer feels like a hidden message, just air. Your body relaxes into the mattress, muscle by muscle, as if it has finally been given permission to stop rehearsing and simply rest.")
        return wait_for_choice([
            ("Close your eyes", self.close_eyes)
        ])

    def close_eyes(self):
        scr("You close your eyes. Darkness blooms, but it is not the sharp black of the dream stage or the flicker of a failing scene. It is soft and deep and strangely kind. Somewhere very far away, a beep continues its slow, steady counting. It might be measuring your heartbeat. It might be measuring the time left in this day. You are too tired to decide which.")
        return wait_for_choice([
            ("Let yourself drift", self.drift)
        ])

    def drift(self):
        scr("You feel yourself drifting, not up, not down, just away from the edges of the room. Your sense of the city loosens, the hallways and streets and classrooms unhooking themselves from your thoughts. You do not know if you are rising toward waking or sinking further into sleep. You only know that you are not fighting it anymore.")
        return wait_for_choice([
            ("...", self.end_options)
        ])

    def end_options(self):
        scr("Everything narrows to a single, quiet moment. If you wanted to, you could try again. Open your eyes. Stand up. Walk the streets. Test the seams of this day one more time. Or you could let it all go and step away from the loop, whatever that means, wherever it leads.\n\nThis is the end of the story you have been told so far.")
        return wait_for_choice([
            ("Restart the day", self.manager.chapter1.ch1),
            ("Quit", self.quit_game)
        ])

    def quit_game(self):
        pygame.quit()
        sys.exit()



class SceneManager:
    def __init__(self):
        self.chapter1 = ChapterStart(self)
        self.chapter2 = Chapter2(self)
        self.chapter3 = Chapter3(self)
        self.chapter4 = Chapter4(self)
        self.chapter5_1 = Chapter5_1(self)
        self.chapter5_2 = Chapter5_2(self)
        self.chapter6 = Chapter6(self)
        self.chapter7 = Chapter7(self)
        self.chapter8 = Chapter8(self)
        self.chapter9 = Chapter9(self)
        self.chapter10 = Chapter10(self)
        self.chapter11 = Chapter11(self)
        self.chapter12 = Chapter12(self)
        self.chapter13 = Chapter13(self)
        self.current_scene = self.chapter1.ch1

    def run(self):
        while True:
            self.current_scene = self.current_scene()

def main():
    global scene_manager
    scene_manager = SceneManager()
    scene_manager.run()

if __name__ == "__main__":
    main()
