#include<stdio.h>
#include<stdlib.h>
void enqueue(int);
void dequeue();
void display();
struct std
{
   int info;
   struct std*next;
};
struct std*front=NULL,*rear=NULL,*node,*temp;
int item,ch;
main()
{
     while(1)
    {
      printf("press your choice:\n <1> : enqueue\n <2> : dequeue\n <3> : display\n <4> : exit \n");
      scanf("%d",&ch);
      switch(ch)
      {
         case 1 :printf("enter the element :\n");
                 scanf("%d",&item);
                 enqueue(item);
                 break;		
    case 2 :dequeue();
          break;
    case 3 :printf("Our Circular Queue as follows:-\n");
            display();
            break;
    case 4 :exit(0);
    default: printf("wrong choice!!");
      }
   }
}
void enqueue(int data)
{
   node=(struct std*)malloc(sizeof(struct std));
   node->info=data;
   node->next=NULL;
   if(node==NULL)
   printf("Overflow!!");
   else if(front==NULL && rear==NULL)
   {
     front=rear=node;
   }
   else
   {
     rear->next=node;
     rear=node;
   }
rear->next=front; //In circular queue,after reaching to last node,we started inserting from 1st node  
}
void dequeue()
{
    temp=front;
    //item=front->info;
   if(front==NULL && rear==NULL)
   printf("Underflow!!");
   else if(front==rear)
   front=rear=NULL;
   else
   {
      front=front->next;
   }
   printf("Deleted:%d\n",temp->info); 
   free(temp);
}
void display()
{
    temp=front;
   if(front==NULL && rear==NULL)
   printf("Underflow!!");
   while(temp!=rear)
   {
      printf("%d ",temp->info);
      temp=temp->next;
   }
   printf("%d ",temp->info); 
   printf("\n"); 
}
