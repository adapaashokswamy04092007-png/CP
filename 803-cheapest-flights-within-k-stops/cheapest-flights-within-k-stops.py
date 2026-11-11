class Solution:
    from collections import deque
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        INT=float('inf')
        adj={}
        for i in range(n):
            adj[i]=[]
        for flight in flights:
            adj[flight[0]].append((flight[1],flight[2]))
        dist=[INT]*n
        dist[src]=0
        q=deque([(src,0)])
        flights_taken=0
        while q and flights_taken <=k:
            for _ in range(len(q)):
                curr=q.popleft()
                for v,d in adj[curr[0]]:
                    if dist[v]>curr[1]+d:
                        dist[v]=curr[1]+d
                        q.append((v,dist[v]))
            flights_taken+=1
        if dist[dst]!=INT:
            return dist[dst]
        else : return -1