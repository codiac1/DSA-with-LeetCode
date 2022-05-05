#include<stdio.h>
#include<stdlib.h>
#define MAX 5
void enq(int);
void deq();
void display();
int front=-1,rear= -1,q[MAX],i;
int main()
{
    int ch,item;
     while(1)
    {
      printf("press your choice:\n <1> : enqueue\n <2> : dequeue\n <3> : display\n <4> : exit \n");
      scanf("%d",&ch);
      switch(ch)
      {
         case 1 :printf("enter the element :\n");
                 scanf("%d",&item);
                 enq(item);
                 break;		
        case 2 :deq();
                break;
        case 3 :display();
                break;
        case 4 :exit(0);
    default: printf("wrong choice!!");
   }
}
return 0;
}
void enq(int data)
{
         if((rear+1)%MAX==front)
         printf("overflow!");
         else if (front ==-1 && rear==-1)
         {
             front = rear = 0;
             q[rear]=data;	
         }
         else
         {
             rear = (rear+1)%MAX;
             q[rear]=data;	
         }     
}
void deq()
{
    int item;
    item = q[front];
    if(front==-1 && rear==-1)
    printf("Underflow!!");
    else if(front==rear)
    front=rear=-1;
    else
    {
       front++;
       printf("deleted item : %d ", item);	
    }   
}
void display()
{
   //int i;
   if(front==-1 && rear==-1)
   printf("Underflow!!\n");
   else
  {
    for(i=front;i!=rear;i=((i+1)%MAX))
    printf("%d  ",q[i]);
    printf("%d  ",q[i]);	
  }	
}
