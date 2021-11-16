
# EvillNode
CONTENTS OF THIS FILE
---------------------

 * Introduction
 * Terminology
 * Simulation
 * Techologes
 * Libraries
 * Authors
 * License
 
## Introdoction

This is a simulation of the network running,where every epoch,new set of nodes are selected in the active pool.

## Why do we need this simulation?

* We must proof which configurations is the most secure one to protect active pool from evil nodes.

## Terminology
## What is Node pool?

* It can be all nodes in the system.Amount of these mixed nodes(evil and good) potentially millions in the pool.

## What is Active Pool?

* Configured amount of active nodes at one time.

* This parameter can be **configured** in the network rules.

## What is GoodNode?

* The node that behaves by the rules in the system

## What  is EvilNode?
* The node that might break the rules in the system

## Simulation
How is the simulation going ?

## Initial configurable state of simulation: 
* Active Node Pool size (from 10 to 1000)
* Evil Node Amount (300000)
* Good Node Amount (700000)

This simulation run N epochs and choose new random nodes in the active pool.
When the majority in the pool is evil, we print the event with details of configuration that ran.

Notice,that each simulation configuration should run in N iterations, simulating 100 years of work, assuming one epoch takes 30 seconds.

We used method Monte-Karlo to create a random number generator and are used to model processes with uncertainty.
It is effective for calculating business risks and predicting adverse events,such as cost overruns or behind schedule.

Also,we use

## Techologes:
* Let's write down the languages we used, the libraries and its versions:
## Language:
* Python 3.9
## Libraries:
* import time 
---  pip3 install time
* import matplotlib.pyplot as plt
--- pip3 install matplotlib
* import numpy as np
--- pip3 install numpy
* import random
--- pip3 install random
* import pylab
--- pip3 install pylab
* import numpy.random as rand
* from numpy.random import choice


## Authors
Kateryna Leontieva - work on Evil model simulation 


## License
This project is licensed under the MIT License - see the LICENSE.md file for details

