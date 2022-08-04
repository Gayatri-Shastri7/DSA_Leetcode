# Refered the below video for the logic
# https://www.youtube.com/watch?v=_xIBOUWEq1c&ab_channel=AlgorithmsMadeEasy, https://leetcode.com/problems/mirror-reflection/discuss/2376355/Python3-oror-4-lines-geometry-w-explanation-oror-TM%3A-9281 

class Solution:
    def mirrorReflection(self, p: int, q: int) -> int:

        L = lcm(p,q)

        if (L//q)%2 == 0:
            return 2

        return (L//p)%2