"""
File Name: main.py
Aurthor: Justin Kringler
Last Updated: 1/24/2025

Description: Script that tests SemanticNetsAgent.py for mini project 1 in CS7637.

Problem: You are a shepherd tasked with getting sheep and wolves across a river for some reason. 
         If the wolves ever outnumber the sheep on either side of the river, the wolves will overpower
         and eat the sheep. You have a boat, which can only take one or two animals in it at a time,
         and must have at least one animal in it because you’ll get lonely (and because the problem
         is trivial otherwise). How do you move all the animals from one side of the river to the other?

Notes: The test functions uses the solve function from SemanticNetsAgent.py

"""


##### Loading Modules -----

from SemanticNetsAgent import SemanticNetsAgent


##### Test Function -----

def test():

    # Used to Test Agent
    test_agent = SemanticNetsAgent()

    print(test_agent.solve(3, 3))


if __name__ == "__main__":
    test()