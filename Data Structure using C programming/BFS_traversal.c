#include<stdio.h>
int A[20][20],queue[20],visited[20],n,i,j,front=0,rear=-1;
void bfs(int);
int main()
{
   int v;
   printf("Enter the no. of Vertices:\n");
   scanf("%d",&n);
   for(i=0;i<n;i++)
   {
       queue[i]=0;
       visited[i]=0;
   }
   printf("Enter the Adjacency Matrix of Graph:\n");
   for(i=0;i<n;i++)
   {
     for(j=0;j<n;j++)
     {
        scanf("%d",&A[i][j]);
     }
   }
   
   printf("\nEnter the Starting Vertex:\n");
   scanf("%d",&v);
   bfs(v);
   printf("Traversed nodes are:\n");
   for(i=0;i<n;i++)
   {
      if(visited[i])
       printf("\nThe Node %d is reachable",i);
      else
       printf("\nThe Node %d is not reachable",i); 
   }
   return 0;
}

void bfs(int v)
{
   for(i=0;i<n;i++)
   {
      if(A[v][i] && !visited[i])
          queue[++rear]=i;	
   }
   if(front<=rear)
   {
      visited[queue[front]]=1;
      bfs(queue[++front]);   //recursively calling bfs() & increasing front
   }
}

