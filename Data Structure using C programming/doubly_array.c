#include<stdio.h>
#include<stdlib.h>
#define MAX 10
int doubly_queue[MAX],front=-1,rear=-1;
void insert_rear(int);
void insert_front(int);
void del_front();
void del_rear();
void display();
int i,ch,item;
main()
{
   while(1)
   {
         printf("press your choice:\n <1> : Insert to rear\n <2> : Insert to front\n <3> : Delete from front\n <4> : Delete from rear \n <5> : Display\n <6> : Exit\n");
         scanf("%d",&ch);
       switch(ch)
        {
            
         case 1 :printf("enter the element :\n");
                 scanf("%d",&item);
                 insert_rear(item);
                   break;         		
         case 2 :printf("enter the element :\n");
                 scanf("%d",&item);
                 insert_front(item);
                 break;
         case 3 :del_front();
                 break;
         case 4 :del_rear();
                 break;
         case 5:printf("Doubly eneded queue:-\n");
                display();
                printf("\n");
                break;
          case 6 :exit(0);
         default :printf("wrong choice!!");
           }	
   }
}
void insert_rear(int item)
{
    if(front==0 && rear==MAX-1)
    printf("Overflow!!");
    else if(front==-1 && rear==-1)
    front=rear=0;
    else
    {
        rear++;	
    }
   
    doubly_queue[rear]=item;
}
void del_front()
{
    item=doubly_queue[front];
    if(front==-1)
    printf("Underflow!!");
    else if(front==rear)
    front=rear=-1;
    else
    front++;
   printf("Deleted:%d ",item);
}
void insert_front(int item)
{
    if(front==0 && rear==MAX-1)
    printf("Overflow!!");
    else if(front==-1 && rear==-1)
    front=rear=0;
    else
    {
         for(i=rear;i>=front;i--)
         doubly_queue[i+1]=doubly_queue[i];     
    } 
        doubly_queue[front]=item; 
}
void del_rear()
{
     item=doubly_queue[rear];
    if(front==-1)
    printf("Underflow!!");
    else if(front==rear)
    front=rear=-1;
    else
    rear--;
    printf("Deleted:%d",item);
}
void display()
{
  if(front==-1 && rear==-1)
  printf("Underflow!!");
  else
  {
     for(i=front;i<=rear;i++)
     {
       printf("%d ",doubly_queue[i]);
     }
 printf("%d ",doubly_queue[i]);
  }
}
