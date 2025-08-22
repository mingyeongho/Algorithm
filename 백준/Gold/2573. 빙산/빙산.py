import sys
input=sys.stdin.readline
from collections import deque

def bfs(s_x,s_y):
    dx=[1,0,-1,0]
    dy=[0,-1,0,1]
    q=deque()
    q.append((s_x,s_y))
    visited[s_x][s_y]=1
    while q:
        x,y=q.popleft()
        for i in range(4):
            xx,yy=x+dx[i],y+dy[i]
            if 0<=xx<n and 0<=yy<m:
                if mapp[xx][yy]==0:
                    lake[x][y]+=1
                elif mapp[xx][yy]>0 and visited[xx][yy]==0:
                    visited[xx][yy]=1
                    q.append((xx,yy))
              
def remove():
    new_ice=[]
    for i,j in ice:
        mapp[i][j]=max(0,mapp[i][j]-lake[i][j])
        if mapp[i][j]>0:
            new_ice.append((i,j))
    return new_ice

#n:행,m:열
n,m=map(int,input().split())
mapp=[list(map(int,input().split())) for _ in range(n)]
ice=[]
for i in range(n):
    for j in range(m):
        if mapp[i][j]>0:
            ice.append((i,j))
year=0
while True:
    visited=[[0 for _ in range(m)] for _ in range(n)]
    lake=[[0 for _ in range(m)] for _ in range(n)]#주변 호수 개수
    num=0
    for x,y in ice:
        if visited[x][y]==0:
            bfs(x,y)
            num+=1
        
    if num>1:#종료
        print(year)
        break
    ice=remove()
    year+=1
        
    if len(ice)==0:
        print(0)
        break