#include<stdio.h>
#include<stdlib.h>
#define MAX 10
int stack[MAX],top=-1,ch,item;
void push(int);
void pop();
void display();
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
    if(top==MAX-1)
    printf("Overflow!!");
    else if(top==-1)
    top=0;
    else
    top++;
stack[top]=item;
}
void pop()
{
item=stack[top];
   if(top==-1)
   printf("Underflow!!");
   else if(top==0)
   top=-1;
   else
   top--;
printf("Deleted:%d\n",item);   
}
void display()
{
   int i;
   if(top==-1)
   printf("Underflow");
   for(i=0;i<=top;i++)
   printf("%d ",stack[i]);
}
