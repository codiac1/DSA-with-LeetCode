#include<stdio.h>
#include<stdlib.h>
#define MAX 10
#define INFINITY 99999
int distance[MAX][MAX],A[MAX][MAX],i,j,k,n;
void f_warshall(int A[MAX][MAX],int n)
{
  for(i=0;i<n;i++)
  {
    for(j=0;j<n;j++)
    {
        if(A[i][j]==0)
          distance[i][j]=INFINITY;
        else
          distance[i][j]=A[i][j];
    }
  }
  
 for(k=0;k<n;k++)
 {
    for(i=0;i<n;i++)
    {
      for(j=0;j<n;j++)
      {
         if(distance[i][k]==INFINITY || distance[k][j]==INFINITY)
            continue;
         else if((distance[i][k]+distance[k][j]) < distance[i][j])
            distance[i][j] = (distance[i][k]+distance[k][j]);
         else if(i==j)
            distance[i][j]=0;   
      }
    }
 }//END of for loop of k 
  
 for(i=0;i<n;i++)
 {
   for(j=0;j<n;j++)
     printf("Distance from %d to %d is %d\n",i,j,distance[i][j]);  	
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
   f_warshall(A,n);
   return 0;
}
