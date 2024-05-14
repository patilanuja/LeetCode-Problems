# same account same name same email
# input : list of lists 
# output list of lists

class UnionFind:
    def __init__(self,n):
        self.parent = [i for i in range(n)] 
        self.rank = [1]*n

    def find(self, n):
        while n != self.parent[n]:
            self.parent[n] = self.parent[self.parent[n]]
            n = self.parent[n]
        return n

    def union(self, n1, n2):
        p1, p2 = self.find(n1), self.find(n2)

        if p1 == p2:
            return False
        
        if self.rank[p2] > self.rank[p1]:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]

        else:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]

        return True

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        
        uf = UnionFind(len(accounts))

        # email -> Acc index 
        # unite the accounts if emails are same
        emailToAcc = {}

        for idx, acc in enumerate(accounts):
            for email in acc[1:]:
                if email in emailToAcc:
                    uf.union(idx, emailToAcc[email])
                else:
                    emailToAcc[email] = idx

        # Group the eamils # find the leader
        # idx -> all related emails
        emailGroup = defaultdict(list)

        for email, idx in emailToAcc.items():
            leader = uf.find(idx)
            emailGroup[leader].append(email)

        res = []
        for idx, emails in emailGroup.items():
            name = accounts[idx][0]
            res.append([name] + sorted(emailGroup[idx]))
        return res

        

        