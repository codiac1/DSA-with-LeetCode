#include<stdio.h>
#include<stdlib.h>
struct tree
{
  int info;
  struct tree*left;
  struct tree*right;
};
struct tree*insertion(struct tree*,int);
struct tree*deletion(struct tree*,int);
struct tree*successor(struct tree*);
void inorder(struct tree*);
void preorder(struct tree*);
void postorder(struct tree*);
struct tree*root=NULL,*temp;
int element,ch,item;
main()
{
while(1)
    {
      printf("press your choice:\n <1> : Insertion\n <2> : Deletion\n <3> : Inorder\n <4> : Preorder\n <5> : Postorder\n <6> : Exit \n");
      scanf("%d",&ch);
      switch(ch)
      {
         case 1 :printf("enter the element :\n");
                 scanf("%d",&item);
                 root=insertion(root,item);
                  break;		
         case 2 :printf("enter element to delete:\n");
                 scanf("%d",&item);
                 root=deletion(root,item);
                  break;
         case 3 :printf("Inorder:\n");
                 inorder(root);
                  break;
         case 4 :printf("Preorder:\n");
                 preorder(root);
                  break;
         case 5 :printf("Postorder:\n");
                 postorder(root);
                  break;
         case 6 :exit(0);
                  break;
    default: printf("wrong choice!!");			  				
     }
    }
}
struct tree*create(int element)
{
   struct tree*temp=(struct tree*)malloc(sizeof(struct tree));
   temp->info=element;
   temp->left=temp->right=NULL;
   return temp;
}
struct tree*insertion(struct tree*node,int element)
{
   if(node==NULL)
   {
     return create(element);
   }
   else if(element<node->info)
     {
        node->left=insertion(node->left,element);	
     }
   else
   {
        node->right=insertion(node->right,element);	
   }
return node;
}
void inorder(struct tree*node)
{
   if(node!=NULL)
   {
      inorder(node->left);
      printf("%d,",node->info);
      inorder(node->right);	
   }
}   
void preorder(struct tree*node)
{
   if(node!=NULL)
   {
     printf("%d,",node->info);
     preorder(node->left);
     preorder(node->right);
   }
}
void postorder(struct tree*node)
{
   if(node!=NULL)
   {
     postorder(node->left);
     postorder(node->right);
     printf("%d,",node->info);
   }
}
struct tree*successor(struct tree*node)
{
   struct tree*current=node;
   while(current!=NULL && current->left!=NULL)
     current=current->left;
return current;
}
struct tree*deletion(struct tree*node,int element)
{
  if(node==NULL)
  {
   return(node);	
  }
  if(element<node->info)
  node->left=deletion(node->left,element);
  else if(element>node->info)
  node->right=deletion(node->right,element);
  else
  {
    if(node->left==NULL)  //element has 1 child i.e. right child or no child
     {
       temp=node->right;
     free(node);
     return temp;	
     }
    else if(node->right==NULL) //element has 1 child i.e. left child
    {
     temp=node->left;
     free(node);
     return temp;
    }
    //element has 2 childs
         temp=successor(node->right);
         node->info=temp->info;
         node->right=deletion(node->right,temp->info);	
   }
   
return node;
   	
}
