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
        scr("You walk out and greet Mr.Juger, he greet you back and enquires about the bandaid you are wearing. You tell him a half baked lie, he doesn't seem to notice and asks you to be more careful with your own body. You nod and ...")
        return wait_for_choice([
            ("Walk away",self.walk),
            ("Ask Him",self.ask_juger)
        ])



class SceneManager:
    def __init__(self):
        self.chapter1 = ChapterStart(self)
        self.chapter2 = Chapter2(self)
        self.chapter3 = Chapter3(self)
        self.chapter4 = Chapter4(self)
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
