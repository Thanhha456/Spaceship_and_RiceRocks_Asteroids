# program template for Spaceship
import simpleguitk as simplegui
import math
import random

# globals for user interface
WIDTH = 800
HEIGHT = 600
score = 0
lives = 3
time = 0
started = False

class ImageInfo:
    def __init__(self, center, size, radius=0, lifespan=None, animated=False):
        self.center = center
        self.size = size
        self.radius = radius
        if lifespan:
            self.lifespan = lifespan
        else:
            self.lifespan = float('inf')
        self.animated = animated

    def get_center(self):
        return self.center

    def get_size(self):
        return self.size

    def get_radius(self):
        return self.radius

    def get_lifespan(self):
        return self.lifespan

    def get_animated(self):
        return self.animated


# art assets created by Kim Lathrop, may be freely re-used in non-commercial projects, please credit Kim

# debris images - debris1_brown.png, debris2_brown.png, debris3_brown.png, debris4_brown.png
#                 debris1_blue.png, debris2_blue.png, debris3_blue.png, debris4_blue.png, debris_blend.png
debris_info = ImageInfo([320, 240], [640, 480])
debris_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/debris2_blue.png")

# nebula images - nebula_brown.png, nebula_blue.png
nebula_info = ImageInfo([400, 300], [800, 600])
nebula_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/nebula_blue.f2014.png")

# splash image
splash_info = ImageInfo([200, 150], [400, 300])
splash_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/splash.png")

# ship image
ship_info = ImageInfo([45, 45], [90, 90], 35)
ship_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/double_ship.png")

# missile image - shot1.png, shot2.png, shot3.png
missile_info = ImageInfo([5, 5], [10, 10], 3, 50)
missile_image = simplegui.load_image("http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/shot2.png")

# asteroid images - asteroid_blue.png, asteroid_brown.png, asteroid_blend.png
asteroid_info = ImageInfo([45, 45], [90, 90], 40)
asteroid_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/asteroid_blue.png")

# animated explosion - explosion_orange.png, explosion_blue.png, explosion_blue2.png, explosion_alpha.png
explosion_info = ImageInfo([64, 64], [128, 128], 17, 24, True)
explosion_image = simplegui.load_image(
    "http://commondatastorage.googleapis.com/codeskulptor-assets/lathrop/explosion_alpha.png")


# helper functions to handle transformations
def angle_to_vector(ang):
    return [math.cos(ang), math.sin(ang)]


def dist(p, q):
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)


# Ship class
class Ship:
    def __init__(self, pos, vel, angle, image, info):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.thrust = False
        self.angle = angle
        self.angle_vel = 0
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()

    def get_radius(self):
        return self.radius

    def get_position(self):
        return self.pos

    def draw(self, canvas):
        canvas.draw_image(ship_image, ship_info.get_center(), ship_info.get_size(), self.pos, self.image_size, self.angle)
        if self.thrust:
            canvas.draw_image(ship_image, [ship_info.get_center()[0] + ship_info.get_size()[0], ship_info.get_center()[1]],
                              ship_info.get_size(), self.pos, self.image_size, self.angle)

    def increase_ang_vel(self):
        self.angle_vel += 0.05
        return self.angle_vel

    def decrease_ang_vel(self):
        self.angle_vel -= .05
        return self.angle_vel

    def shoot(self):
        forward = angle_to_vector(self.angle)
        missile_pos = [self.pos[0] + self.radius * forward[0], self.pos[1] + self.radius * forward[1]]
        missile_vel = [self.vel[0] + 10 * forward[0], self.vel[1] + 10 * forward[1]]
        missile = Sprite(missile_pos, missile_vel, self.angle, 0, missile_image, missile_info)
        missile_group.add(missile)

    def update(self):
        self.angle += self.angle_vel
        if self.thrust:
            self.vel[0] += angle_to_vector(self.angle)[0] * .1
            self.vel[1] += angle_to_vector(self.angle)[1] * .1
        self.vel[0] *= .99
        self.vel[1] *= .99
        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT

