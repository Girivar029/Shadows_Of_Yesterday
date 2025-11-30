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
    def __init__(self,manager):
        self.manager = manager

    def intro(self):
        scr("Chapter 5: A instinctive decision")
        return wait_for_choice([
            ("Continue",self.do)
        ])

    def do(self):
        scr("You wake up in this day, trying to comprehend the situation you are in. Fed up with the continous day loop that you are in, you decide to try out stuff to check the limilts of this.")
        return wait_for_choice([
            ("Try out pain",self.pain)
        ])
    
    def pain(self):
        scr("You test the limits of pain which you can mentally handle, from aggrevating pain to a lot more accidents, almost reliving every accident from the previous times")
        return wait_for_choice([
            ("Calm Down",self.calma)
        ])
    
    def calma(self):
        scr("You calm down, breathing slowly and reinterpreting all the knowledge you have gathered so far. You know that almost anything you do, lets you back to wake up in the same day. You tried everything that you can to hurt yourself but everything leads you back to this place in the same say and time. You suddenly feel pain.....")
        return wait_for_choice([
            ("Faint",self.faint)
        ])
    
    def faint(self):
        scr("You faint and wait for the moment to wake back up again, but that doesn't happen, you hear a man crying, someone having pain all over their body, you can sense it but cannot pin point how.")
        return wait_for_choice([
            ("Listen More",self.more_patience)
        ])
    
    def more_patience(self):
        scr("You patiently listen more, you hear the man describing all the pain in his body, which feels really uncomfortable. You cannot understand why but you can't escape this moment. After a long time of efforts you, finally wake up.")
        return wait_for_choice([
            ("Check Others",self.others)
        ])
    
    def others(self):
        scr("You decide to check few other theories you have out, you want to do a lot of things now. You have a lot of theories to test. You decide to...")
        return wait_for_choice([
            ("Check interactions",self.inter),
            ("Play with risks",self.risks)
        ])
    
    def inter(self):
        scr("You want to talk to the people and find out what is causing all this, checking for clues, people who can help and anything, anything you want. You decide to ask")
        return wait_for_choice([
            ("Ask Mr.Juger",self.juger),
            ("Ask the homeless man",self.homeless),
            ("Check out the school",self.school)            
        ])
    
    def school(self):
        scr("You decide to wander back ti the school, as it was the last place you had been in the previous renditions of this day. You enter this building, still as empty as ever and decide to keep walking, right back into the place where he had seen the TV. The TV now off gives no new clues to us, almost as if it never did anything in the first place.")
        return wait_for_choice([
            ("Go Deeper",self.deep)
        ])
    
    def deep(self):
        scr("You search the school, more and more, finding nothing in the way. You still look, not knowing what to find, search through benches, locker rooms and others. finding few books with many names on it but all having empty pages, or nothing on them.")
        return wait_for_choice([
            ("Turn Back",self.back)
        ])
    
    def back(self):
        scr("You decide to go back as you did not find anything anyways, but when you decide to walk out, you find a boy, sitting alone in a classroom, you decide to...")
        return wait_for_choice([
            ("Talk",self.talk),
            ("Walk Out",self.out)
        ])
    
    def talk(self):
        scr("You go to him and ask him, trying to find some answers but fid none, almost as if he is mute and deaf. You decide to ask him more questions, trying to get any information from the guy, but all he does is turn towards you and smile, not creepy, not sad just a normal smile and nothing else.")
        return wait_for_choice([
            ("Walk Out",self.out)
        ])
    
    def out(self):
        scr("You walk out and decide to...")
        return wait_for_choice([
            ("Ask Mr.Juger",self.juger)
        ])
    
    def juger(self):
        scr("You find Mr.Juger on the road again, in the same time and place as you usually do, you want to ask him a question but what do you ask...")
        return wait_for_choice([
            ("Ask About Loop",self.ask_loop),
            ("Ask About Time",self.time)
        ])
    
    def ask_loop(self):
        scr("You ask him about a time loop, asking him if it is possible, and will it take place properly and is it even practically possible. He replies telling you that he had heard stories about time loops, of people living through the same day to fulfill a particular thing which finally frees them from the loop. He also mentioned that he doesn't believe in anything like a time loop and thinks it is all a fairy tale.")
        return wait_for_choice([
            ("Ask About Time",self.time),
            ("Leave",self.out_juger)
        ])
    
    def time(self):
        scr("You ask him about the concept of time and how time can be looped, like can time have a start and an end or is it infinte, he answers back laughing it off, telling you it is not very common to be talking about time but time is not a big piece of discussion, and is a very philosophical thing which he cannot answer.")


class Chapter5_2:
    def __init__(self,manager):
        self.manager = manager
        


class SceneManager:
    def __init__(self):
        self.chapter1 = ChapterStart(self)
        self.chapter2 = Chapter2(self)
        self.chapter3 = Chapter3(self)
        self.chapter4 = Chapter4(self)
        self.chapter5_1 = Chapter5_1(self)
        self.chapter5_2 = Chapter5_2(self)
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
