class Solution(object):
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        
        stack = []

        for a in asteroids:
            while stack and a < 0 < stack[-1]:
                
                if stack[-1] < -a:
                    stack.pop()
                    continue
                elif stack[-1] == -a:
                    stack.pop()
                    break
                else:
                    break
            else:
                stack.append(a)

        return stack