# Sprite class
class Sprite:
    def __init__(self, pos, vel, ang, ang_vel, image, info, sound=None):
        self.pos = [pos[0], pos[1]]
        self.vel = [vel[0], vel[1]]
        self.angle = ang
        self.angle_vel = ang_vel
        self.image = image
        self.image_center = info.get_center()
        self.image_size = info.get_size()
        self.radius = info.get_radius()
        self.lifespan = info.get_lifespan()
        self.animated = info.get_animated()
        self.age = 0
        if sound:
            sound.rewind()
            sound.play()

    def get_radius(self):
        return self.radius

    def get_position(self):
        return self.pos

    def draw(self, canvas):
        if self.animated:
            image_tile = (self.age % 24) // 1
            self.image_center = [self.image_center[0] + image_tile * self.image_size[0], self.image_center[1]]

        canvas.draw_image(self.image, self.image_center, self.image_size, self.pos, self.image_size, self.angle)

    def update(self):
        #update the position
        self.angle += self.angle_vel

        self.pos[0] = (self.pos[0] + self.vel[0]) % WIDTH
        self.pos[1] = (self.pos[1] + self.vel[1]) % HEIGHT
        #update the age and lifespan
        self.age += 1
        if self.age <= self.lifespan:
            return False
        else:
            self.age = 0
            return True

    def collied(self, other):
        """
        take an other_object as an argument and return True if there is a collision or False otherwise.
        """
        if dist(self.get_position(), other.get_position()) <= self.get_radius() + other.get_radius():
            return True
        else:
            return False

def keydown(key):
    if key == simplegui.KEY_MAP["left"]:
        my_ship.increase_ang_vel()
    elif key == simplegui.KEY_MAP["right"]:
        my_ship.decrease_ang_vel()
    elif key == simplegui.KEY_MAP["up"]:
        my_ship.thrust = True
    elif key == simplegui.KEY_MAP["space"]:
        my_ship.shoot()

def keyup(key):

    if key == simplegui.KEY_MAP["left"]:
        my_ship.decrease_ang_vel()
    elif key == simplegui.KEY_MAP["right"]:
        my_ship.increase_ang_vel()
    elif key == simplegui.KEY_MAP["up"]:
        my_ship.thrust = False

