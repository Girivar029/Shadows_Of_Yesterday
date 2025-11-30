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
    
        


class SceneManager:
    def __init__(self):
        self.chapter1 = ChapterStart(self)
        self.chapter2 = Chapter2(self)
        self.chapter3 = Chapter3(self)
        self.chapter4 = Chapter4(self)
        self.chapter5_1 = Chapter5_1(self)
        self.chapter5_2 = Chapter5_2(self)
        self.chapter6 = Chapter6(self)
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
