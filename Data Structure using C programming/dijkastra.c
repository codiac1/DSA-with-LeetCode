#include<stdio.h>
#define MAX 10
#define INFINITY 99999
int A[MAX][MAX],cost[MAX][MAX],visited[MAX],dist[MAX],predecessor[MAX],v,n;
int i,j;

void dijk(int A[MAX][MAX],int n,int v)
{
  int count,min,next_node;
  
  for(i=0;i<n;i++)
  {
   for(j=0;j<n;j++)
    {
       if(A[i][j]==0)
       {
          cost[i][j]=INFINITY;	
       }
       else
       {
          cost[i][j]=A[i][j];	
       }	
    }
  }
  for(i=0;i<n;i++)
  {
    dist[i]=cost[v][i];
    predecessor[i]=v;
    visited[i]=0;
  }
  dist[v]=0;
  visited[v]=1;
  count=1;
  
 while(count < n-1)
 {
    min=INFINITY;
    for(i=0;i<n;i++)
    {
      if(dist[i] < min && !visited[i])
      {
         min = dist[i];
         next_node=i;
      }	
    }
    
    visited[next_node]=1;
    for(i=0;i<n;i++)
    {
      if(!visited[i])
      {
         if((min + cost[next_node][i])< dist[i])
         {
            dist[i]=(min + cost[next_node][i]);
            predecessor[i]=next_node;
         }
      }
    }
  count++;  
 } 
}
void display()
{
   for(i=0;i<n;i++)
   {
      if(i != v)
      {
         printf("The distance of node %d is %d\n", i, dist[i]);
         printf("The path is: %d ",i);
         
         j=i;
         do
         {
           j=predecessor[j];
           printf("<- %d",j);
         }while(j != v);
      }
      printf("\n");
   }
}

int main()
{
   printf("Enter the no. of Vertices:\n");
   scanf("%d",&n);
   printf("Enter the Path Matrix of graph:\n");
   for(i=0;i<n;i++)
   {
     for(j=0;j<n;j++)
     {
        scanf("%d",&A[i][j]);
     }
   }
   printf("\nEnter the Starting Vertex:\n");
   scanf("%d",&v);
   dijk(A,n,v);
   display();
   return 0;
}
