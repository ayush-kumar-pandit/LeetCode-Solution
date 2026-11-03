class Solution:
    def findAllRecipes(self, recipes: list[str], ingredients: list[list[str]], supplies: list[str]) -> list[str]:
        res = []
        menu = {}

        for i in range(len(recipes)):
            menu[recipes[i]] = ingredients[i]

        changed = True

        while changed:
            changed = False

            for k, v in menu.items():
                if k in supplies:
                    continue

                for ch in v:
                    if ch not in supplies:
                        break
                else:
                    res.append(k)
                    supplies.append(k)
                    changed = True

        return res