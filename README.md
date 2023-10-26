# AI_project2-genetic-algorithm
It's second project of Artificial intelligence course in Amirkabir University Of Technology.
Genetic algorithm in AI has been implemented in this repository with showing different states in a simple game.
The game is basically likes "Supermario". Genetic algorithm has 4 steps: initial population, fitness function, crossover, mutation. each of these steps has implemented.


# Genetic Algorithm
Artificial Intelligence Course 2nd Project: Implementing genetic algorithm in order to solve Super Mario game.
<br>
In this group project we ([pouyanhessabi](https://github.com/pouyanhessabi) and [omidmahyar](https://github.com/omidmahyar)) implemented `genetic algorithm` to solve Super-Mario game.<br>
Mario can jump, go straight or dodge. Mario must jump over Goomba and must dodge when it reaches Lakito. If Mario jumps 2 step before Goomba it can kill Goomba and then it gets more points.
If Mario jumps when it reaches at the end of the board it gets more points (but it's adjustable). If Mario jumps on a Goomba it gets additional points.
<br>

We implemented different types of `crossover`:
* crossover from one point which is chosen and randomly
* crossover from one point which you can specify (by index)
* crossover from two points which are chosen randomly
* crossover from two points which you can specify (by index)

and `selection`:
* weighted random
* best selection 

that you can choose from. Also you can the number of `initial population` and `mutation probability`.
<br>


Check full description (in persian): [here](https://github.com/pouyanhessabi/AI-project2-genetic-algorithm/blob/main/AI_P2.pdf)
<br>
Project report (in persian): [here](https://github.com/Amirhossein-Rajabpour/Genetic-Algorithm/blob/main/AI_P2_Report.pdf)
<br>
Check our other AI Course projects:
* [Project 1: Searching Algorithms (IDS, BBFS, A*)](https://github.com/pouyanhessabi/AI-project1-searching-algorithms)
* [Project 4: NLP Comment Filtering](https://github.com/pouyanhessabi/AI-project4-NLP)