def draw(canvas):
    global time, lives, score, started, rock_group, missile_group

    # animiate background
    time += 1
    wtime = (time / 4) % WIDTH
    center = debris_info.get_center()
    size = debris_info.get_size()
    canvas.draw_image(nebula_image, nebula_info.get_center(), nebula_info.get_size(), [WIDTH / 2, HEIGHT / 2],
                      [WIDTH, HEIGHT])
    canvas.draw_image(debris_image, center, size, (wtime - WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_image(debris_image, center, size, (wtime + WIDTH / 2, HEIGHT / 2), (WIDTH, HEIGHT))
    canvas.draw_text("Lives  %s" % lives, (50, 50), 20, "White")
    canvas.draw_text("Score  %s" % score, (650, 50), 20, "White")

    #start
    if not started:
        splash_center = [WIDTH / 2, HEIGHT / 2]
        canvas.draw_image(splash_image, splash_info.get_center(), splash_info.get_size(), splash_center, splash_info.get_size())
    else:
        # draw ship and sprites
        my_ship.draw(canvas)
    # to detect missile/rock collisions.
    score += group_group_collide(rock_group, missile_group)
    # update ship and sprites
    process_sprite_group(rock_group, canvas)
    process_sprite_group(missile_group, canvas)
    process_sprite_group(explosion_group, canvas)
    my_ship.update()
    #removes a rock when the ship collides with a rock.
    rock_group_copy = rock_group.copy()
    for rock in rock_group_copy:
        if rock.collied(my_ship):
            rock_group.remove(rock)
            my_ship.pos = [WIDTH / 2, HEIGHT / 2]
            my_ship.angle = 0
            lives -= 1
    if lives <= 0 or len(rock_group) == 0:
        started = False
        lives = 0
        rock_group = set()

def group_collile(other_object, group):
    """
    take a set group and a sprite other_object and check for collisions between other_object and elements of the group.
    If there is a collision, the colliding object should be removed from the group.
    if there is a collision, create a new explosion (an instance of the Sprite class)and add it to the explosion_group.
    Make sure that each explosion plays the explosion sound.

    """
    global explosion_group
    copy_group = group.copy()
    for sprite in copy_group:
        if other_object.collied(sprite):
            explosion_group.add(Sprite(sprite.get_position(), [0, 0], 0, 0, explosion_image, explosion_info))
            group.remove(sprite)
            return True
        else:
            return False

def group_group_collide(group, other_group):
    """
    """
    group_copy = group.copy()
    removing_list =[]
    for ele in group_copy:
        if group_collile(ele, other_group):
            removing_list.append(ele)
    for ele_x in removing_list:
        group.discard(ele_x)
    return len(removing_list)

def process_sprite_group(sprite_group, canvas):
    """
    This function should take a set and a canvas and call the update and draw methods for each sprite in the group.
    Call the process_sprite_group function on rock_group in the draw handler.
    """
    sprite_group_copy = sprite_group.copy()
    for spr in sprite_group_copy:
        spr.draw(canvas)
        #remove the sptrite after a certain time
        if spr.update():
            sprite_group.remove(spr)

# timer handler that spawns rocks
def rock_spawner():
    """
    Modify your rock spawner to limit the total number of rocks in the game at any one time. We suggest you limit it to 12.
    With too many rocks the game becomes less fun and the animation slows down significantly.
    """
    global rock_group, my_ship
    if started == True:
        while len(rock_group) <= 12:
            pos = [random.randrange(WIDTH), random.randrange(HEIGHT)]
            vel = [random.uniform(-3, 3), random.uniform(-1, 1)]
            angle = random.uniform(-3, 3)
            angle_vel = random.uniform(-.3, .3)
            #rocks spawn from distance beyon 100 px to the ship
            if dist(my_ship.get_position(), pos) >= 100:
                rock = Sprite(pos, vel, angle, angle_vel, asteroid_image, asteroid_info)
                rock_group.add(rock)

def click(pos):
    """
    click any where on the splash to start the program
    """
    global started, lives, score, rock_group, my_ship

    if (WIDTH / 2 - splash_info.get_size()[0] / 2) <= pos[0] <= (WIDTH / 2 + splash_info.get_size()[0] / 2):
        if (HEIGHT / 2 - splash_info.get_size()[1] / 2) <= pos[1] <= (HEIGHT / 2 + splash_info.get_size()[0] / 2):
            started = True
            rock_group = set()
            rock_spawner()
            my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
            lives = 3
            score = 0
            # soundtrack.rewind()
            # soundtrack.play()

# initialize frame
frame = simplegui.create_frame("Asteroids", WIDTH, HEIGHT)
frame.set_keydown_handler(keydown)
frame.set_keyup_handler(keyup)
frame.set_mouseclick_handler(click)

# initialize ship and two sprites
my_ship = Ship([WIDTH / 2, HEIGHT / 2], [0, 0], 0, ship_image, ship_info)
a_missile = Sprite([2 * WIDTH / 3, 2 * HEIGHT / 3], [-1, 1], 0, 0, missile_image, missile_info)
# a_rock = Sprite(pos, vel, angle, angle_vel, asteroid_image, asteroid_info)

rock_group = set()
missile_group = set()
explosion_group = set()

# register handlers
frame.set_draw_handler(draw)

timer = simplegui.create_timer(1000.0, rock_spawner) #spawns a rock every second

# get things rolling
timer.start()
frame.start()
