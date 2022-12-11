# Lab 3 Nim
In this repo is present an implementation to solve the Computational Intellegence course lab 3 from Politecnico of Turin, I worked with [Luca Marcellino (s292950)](https://github.com/Lucamarcellino/Computational_Intelligence).

The main taks is impemented a code tha can play [Nim](https://it.wikipedia.org/wiki/Nim). This repo is diveded in different sub-folder in which you can find different kind of applications.
The lab was divided in different sub-task:

- Task3.1: An agent using fixed rules based on nim-sum (i.e., an expert system) (Folder lab3)
- Task3.2: An agent using evolved rules (Folder lab3)
- Task3.3: An agent using minmax (Folder MinMax)
- Task3.4: An agent using reinforcement learning (Folder Reinforcement learning)

## Folder lab3

In this folder are present the first two taks. 

### Nim-Sum

The nim-sum is an optimal solution in which we have to divide the number of stick in each line in multiple of 1,2,4. Example:

Row1 = 1= 1 x 1 = 1	=&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;1

Row2 = 3= 1 x 2 + 1 x 1	=&emsp;&emsp;&emsp;&emsp;&emsp;2&emsp;1

Row3 = 5= 1 x 4 + 1 x 1	= &emsp;&emsp;&emsp;4&emsp;&emsp;&emsp;1
 
Row4 = 7= 1 x 4 + 1 x 2 + 1 x 1	= 4&emsp;2&emsp;1

The objective is try to elimnate all the number in the same column, in this way we increase our winning probability.

### Evolved rules

For this kind of implementation we decide to pick always random from the field until we have 3 rows. At that point we leave also 1 stick at the longest raw until is possible.

## Folder MinMax

To write this code we used this [repo](https://github.com/kevinyang372/Nim). In this repo is present an implementation of the MinMax algorithm used to solve/play Nim. We solve the fact that the stopping condition in the kevin's repo was that: who take the last lose. In this implementation you can play against the computer 

## Folder Reinforcement Learing

To solve this implementation we based our code on this [repo](https://github.com/abelmariam/nimPy). In this folder is present a Q_learning code to teach, to the computer, how to play Nim. To train the computer we decided to make 100_000 games against an optiaml_player. Then you can choose against the computer can play (except the human).


