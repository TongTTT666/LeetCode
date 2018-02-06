class Solution:
    def simplifyPath(self, path):
        places = [p for p in path.split("/") if p!="." and p!=""]
        print(places)
        stack = []
        for p in places:
            if p == "..":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + "/".join(stack)

