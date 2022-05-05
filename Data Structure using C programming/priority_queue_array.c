#include<stdio.h>
#include<stdlib.h>
#define MAX 10
void insert(int,int);
int sort_priority();
void del_high_pri();
void display();
struct priority_queue
{
   int ele;
   int priority;
}pq[MAX],p_array[MAX];
int front=-1,rear=-1,p,i,j,max;
/*int asc_prior()
{
   for(i=0;i<=rear;i++)
   {
     p_array[i].priority=pq[i].priority;
   }
   max=p_array[0].priority;
   for(j=0;j<=i;j++)
   {
      if(p_array[j].priority<max)
      max=p_array[j].priority;
   }
return max;
}*/
int main()
{
    int ch,item,pri,a;
     while(1)
    {
      printf("press your choice:\n <1> : Insert\n  <2> : Delete highest priority\n <3> : display\n <4> : exit \n");
      scanf("%d",&ch);
      switch(ch)
      {
         case 1 :printf("\nEnter an element :");
                 scanf("%d",&item);
                 printf("\nEnter its priority :");
                 scanf("%d",&pri);
                 insert(item,pri);
                 break;
                 		
         case 2 :del_high_pri();
                 break;
         case 3 :printf("Our Priority Queue: ");
                 a=sort_priority();
                 display();
                 break;
         case 4 :exit(0);
                 break;
    default: printf("wrong choice!!");
     }
}
return 0;
}
void insert(int item,int p)
{
   if(front==0 && rear==MAX-1)
   printf("Overflow!!\n");
   else
   {
     rear=rear+1;
     pq[rear].ele=item;
     pq[rear].priority=p;
   }
}
int sort_priority()
{
   int i,j;
   struct priority_queue temp;
   for(i=0;i<rear;i++)
   {
     for(j=0;j<rear-i;j++)
     {
       if(pq[j].priority>pq[j+1].priority)
       {
          temp=pq[j];
          pq[j]=pq[j+1];
          pq[j+1]=temp;
       }
     }
   }
   max=pq[0].priority;
   return max;
}
/*int highest_priority()
{
   int i,p=-1;
   if(!(front==-1 && rear==-1)) // Underflow
   {
      for(i=0;i<=rear;i++)
      {
         if(pq[i].priority>p)
         p=pq[i].priority;
      }
   }
   return p;
}*/
void del_high_pri()
{
    int i,j,prior,ele;
    if(front==-1 && rear==-1)
    printf("Underflow!!\n");
    else
   {
    prior=sort_priority();
    for(i=0;i<=rear;i++)
    {
       if(pq[i].priority==prior)
       {
          ele=pq[i].ele;
          break;
       }
    }
    if(i<rear)
    {
      for(j=i;j<rear;j++)
      {
        pq[j].ele=pq[j+1].ele;
        pq[j].priority=pq[j+1].priority;
      }
    }
    rear=rear-1;
    printf("%d",ele); 
 }
}
void display()
{
   int i;
   if(front==-1 && rear==-1)
   printf("Underflow!!\n");
   else
   {
      for(i=0;i<=rear;i++)
      printf("element:%d - priority:%d \n",pq[i].ele,pq[i].priority);
   }   
}
