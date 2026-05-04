class Solution:
    def minimumBoxes(self, apple: List[int], capacity: List[int]) -> int:
        capacity.sort(reverse = True)
        app = sum(apple)
        count = 0
        for i in capacity:
            count += 1
            app -= i
            if app < 1:
                return count
            
        