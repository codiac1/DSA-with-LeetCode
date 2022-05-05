#include<stdio.h>
struct std
{
   int info;
   struct std *next;
};
struct std *new_node,*temp,*start=NULL,*preptr,*ptr;

int item,data,num,ch;
void insert_at_end(int item)
{
   new_node=(struct std*)malloc(sizeof(struct std));
   new_node->info=item;
   new_node->next=NULL;
  if(new_node==NULL)
     printf("\nOverflow!!\n");
  else
  {
     if(start==NULL)
     {
         start=new_node;
         temp=new_node;	
     }
      else
      {
          temp->next=new_node;
          temp=temp->next;
      }  	
  }     		
}

void insert_at_begin(int data)
{
   new_node=(struct std*)malloc(sizeof(struct std));
   new_node->info=data;
   new_node->next=NULL;
  if(new_node==NULL)
     printf("\nOverflow!!\n");
  else
  {
     new_node->next=start;
     start=new_node; 	
  }
}

void insert_at_pos(int item)
{
   
   new_node=(struct std*)malloc(sizeof(struct std));
   new_node->info=item;
   new_node->next=NULL;
  if(new_node==NULL)
     printf("\nOverflow!!\n");
  else
  {
    printf("Enter the node before u wanna insert the Element:\n");
    scanf("%d",&num);
    for(ptr=start;ptr->info!=num;ptr=ptr->next)
    {
       preptr=ptr;
    }
    preptr->next=new_node;
    new_node->next=ptr;	
  }      
}

void del_at_begin()
{
  if(start==NULL)
    printf("\nUnderflow!!\n");
  else
  {
     start=start->next;
  }  
}

void del_at_end()
{
  int p;
  if(start==NULL)
    printf("\nUnderflow!!\n");
  else
  {
    
    for(ptr=start;ptr->next->next!=NULL;ptr=ptr->next)
    {
       	
    }
    p=ptr->next;
    ptr->next=NULL;
   free(p);	
  }  
}

void display()
{
   if(start==NULL)
     printf("Underflow!!\n");
   else
   {
      for(temp=start;temp!=NULL;temp=temp->next)
          printf("%d ",temp->info);	
   }  
   printf("\n"); 
}
void del_at_pos()
{
  if(start==NULL)
     printf("Underflow!!\n");
   else
   {
       printf("Enter the node u wanna delete :\n");
       scanf("%d",&num);
      for(ptr=start;ptr->info!=num;ptr=ptr->next)
      {
       preptr=ptr;
      }
      preptr->next=ptr->next;
      free(ptr);
      
   }
}

int main()
{
     while(1)
    {
      printf("press your choice:\n <1> : Insertion at End\n <2> : Insertion at Begin\n <3> : Insertion at Pos\n <4> : Deletion at begin \n <5> : Deletion at End\n <6> : Deletion at Pos\n <7> : Display\n <8> : Exit\n");
      scanf("%d",&ch);
      switch(ch)
      {
         case 1 :printf("enter the element :\n");
                 scanf("%d",&item);
                 insert_at_end(item);
                 break;       		
         case 2 :printf("enter the element :\n");
                 scanf("%d",&item);
                 insert_at_begin(item);
                 break;
         case 3 :printf("enter the element :\n");
                 scanf("%d",&item);
                 insert_at_pos(item);
                 break;
         case 4 :del_at_begin();
                 break;
         case 5 :del_at_end(item);
                 break; 
         case 6 :del_at_pos(item);
                 break;  
         case 7 :display();
                 break;
         case 8 :exit(0);                            
         default: printf("wrong choice!!");
      }
   }
   return 0;
}

