class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        asteroids.sort()
        mx = max(asteroids)
        for i in asteroids:
            if i > mass:
                return False
            if mx <= mass:
                return True
            mass += i
        return True