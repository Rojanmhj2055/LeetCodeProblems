#Problem Statement:There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].
#You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th 
# station. You begin the journey with an empty tank at one of the gas stations.Given two integer arrays gas and cost, 
# return the starting gas station's index if you can travel around the circuit once in the clockwise direction
# , otherwise return -1. If there exists a solution, it is guaranteed to be unique


#url: https://leetcode.com/problems/gas-station/
gas =[1,2,3,4,5]
cost =[3,4,5,1,2]

def canCompleteCircuit(gas,cost)->int:
        if sum(gas)<sum(cost):
            return -1
        
        total = 0
        start = 0
        for i in range(len(gas)):
           total+= gas[i]-cost[i]
           if total<0:
               total = 0
               start = i+1
        
        return start