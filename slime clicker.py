import pygame
import random
import pygame_menu

"""from pygame.locals import (
    KEYDOWN,
    K_ESCAPE,
    QUIT,
    MOUSEBUTTONUP,
    K_s,
    K_u,
    K_i,
    K_a,
)"""
from pygame.locals import *
pygame.init()
pygame.font.init()
#import and initialize modules and keys needed

gpTotal = 0
highestGPT = 0


class Bard:
    def __init__(self):
        self.quantity = 0
        self.cost = 10
        self.prod = 0
        self.mult = 1
    def purchase(self):
        global gpTotal
        if gpTotal > self.cost:
            gpTotal -= self.cost
            self.quantity += 1
            self.prod += 1
            self.cost *= 1.2
    def price(self):
        return round(self.cost)
    def quantity(self):
        return self.quantity
    def upgrade(self, multiplier):
        self.mult *= multiplier
    def getProd(self):
        return self.prod * self.mult
        
bardUpgrade = [False, False, False, False, False]
        
class Fighter:
    def __init__(self):
        self.quantity = 0
        self.cost = 110
        self.prod = 0
    def purchase(self):
        global gpTotal
        if gpTotal > self.cost:
            gpTotal -= self.cost
            self.quantity += 1
            self.prod += 10
            self.cost *= 1.2
    def price(self):
        return round(self.cost)
    def quantity(self):
        return self.quantity
    def getProd(self):
        return self.prod        
        
class Druid:
    global gpTotal
    def __init__(self):
        self.quantity = 0
        self.cost = 1200
        self.prod = 0
    def purchase(self):
        global gpTotal
        if gpTotal > self.cost:
            gpTotal -= self.cost
            self.quantity += 1
            self.prod += 90
            self.cost *= 1.2
    def price(self):
        return round(self.cost)
    def quantity(self):
        return self.quantity
    def getProd(self):
        return self.prod

class Rogue:
    global gpTotal
    def __init__(self):
        self.quantity = 0
        self.cost = 13000
        self.prod = 0
    def purchase(self):
        global gpTotal
        if gpTotal > self.cost:
            gpTotal -= self.cost
            self.quantity += 1
            self.prod += 500
            self.cost *= 1.2
    def price(self):
        return round(self.cost)
    def quantity(self):
        return self.quantity
    def getProd(self):
        return self.prod
        
class Archmage:
    global gpTotal
    def __init__(self):
        self.quantity = 0
        self.cost = 250000
        self.prod = 0
    def purchase(self):
        global gpTotal
        if gpTotal > self.cost:
            gpTotal -= self.cost
            self.quantity += 1
            self.prod += 1500
            self.cost *= 1.2
    def price(self):
        return round(self.cost)
    def quantity(self):
        return self.quantity
    def getProd(self):
        return self.prod
        
#^adventurer classes 
    
clickMultiplier = 1
clickFlat = 0

bMU = [['Bard College', False, 500], ['Louder Lutes', False, 5500], ['Snappier Strings', False, 55500]]

fMU = [['Beefier Armor', False, 2000], ['Diamond Hands', False, 20000]]

dMU = [['Watering Cans', False, 10000], ['Weather Magic', False, 100000], ['Wooden Coinage', False, 1000000]]

rMU = [['Quieter Clothing', False, 45000],['Bigger Pockets', False, 135000],['Sleepier Dragons',False, 1025000],['More Black Dye',False, 10150150],['Fingerless Gloves',False, 100500500]]

mMU = []


clock = pygame.time.Clock()
tickrate = 60
bg = pygame.image.load("images/FogsEdgeSmall.jpg")
slime = pygame.image.load('images/beeg_slime.png')
goldSlime = pygame.image.load('images/goldslime.png')
font = pygame.font.Font('images/L_10646.ttf', 32)
logo = pygame.image.load("images/greenslime16.png")
pygame.display.set_icon(logo)
pygame.display.set_caption("Slime Clicker")
screen = pygame.display.set_mode((1024, 768))
#^ set up screen and window


