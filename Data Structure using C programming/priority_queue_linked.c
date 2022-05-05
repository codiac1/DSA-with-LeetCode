#include<stdio.h>
#include<stdlib.h>
typedef struct std
{
   int info;
   int priority;
   struct std *next;
}Node;
Node *front=NULL,*temp,*ptr;

void insert(int ele,int priority)
{
   temp=(Node*)malloc(sizeof(Node));
   temp->info=ele;
   temp->priority=priority;
   temp->next=NULL;
   
   if((front==NULL) || (priority<front->priority))
   {
      temp->next=front;
      front=temp;
   }
   else
   {
     ptr=front;
     while(ptr->next!=NULL && ptr->next->priority <= priority)
     {
        ptr=ptr->next;
     }
     temp->next=ptr->next;
     ptr->next=temp;
   }
}

void del()
{
   if(front==NULL)
     printf("Underflow!!\n");
   else
   {
     temp=front;
     printf("Deleted Item: %d\n",temp->info);
     front=front->next;
     free(temp);
   }
}

void display()
{
   if(front==NULL)
     printf("Underflow!!");
   else
   {
     for(ptr=front;ptr!=NULL;ptr=ptr->next)
       printf("Element: %d Priority: %d\n",ptr->info,ptr->priority);	
   } 
}

int main()
{
    int ch,item,pri,a;
     while(1)
    {
      printf("press your choice:\n <1> : Insert\n <2> : Delete highest priority\n <3> : display\n <4> : exit \n");
      scanf("%d",&ch);
      switch(ch)
      {
         case 1 :printf("\nEnter an element :");
                 scanf("%d",&item);
                 printf("\nEnter its priority :");
                 scanf("%d",&pri);
                 insert(item,pri);
                 break;       		
         case 2 :del();
                 break;
         case 3 :printf("Our Priority Queue: \n");
                 display();
                 break;
         case 4 :exit(0);
    default: printf("wrong choice!!");
     }
}
return 0;
}
