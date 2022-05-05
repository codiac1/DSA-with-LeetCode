#include<stdio.h>
#include<stdlib.h>

int item,y;
struct node
{
  int data;
  struct node *child,*next;
}*start,*temp,*newnode,*ptr;

struct std
{
  int info;
  struct std *nxt;
}*head,*node,*temp2,*ptr1;

//typedef struct node *list;
//typedef struct std *linked;

struct node *create()
{
  newnode = (struct node*)malloc(sizeof(struct node));
  if(newnode==NULL)
  {
     printf("\nSomething Went Wrong..!");
     exit(0);
  }
 newnode->data = item;
 newnode->next = NULL;
 newnode->child = NULL;
return newnode;
}

struct std *create2()
{
  node = (struct std*)malloc(sizeof(struct std));
  if(node==NULL)
  {
    printf("\nSomething Went Wrong..!");
    exit(0);
  }
 node->info = item;
 node->nxt = NULL;
return node;
}

struct std *adjacency()
{
  int i=1,ch1;
  while(i)
  {
     printf("\nDo you want to insert its adjacent node(1/0): ");
     scanf("%d",&ch1);
     if(ch1==1)
      {
        printf("\nEnter node adjacent to node %d: ",item);
        scanf("%d",&y);
        ptr1=create2();
        ptr1->info = y;
        if(head == NULL)
        {
          head = ptr1;
        }
        else
        {
          temp2 = head;
        while(temp2->nxt != NULL)
        {
          temp2 = temp2->nxt;
        }
       temp2->nxt = ptr1;
       }
      }
   else
   {
     i=0;
   }
 }
 return head;	
}

void insert()
{
  printf("\nEnter data: ");
  scanf("%d",&item);
  ptr = create();
  ptr->data = item;
  ptr->child = adjacency(); 
 if(start==NULL)
  {
    start = ptr;
  }
 else
 {
   temp = start;
   while(temp->next != NULL)
   {
     temp=temp->next;
   }
  temp->next = ptr;
 }
head = NULL;
}

void display()
{
  temp = start;
  while(temp!=NULL)
  {
     printf("\n%d\n",temp->data);
     temp2=temp->child;
     while(temp2!=NULL)
     {
        printf("->%d",temp2->info);
        temp2=temp2->nxt;
     }
     temp=temp->next;
  }
}

int main()
{
  int ch;
  printf("\n1:INSERT\t2:DISPLAY\t3:EXIT\n");
  while(1)
  {
    printf("\nEnter choice: ");
    scanf("%d",&ch);
    switch(ch)
    {
      case 1: insert();
              break;
      case 2: display();
              break;
      case 3: exit(0);
              break;
     default: printf("\nWrong choice...");
    }
		
   }
return 0;
}
