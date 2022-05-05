#include<stdio.h>
int i,j,k;
void merge(int a[],int first,int mid,int last)
{
   int b[10];
   i=first;
   j=mid+1;
   k=first;
 while(i<=mid && j<=last)
 {
    if(a[i]<=a[j])
    {
      b[k]=a[i];
      i++;
    }
    else
    {
       b[k]=a[j];
       j++;	
    }
    k++;	
 } 
 if(i>mid)
 {
   while(j<=last)
    {
      b[k]=a[j];
      j++;
      k++;	
    }	
 }
 else
 {
    while(i<=mid)
   {
      b[k]=a[i];
      i++;
      k++;	
   }
 }
 for(k=first;k<=last;k++)
 {
    a[k]=b[k];
 }  
}

void merge_sort(int a[],int first,int last)
{
   
   int mid; 
   if(first<last)
   {	
     mid=(first+last)/2;	
     merge_sort(a,first,mid);
     merge_sort(a,(mid+1),last); 
     merge(a,first,mid,last);
   }     
}
int main()
{
   int a[10],b[10],n,first,last;
   printf("Enter the size of array:\n");
   scanf("%d",&n);
   printf("Enter array elements:\n");
   for(i=0;i<n;i++)
     scanf("%d",&a[i]);
   printf("Unsorted Array:\n");
   for(i=0;i<n;i++)
     printf("%d ",a[i]);
   first=0;
   last=(n-1); 
   merge_sort(a,first,last);	
   printf("\nSorted Array:\n");
   for(i=0;i<n;i++)
     printf("%d ",a[i]); 
   return 0;
}
