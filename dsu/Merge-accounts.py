class UnionFind:
    def __init__(self):
        self.el_dict = {}
    
    def find(self, x):
        parent = x
        if x in self.el_dict:
            parent = self.el_dict[x]
        
        if x != parent:
            parent = self.find(parent)
            self.el_dict[x] = parent
        
        return parent
    
    def merge(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        self.el_dict[root_x] = root_y


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        dsu = UnionFind()
        for i in range(len(accounts)):
            current_account = accounts[i]
            username = current_account[0]
            primary_mail = current_account[1]
            primary_key = (" ").join([username, primary_mail])
            j = 2
            while j < len(current_account):
                mail = current_account[j]
                key = (" ").join([username, mail])
                dsu.merge(primary_key, key)
                j += 1
            
        result_as_map = {}
        for i in range(len(accounts)):
            current_account = accounts[i]
            username = current_account[0]
            primary_mail = current_account[1]
            primary_key = (" ").join([username, primary_mail])
            root = dsu.find(primary_key)
            if root not in result_as_map:
                result_as_map[root] = []
            j = 1
            while j < len(current_account):
                if current_account[j] not in result_as_map[root]:
                    result_as_map[root].append(current_account[j])
                j += 1
        
        result = []
        for key, val in result_as_map.items():
            val.sort()
            username = key.split(" ")[0]
            result.append([username] + val)
        
        return result