bards = Bard()
fighters = Fighter()
druids = Druid()
rogues = Rogue()
mages = Archmage()
#^ set up objects to hold building data

#buildings: Bard, Fighter, Druid, Rogue, Archmage

goldSlimeFlag = False
goldSlimeTimer = 0
goldSlimeX = 0
goldSlimeY = 0
goldSlimeEffectTimer = 0
goldSlimeEffectActive = False


gameStart = True
    
def goldSlimeFunc():
    global goldSlimeFlag
    global goldSlimeTimer
    global goldSlimeX
    global goldSlimeY
    if not goldSlimeFlag:
            i = random.randint(1, 12000)
            if i == 1:
                goldSlimeFlag = True
                goldSlimeX = random.randint(64, 960)
                goldSlimeY = random.randint(64, 704)
    if goldSlimeFlag == True:
        if goldSlimeTimer < tickrate * 10:
            screen.blit(goldSlime, (goldSlimeX, goldSlimeY))
            goldSlimeTimer += 1
        elif goldSlimeTimer >= tickrate * 10:
            goldSlimeTimer = 0
            goldSlimeFlag = False
        
def goldSlimeClick():
    global gpTotal
    #flag = random.randint(1,2)
    #if flag == 1:
    gpTotal += (gpTotal * 0.5) + 20
    #elif flag ==2:
        #clickMultiplier = 7
        
  
def main():
    global gpTotal
    global highestGPT
    global goldSlimeFlag
    global goldSlimeTimer
    global goldSlimeX
    global goldSlimeY
    global gameStart
    while True:
        text = font.render(str(round(gpTotal)) + ' Gold Pieces | ' + str(bards.getProd() + fighters.getProd() + rogues.getProd() + mages.getProd()) + ' Gold Per Second' , True, (212,175,55))
        #this throws a library initialized error on close and i genuinely can't find out why, considering the library is initialized, but it doesnt have any problems while running
        
        textRect = text.get_rect()
        textRect.center = (512, 660)
        screen.blit(bg, (0,0))
        screen.blit(text, textRect)
        screen.blit(slime, (368, 256))
        goldSlimeFunc()
        pygame.display.update()
        
        #^draw background and slimes to click
        
        gpTotal += (bards.getProd() + fighters.getProd() + rogues.getProd() + mages.getProd())  / 60
        clock.tick(60)
        if gpTotal > highestGPT:
            highestGPT = gpTotal
        
        if gameStart == True:
            openInfo()
            gameStart = False
            
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONUP:
                x, y = pygame.mouse.get_pos()
                if x > 384 and x < 640 and y > 256 and y < 640 and event.button == 1:
                    slimeClick()
                if x > goldSlimeX and x < goldSlimeX + 128 and y > goldSlimeY and y < goldSlimeY + 128 and event.button == 1:
                    goldSlimeClick()
                    goldSlimeFlag = False
                    goldSlimeTimer = 0
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.display.quit()
                    pygame.quit()
                if event.key == K_s:
                    buildingMenu()
                if event.key == K_u:
                    upgradeMenu()
                if event.key == K_a:
                    openAchieve()
                if event.key == K_i:
                    openInfo()

def buildingMenu():
    global gpTotal
    bMenu = pygame_menu.Menu('Adventurers:', 900, 600, columns=2, rows=6, theme=pygame_menu.themes.THEME_DARK)
    populateBuildings(bMenu)
    running = True
    while running:
        clock.tick(60)
            # Draw the menu
        bMenu.draw(surface=screen)
            # Gather events by Menu
        bMenu.update(pygame.event.get())
            # Flip contents to screen
        pygame.display.flip()
        
        gpTotal += (bards.getProd() + fighters.getProd() + rogues.getProd() + mages.getProd())  / 60
            #track production while in menu
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    bMenu.disable()
                if event.key == K_s:
                    running = False
                    bMenu.disable()
                  
             #Menu disabled
        if not bMenu.is_enabled():
            return bMenu._current


