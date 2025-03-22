class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        r, i, s = recipes, ingredients, set(supplies) # shorthand it
        ret = set() # return
        while True:
            sz = len(ret) # tracks if any new recipes were made, potentially unlocking more
            for x in range(len(r)): # for all the recipes
                if set(i[x])&s == set(i[x]): # see if its possible to make it
                    ret.add(r[x]) # add it regardless of whether or not we alr can make it
                    s.add(r[x]) # recipes can be subingredients for other recipes
            if sz == len(ret): # if no new recipes made, no further unlocks
                break
        return list(ret)
