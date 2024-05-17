735. Asteroid Collision
class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        i = 0
        while i < len(asteroids):
            if stack and stack[-1] > 0 and asteroids[i] < 0:
                # collision -> yes
                if abs(stack[-1]) > abs(asteroids[i]):
                    i = i + 1
                elif abs(stack[-1]) < abs(asteroids[i]):
                    stack.pop()

                    continue
                else:#if both asteroids are equal,
                    stack.pop()
                    i = i + 1
            else:
                stack.append(asteroids[i])
                i = i + 1
        print(stack)

        return stack
