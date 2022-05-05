#include<stdio.h>
#include<stdlib.h>
//FUNCTION DECLARATION
void create();
void traverse();
void insert_at_beg();
void insert_at_end();
void insert_pos();
void delete_at_beg();
void delete_at_end();
void delete_pos();

struct node
{
   int info;
   struct node *next;
};
struct node *start=NULL;
   //MAIN FUNCTION
int main()
{
   int choice;
   while(1)
   {
  
    printf("Singly Linked list operations\n");
    printf("MENU\n");
    printf("----*----*----*----\n");
    printf("1.Create\n");
    printf("2.Traverse\n");
    printf("3.Insert at the Beginning\n");
    printf("4.Insert at the End\n");
    printf("5.Insert at the Specified Position\n");
    printf("6.Delete the First node\n");
    printf("7.Delete the Last node\n");
    printf("8.Delete the Specified Node\n");
    printf("----*----*----*----\n");
    printf("Enter your Choice\n");
    scanf("%d\n",&choice);
    switch(choice)
    {
      case 1: create();
               break;
      case 2: traverse();
               break;
      case 3: insert_at_beg();
               break;
      case 4: insert_at_end();
               break;
      case 5: insert_pos();
               break;
      case 6: delete_at_beg();
               break;
      case 7: delete_at_end();
               break;
      case 8: delete_pos();
               break;
      default: printf("Wrong choice\n");
               break;         
    }   //END OF SWITCH
   }   //END OF WHILE
   return 0;
}   //END OF MAIN FUNCTION

  //CREATION OF A NEW NODE
void create()
{
  struct node *temp,*ptr;
  temp=(struct node*)malloc(sizeof(struct node));
  if(temp==NULL)
  {
    printf("Not Enough Space\n");//OVERFLOW CONDITION
    exit(0);
  }
  printf("Enter a value to be stored at the INFO part of the linked list\n");
  scanf("%d\n",&temp->info);
  temp->next=NULL;
  if(start==NULL)
  {
     start=temp;
  }
  else
  {
    ptr=start;
    while(ptr->next!=NULL)
    {
      ptr=ptr->next;
    }
    ptr->next=temp;
  }
  
}   //END OF CREATION

//TRAVERSING THE LINKED LIST
void traverse()
{
   struct node *ptr;
   if(start == NULL)
   {
      printf("List is Empty!!");  //UNDERFLOW
      exit(0);
   }
   else
   {
       ptr=start;
       printf("The List elements are:");
       while(ptr!=NULL)
       {
         printf("%d",ptr->info);
         ptr=ptr->next;
       } //END OF WHILE LOOP
   }//END OF ELSE
} // END OF traverse()

//INSERT A NODE AT BEGINNING
void insert_at_beg()
{
   struct node *temp;
   temp=(struct node*)malloc(sizeof(struct node));
   if(temp==NULL)
   {
     printf("Not Enough Space!!"); //OVERFLOW
     exit(0);
   }
   printf("Enter data value for node to be inserted");
   scanf("%d", &temp->info);
   temp->next = NULL;
   if(start==NULL)
   {
     start=temp;
   }
   else
   {
      temp->next=start;
      start=temp;
   } //END OF ELSE
   
}//END OF insert_at_beg()

//INSERT A NODE AT THE END
void insert_at_end()
{
   struct node *temp,*ptr;
   temp=(struct node*)malloc(sizeof(struct node));
   if(temp==NULL)
   {
     printf("Not Enough Space!!"); //OVERFLOW
     exit(0);
   }
   else
   {
     ptr=start;
     while(ptr->next!=NULL)
     {
         ptr=ptr->next;
     } //END OF WHILE
     ptr->next=temp;
   } //END OF ELSE
}//END OF insert_at_end()

//INSERT A NODE AT SPECIFIED POSITION
void insert_pos()
{
   struct node *temp,*ptr;
   int i,pos;
   temp=(struct node*)malloc(sizeof(struct node));
   if(temp==NULL)
   {
      printf("Not Enough Space!!"); //OVERFLOW
      exit(0);
   }
   printf("Enter the position of node to be inserted");
   scanf("%d",&pos);
   scanf("%d", &temp->info);
   temp->next=NULL;
   if(pos==0)
   {
      temp->next=start;
      start=temp;
   }
   else
   {
    for(i=0, ptr=start; i<(pos-1); i++)
    {
       ptr=ptr->next;
       if(ptr==NULL)
       {
         printf("Position not Found!!");
         exit(0);
       } //END OF IF
    } //END OF FOR LOOP
    temp->next=ptr->next;
    ptr->next=temp;
   } //END OF ELSE
} //END OF INSERT_POS()

//DELETE FROM BEGINNING
void delete_at_beg()
{
   struct node *ptr;
   if(ptr==NULL)
   {
     printf("List is Empty"); //UNDERFLOW
     exit(0);
   }
   else
   {
      ptr=start;
      start=start->next;
      printf("Deleted Element is %d",ptr->info);
      free(ptr);
   } //END OF ELSE
} //END OF DELETE_AT_BEGIN()

//DELETE FROM LAST
void delete_at_end()
{
   struct node *temp,*ptr;
   if(start == NULL)
   {
     printf("List is Empty"); //UNDERFLOW
     exit(0);
   }
   else if(start->next==NULL)
   {
     ptr=start;
     start=NULL;
     printf("Deleted element is %d",ptr->info);
     free(ptr);
   }
   else
   {
     ptr=start;
     while(ptr->next!=NULL)
     {
        temp=ptr;
        ptr=ptr->next;
        
     } //END OF WHILE LOOP
     temp->next =NULL;
     printf("Deleted element is %d",ptr->info);
     free(ptr);
   } //END OF ELSE
} //EMD OF delete_at_end()

//DELETE A SPECIFIED NODE AFTER ANY GIVEN NODE
void delete_pos()
{
  int i,pos;
  struct node *temp,*ptr;
  if(start==NULL)
  {
    printf("List is Empty!!"); //UNDERFLOW
    exit(0);
  } //END OF IF
  else
  {
    printf("Enter position of node to be deleted");
    scanf("%d", &pos);
    if(pos==0)
    {
      ptr=start;
      start=start->next;
      printf("Deleted element is %d",ptr->info);
      free(ptr);
    } //END OF IF
    else
    {
        ptr=start;
        for(i=0; i<pos; i++)
        {
           temp=ptr;
           ptr=ptr->next;
           if(ptr==NULL)
           {
              printf("Position not found!! ");
              exit(0);
           } //END OF IF
        } //END OF FOR
        temp->next=ptr->next;
        printf("Deleted element is %d",ptr->info);
        free(ptr);
    } //END OF INNER ELSE
  } //END OF OUTER ELSE
} //END OF DELETE_POS() 
