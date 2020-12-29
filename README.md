This project is for assessment in "An Introduction to Interactive Programming in Python (Part 2)" course at Rice university.  
https://www.coursera.org/learn/interactive-python-2  

**MiniProject Spaceship**  

For this mini-project, you will implement a working spaceship plus add a single asteroid and a single missile. We have provided art for your
 game so its look and feel is that of a more modern game.The program template includes all
necessary image and audio files. Unfortunately, no audio format is supported by all major browsers so we have decided to provided sounds in
the mp3 format which is supported by Chrome (but not by Firefox on some systems).  

- 1 pt - The program draws the ship as an image.
- 1 pt - The ship flies in a straight line when not under thrust.
- 1 pt - The ship rotates at a constant angular velocity in a counter clockwise direction when the left arrow key is held down.
- 1 pt - The ship rotates at a constant angular velocity in the clockwise direction when the right arrow key is held down.
- 1 pt - The ship's orientation is independent of its velocity.
- 1 pt - The program draws the ship with thrusters on when the up arrow is held down.
- 1 pt - The program plays the thrust sound only when the up arrow key is held down.
- 1 pt - The ship accelerates in its forward direction when the thrust key is held down.
- 1 pt - The ship's position wraps to the other side of the screen when it crosses the edge of the screen.
- 1 pt - The ship's velocity slows to zero while the thrust is not being applied.
- 1 pt - The program draws a rock as an image.
- 1 pt - The rock travels in a straight line at a constant velocity.
- 1 pt - The rock is respawned once every second by a timer.
- 1 pt - The rock has a random spawn position, spin direction and velocity.
- 1 pt - The program spawns a missile when the space bar is pressed.
- 1 pt - The missile spawns at the tip of the ship's cannon.
- 1 pt - The missile's velocity is the sum of the ship's velocity and a multiple of its forward vector.
- 1 pt - The program plays the missile firing sound when the missile is spawned.
- 1 pt - The program draws appropriate text for lives on the upper left portion of the canvas.
- 1 pt - The program draws appropriate text for score on the upper right portion of the canvas.


**MiniProject RiceRock**  

We will complete the implementation of RiceRocks, an updated version of Asteroids,  that we began with the Spaceship.  
At the end of this project, your game will have multiple rocks and multiple missiles.  You will lose a life if your ship collides with a roc
k and you will score points if your missile collides with a rock. You will keep track of the score and lives remaining and end the game at t
he proper time.  You may optionally add animated explosions when there is a collision.  

- 1 pt - The program spawns multiple rocks.
- 1 pt - The program correctly determines whether the ship collides with a rock.
- 1 pt - The program removes a rock when the ship collides with a rock.
- 1 pt - The number of lives decreases by one when the ship collides with a rock.
- 1 pt - The program removes a rock when the ship collides with a rock.
- 1 pt - The number of lives decreases by one when the ship collides with a rock.
- 1 pt - The program spawns multiple missiles.
- 1 pt - The program plays the firing sound when each missile is spawned.
- 1 pt - The program removes a missile that does not collide with a rock after some fixed time period.
- 1 pt - The program correctly determines whether a missile and a rock collide.
- 1 pt - The program removes missiles and rocks that collide.
- 1 pt - The score is updated appropriately after missile/rock collisions.
- 1 pt - When the lives go to zero, the splash screen reappears and all rocks are removed.
- 1 pt - When the splash screen is clicked, the lives are reset to 3, score is reset to zero and the background music restarts.
- 1 pt - The game spawns rocks only when the splash screen is not visible and a game is in progress.


