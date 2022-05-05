#include<stdio.h>
#include<stdlib.h>
void linked_list();
void reverse_list();
void display();
struct std
  {
     int info;
     struct std* next;
  }; 
 struct std*temp,*node,*start=NULL;
 
int item;
char c; 
int main()
{
	int ch;
   while(1)
   {
     printf("<1> : Linked List\n<2> : Reversed Linked List\n<3> : Display\n<4> : Exit\n");
     scanf("%d",&ch);
     switch(ch)
     {
        case 1: linked_list();
                break;
        case 2: reverse_list(&start);
                break;
        case 3: display();
                 break;
        case 4: exit(0);
        default:printf("Wrong choice!!");
     }
   }
 /* linked_list();
  printf("Linked list : \n");
  display();
  printf("Reverse of Linked list : \n");
  reverse_list(start);
  display();*/
return 0;
}

void linked_list()
{
	
  do
  {
   node=(struct std*)malloc(sizeof(struct std));
   printf("Enter a value to be inserted:\n");
   scanf("%d",&item);
   node->info=item;
   node->next=NULL;
   if(start==NULL)
   {
     start=node;
     temp=node;	
   }
   else
   {
     temp->next=node;
     temp=temp->next;
   }
   fflush(stdin);
   printf("\nDo u wanna continue ?:(y/n)\n");
   scanf("%c",&c);	
 }while(c=='y' || c=='Y');
}

void reverse_list(struct std**start)
{
   struct std *prev=NULL;
   struct std *current= *start;
   struct std *next=NULL;
   
   while(current!=NULL)
   {
      next=current->next;
      current->next=prev;
      
      prev=current;
      current=next;
   }
   *start=prev;  
}

void display()
{
   
 for(temp=start; temp!=NULL; temp=temp->next)
 {
    printf("%d->",temp->info);
 }
  printf("NULL\n");
}
