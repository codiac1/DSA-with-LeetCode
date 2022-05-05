#include<stdio.h>
#include<stdlib.h>
void enq_rear(int);
void deq_front();
void enq_front(int);
void deq_rear();
void display();
struct std 
{
   int info;
   struct std* next;
};
struct std *front = NULL, *rear = NULL, *temp,*node;
int main()
{
   int ch,item,p;
   while(1)
   {
      printf("enter <1> for input restricted queue\n press <2> for out put ristricted queue :\n ");
      scanf("%d",&p);
      switch(p)
      {
         case 1:
         {
           while(1)
           {
              printf("press your choice:\n <1> : equeue_front\n <2> : deq_front\n <3> : deq_rear\n <4> : display\n <5> : exit \n");
              scanf("%d",&ch);
              switch(ch)
               {
                  case 1 :printf("enter the element :\n");
                          scanf("%d",&item);
                          enq_front(item);
                          break;
                  case 2 :deq_front();
                          break;
                  case 3 :deq_rear(); 
                          break;       
                  case 4 :display();
                          break;
                  case 5 :exit(0);
                         
                }
               }
         break;
     }
  case 2:
{
  while(1)
  {
     printf("press your choice:\n<1>enq_rear\n <2> : enq_front\n <3> : deq_rear\n <4> : display\n <5> : exit \n");
     scanf("%d",&ch);
     switch(ch)
     {
       case 1 :printf("enter the element :\n");
               scanf("%d",&item);
               enq_rear(item);
               break;
       case 2 :printf("enter the element :\n");
               scanf("%d",&item);
               enq_front(item);
               break;
       case 3 :deq_rear();
               break;       
       case 4 :display();
               break;
       case 5 :exit(0);       
     }					        
    }
   break;
  }
 }
}
return 0;
}
void enq_rear(int data)
{
   node = (struct std*)malloc(sizeof(struct std));
   node->info = data;
   node->next = NULL;
   if(node==NULL)
      printf("overflow!");
   else if(front == NULL && rear == NULL)
      rear = front = node;
   else
    {
       rear->next= node;
       rear = node;
    }	   
}
void enq_front(int data)
{
    node = (struct std*)malloc(sizeof(struct std));
    node->info = data;
    node->next = NULL;
    if(node==NULL)
       printf("overflow!");
    else if(front ==NULL && rear == NULL)
       rear = front = node;
    else
    {
       node->next = front;
       front=node;
    }	
}
void deq_front()
{
   temp = front;
   if(front ==NULL && rear == NULL)
      printf("\nempty!");
   else if (front==rear)
   {
      front = rear = NULL;
      free(temp);
   }
   else
   {
     front = front->next;
     free(temp);
   }
}
void deq_rear()
{
    if(front == NULL && rear == NULL)
        printf("\nempty!");
    else if(front == rear)
    {
        front = rear = NULL;
    }
    else
    {
      for(temp = front;temp->next!=rear;temp = temp->next);
      temp->next = NULL;
      rear = temp;
    }
}
void display()
{
    if(front ==NULL && rear == NULL)
         printf("\nempty!");
    else
    {
      printf("here is your queue !\n");	
      for(temp=front; temp!=rear;temp=temp->next)
      printf("%d ",temp->info);
      printf("%d\n",temp->info);   
    }   
}