def upgradeMenu():
    global gpTotal
    uMenu = pygame_menu.Menu('Upgrades:', 950, 700, theme=pygame_menu.themes.THEME_DARK)
    populateBardUpgrades(uMenu)
    running = True
    while running:
        clock.tick(60)
            # Draw the menu
        uMenu.draw(surface=screen)
            # Gather events by Menu
        uMenu.update(pygame.event.get())
            # Flip contents to screen
        pygame.display.flip()
        
        gpTotal += (bards.getProd() + fighters.getProd() + rogues.getProd() + mages.getProd())  / 60
            #track production while in menu
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    uMenu.disable()
                if event.key == K_u:
                    running = False
                    uMenu.disable()
                  
            # Menu disabled
        if not uMenu.is_enabled():
            return uMenu._current
    
def slimeClick():
    global gpTotal
    gpTotal += 1 * clickMultiplier + clickFlat
    
def openAchieve():
        global gpTotal
        aMenu = pygame_menu.Menu('Achievements:', 950, 700, theme=pygame_menu.themes.THEME_DARK)
        populateAchieves(aMenu)
        running = True
        while running:
            clock.tick(60)
            # Draw the menu
            aMenu.draw(surface=screen)
            # Gather events by Menu
            aMenu.update(pygame.event.get())
            # Flip contents to screen
            pygame.display.flip()
        
            gpTotal += (bards.getProd() + fighters.getProd() + rogues.getProd() + mages.getProd())  / 60
            #track production while in menu
            events = pygame.event.get()
            for event in events:
                if event.type == QUIT:
                    pygame.display.quit()
                    pygame.quit()
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                        aMenu.disable()
                    if event.key == K_a:
                        running = False
                        aMenu.disable()
                        
            if not aMenu.is_enabled():
                return aMenu._current
                    
def populateAchieves(menu):
    global highestGPT
    aGreen = (161, 224, 64)
    aRed = (200, 82, 82)
    a1 = menu.add.label('Kill a slime')
    if highestGPT >= 1:
        a1.set_background_color(aGreen)
    else:
        a1.set_background_color(aRed)
    a2 = menu.add.label('Thousaindaire: Have 1000 GP at once')
    if highestGPT >= 1000:
        a2.set_background_color(aGreen)
    else:
        a2.set_background_color(aRed)
    a3 = menu.add.label('Band: Own 10 Bards')
    if bards.quantity >= 10:
        a3.set_background_color(aGreen)
    else:
        a3.set_background_color(aRed)
    a4 = menu.add.label('Fight Club: Own 10 Fighters')
    if fighters.quantity >= 10:
        a4.set_background_color(aGreen)
    else:
        a4.set_background_color(aRed)
    a5 = menu.add.label('Friend of the Forest: Own 10 Druids')
    if druids.quantity >= 10:
        a5.set_background_color(aGreen)
    else:
        a5.set_background_color(aRed)
    a6 = menu.add.label('Criminal: Own 10 Rogues')
    if rogues.quantity >= 10:
        a6.set_background_color(aGreen)
    else:
        a6.set_background_color(aRed)
    a6 = menu.add.label('Headmaster: Own 10 Mages')
    if mages.quantity >= 10:
        a6.set_background_color(aGreen)
    else:
        a6.set_background_color(aRed)
    menu.add.button('Quit ', menu.disable)
                                    
    
    
