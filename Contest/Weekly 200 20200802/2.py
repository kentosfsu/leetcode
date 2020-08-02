"""
5476. Find the Winner of an Array Game
Given an integer array arr of distinct integers and an integer k.

A game will be played between the first two elements of the array (i.e. arr[0] and arr[1]). In each round of the game, we compare arr[0] with arr[1], the larger integer wins and remains at position 0 and the smaller integer moves to the end of the array. The game ends when an integer wins k consecutive rounds.

Return the integer which will win the game.

It is guaranteed that there will be a winner of the game.
"""
class Solution:
    def getWinner(self, arr: List[int], k: int) -> int:
        if k > len(arr) - 2:
            return max(arr)
        win_counter = 0
        while(win_counter < k):
            if arr[0] > arr[1]:
                loser = arr[1]
                arr.remove(loser)
                arr.append(loser)
                win_counter += 1
            else:
                loser = arr[0]
                arr.remove(loser)
                arr.append(loser)
                win_counter = 1
        return arr[0]