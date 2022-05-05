#include<stdio.h>
#define MAX 10
#define INFINITY 99999
int A[MAX][MAX],visited[MAX],i,j,n;
int count=1,a,b,u,v,min,min_cost=0;
void mst(int A[MAX][MAX],int n)
{ 
  for(i=0;i<n;i++)
  {
   for(j=0;j<n;j++)
    {
       if(A[i][j]==0)
        A[i][j]=INFINITY;
    }
  }
   visited[0]=1;
   printf("\n");
   while(count < n)
   {
     min=INFINITY;
     for(i=0;i<n;i++)
      { 
        for(j=0;j<n;j++)
        {
            if(A[i][j] < min)
            {
               if(visited[i]!=0)
               {
                 min=A[i][j];
                 a=u=i;
                 b=v=j;
               }
            }
          }
        }
            if(visited[u]==0 || visited[v]==0)
            {
              printf("\n Edge %d:(%d %d) Cost:%d",count++,a,b,min);
              min_cost=min_cost+min;
              visited[b]=1;
            }
            A[a][b]=A[b][a]=INFINITY;
        }
        printf("\nTotal Minimum Cost = %d",min_cost);
      }	
int main()
{
   printf("Enter the no. of Vertices:\n");
   scanf("%d",&n);
   printf("Enter path matrix of Graph:\n");
   for(i=0;i<n;i++)
   {
     for(j=0;j<n;j++)
     {
        scanf("%d",&A[i][j]);
     }
   }
mst(A,n); 
return 0;
}
