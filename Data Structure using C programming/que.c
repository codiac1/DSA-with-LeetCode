#include<stdio.h>
#define MAX 15
void enque();
void deque(); 
void display();
int que[MAX];
int choice ;
static int front = -1; 
static int rear = -1;
main()
{
 while(1)
 {
 printf("\n 1 - insert an element\n 2 - delete an element\n 3 - diplay the que");
 printf("\nenter your respective choice : ");
 scanf("%d", &choice);
 switch(choice)
 {
 	case (1):
        enque();
 		break;
 	case (2):
 		deque();
 		break;
 	case (3):
	    display();
		break;
	default:
	    printf("\nwrong choice made ");	    
 }
 }
}
void enque()
{
	int new ;
	if (rear == MAX-1)
       printf("\nque is full");
    else
	{
		if(front==-1)
		front =0;
		printf("\nenter the element in que : ");
		scanf("%d",&new);
		rear++;
		que[rear]= new;
	   }   
}
void deque()
{
	if (front == -1||front>rear)
	  printf("\nque is empty");
	else
	{
		printf("\ndeleted element from quue is %d ",que[front] );
		front++;
	  }  
}
void display()
{
	int i;
	if(front=-1)
	   printf("\nque is empty ");
	else
	{
	   printf("\nhere is the que : ");	
	   for (i=front;i<=rear;i++)
	       printf("\n%d",que[i]);
	   printf("\n");    
    }
}
