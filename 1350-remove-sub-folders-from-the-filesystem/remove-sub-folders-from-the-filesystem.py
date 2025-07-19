class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        # we have lists of folders 
        # if folder[i] is inside folder[j] then j is subfolder of a
        # Input: folder = ["/a","/a/b","/c/d","/c/d/e","/c/f"]
        # in above eg. /a/b is subfolder of /a /c/d/e is of /c/d 

        # lexiographical sorting if parent folder is in our set then we dont consider

        folder.sort()
        res = []

        i = 0
        # for f in folder:
        for f in folder:
            if not res:
                res.append(f)
            else:
                prev = res[-1]
                if len(f) > len(prev) and f.startswith(prev) and f[len(prev)] == "/":
                    continue
                else:
                    res.append(f)

        return res