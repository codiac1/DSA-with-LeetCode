#include<stdio.h>
int A[20][20],stack[20],visited[20],n,i,j,top=-1;
void dfs(int);
int main()
{
   int v;
   printf("Enter the no. of Vertices:\n");
   scanf("%d",&n);
   for(i=0;i<n;i++)
   {
       stack[i]=0;
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
   dfs(v);
   printf("Traversed nodes are:\n");
   for(i=0;i<n;i++)
   {
      if(visited[i])
        printf("\nThe Node %d is reachable",i);
     else
      {
         printf("\nThe Node %d is not reachable",i);
      }
   }
   return 0;
}

void dfs(int v)
{
   for(i=0;i<n;i++)
   {
      if(A[v][i] && !visited[i])
          stack[++top]=i;	
   }
   if(top!=-1)
   {
      visited[stack[top]]=1;
      dfs(stack[--top]);   //recursively calling dfs() & decreasing top
   }
}                                                                                                   