def populateBuildings(menu):
    #bPic = menu.add.image()
    #fPic = menu.add.image()
    #dPic = menu.add.image()
    #rPic = menu.add.image()
    #mPic = menu.add.image()
    b1 = menu.add.button('Bard(' +str(bards.quantity) + '):     ' + str(bards.price()), bards.purchase)
    b1.add_draw_callback(bard_update)
    b1.force_menu_surface_update()
    f1 = menu.add.button('Fighter(' +str(fighters.quantity) + '):     ' + str(fighters.price()), fighters.purchase)
    f1.add_draw_callback(fighter_update)
    f1.force_menu_surface_update()
    d1 = menu.add.button('Druid(' +str(druids.quantity) + '):    ' + str(druids.price()), druids.purchase)
    d1.add_draw_callback(druid_update)
    d1.force_menu_surface_update()
    r1 = menu.add.button('Rogue(' +str(rogues.quantity) + '):    ' + str(rogues.price()), rogues.purchase)
    r1.add_draw_callback(rogue_update)
    r1.force_menu_surface_update()
    m1 = menu.add.button('Mage(' +str(mages.quantity) + '):     ' + str(mages.price()), mages.purchase)
    m1.add_draw_callback(mage_update)
    m1.force_menu_surface_update()
    q1 = menu.add.button('Quit ', menu.disable)
    #^Buttons run adventurer purchase methods on click and update their own titles + force redraws on load(it's kinda janky)

def bard_update(button, menu):
    button.set_title('Bard(' +str(bards.quantity) + '):     ' + str(bards.price()))
def fighter_update(button, menu):
    button.set_title('Fighter(' +str(fighters.quantity) + '):     ' + str(fighters.price()))
def rogue_update(button, menu):
    button.set_title('Rogue(' +str(rogues.quantity) + '):    ' + str(rogues.price()))
def druid_update(button, menu):
    button.set_title('Druid(' +str(druids.quantity) + '):    ' + str(druids.price()))
def mage_update(button, menu):
    button.set_title('Mage(' +str(mages.quantity) + '):     ' + str(mages.price()))
#^buttons update their titles on load 
    
def populateBardUpgrades(menu):
    global bardUpgrade
    l1 = menu.add.label('Bard Upgrades')
    clickFrame = menu.add.frame_h(800, 128)
    if not bardUpgrade[0]:
        menu.add.button('Bard College(2x): 500', bardPurchase, 500, 0, menu)
    if not bardUpgrade[1]:
        menu.add.button('Louder Lutes(2x): 5,000', bardPurchase, 5000, 1, menu)
    if not bardUpgrade[2]:
        menu.add.button('Snappier Strings(2x): 50,000', bardPurchase, 50000, 2, menu)
    if not bardUpgrade[3]:
        menu.add.button('Portlier Patrons(2x): 500,000', bardPurchase, 500000, 3, menu)
    if not bardUpgrade[4]:
        menu.add.button('Sheetier Sheet Music(2x): 5,000,000', bardPurchase, 5000000, 4, menu)
    q1 = menu.add.button('Quit ', menu.disable)
    
def bardPurchase(price, index, menu):
    global bardUpgrade
    global gpTotal
    if not bardUpgrade[index] and gpTotal >= price:
        gpTotal -= price
        bards.upgrade(2)
    bardUpgrade[index] = True

def openInfo():
    global gpTotal
    iMenu = pygame_menu.Menu('Info:', 950, 700, theme=pygame_menu.themes.THEME_DARK)
    iMenu.add.label('I = Open Info Screen')
    iMenu.add.label('A = Open Achievements Screen')
    iMenu.add.label('S = Open Adventurer Store')
    iMenu.add.label('U = Open Upgrade Store')
    iMenu.add.button('Close', iMenu.disable)
    running = True
    while running:
        clock.tick(60)
        # Draw the menu
        iMenu.draw(surface=screen)
        # Gather events by Menu
        iMenu.update(pygame.event.get())
        # Flip contents to screen
        pygame.display.flip()
        
        gpTotal += (bards.getProd() + fighters.getProd() + rogues.getProd() + mages.getProd())  / 60
        #track production while in menu
        events = pygame.event.get()
        for event in events:
            if event.type == QUIT:
                pygame.display.quit()
                pygame.quit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    running = False
                    iMenu.disable()
                if event.key == K_a:
                    running = False
                    iMenu.disable()
                        
        if not iMenu.is_enabled():
            return iMenu._current
        
   
main()
