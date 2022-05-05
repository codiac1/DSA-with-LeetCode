#include<stdio.h>
#include<stdlib.h>
void push(int);
void pop();
void display();
struct std
{
   int info;
   struct std*next;
};
struct std*top=NULL,*node,*temp,*start;
int item,ch;
main()
{
   while(1)
    {
      printf("press your choice:\n <1> : Push\n <2> : Pop\n <3> : display\n <4> : exit \n");
      scanf("%d",&ch);
      switch(ch)
      {
         case 1 :printf("enter the element :\n");
                 scanf("%d",&item);
                 push(item);
                 break;		
         case 2 :pop();
                 break;
         case 3 :printf("Our stack as follows: ");
                 display();
                printf("\n");
                 break;
    case 4 :exit(0);
            break;
    default: printf("wrong choice!!");
     }
 } 
}
void push(int item)
{
   node=(struct std*)malloc(sizeof(struct std));
   node->info=item;
   node->next=NULL;
   
   if(node==NULL)
   printf("Overflow!!");
   else if(top==NULL)
   {
      top=node;
      start=node;	
   }

   else
   {
      top->next=node;
      top=node;	
   }
}
void pop()
{
   item=top->info;
   if(top==NULL)
   {
       printf("Underflow!!");	
   }
   else if(top==start)
   top=NULL;
   else
   {
     for(temp=start;temp->next!=top;temp=temp->next)
     {
     	
     }
     temp->next=NULL;
     top=temp;	
   }
printf("Deleted:%d ",item);

}
void display()
{
  if(top==NULL)
  printf("Underflow!!");
  else
  {
    for(temp=start;temp!=top;temp=temp->next)
    {
      printf("%d ",temp->info);
    }
     printf("%d ",temp->info);
  }
}
