#include<stdio.h>
void swap(int *a,int *b)
{
   int temp=*a;
      *a=*b;
      *b=temp;
}
void quick_sort(int a[],int first,int last)
{
   int location;
   if(first<last)
   {
     location=partition(a,first,last);
     quick_sort(a,first,(location-1));
     quick_sort(a,(location+1),last);
   }
}
int partition(int a[],int first,int last)
{
  int pivot=a[first];
  int start=first;
  int end=last;
 while(start<end)
 {
    while(a[start]<=pivot)
      {
       start++;
      }
  while(a[end]>pivot)
  {
    end--;
  }
  if(start<end)
  {
    swap(&a[start],&a[end]);
    /*int temp=a[start];
    a[start]=a[end];
    a[end]=temp;*/
  }	
 } 
 
 swap(&a[first],&a[end]);
 /*int ptr=a[first];
 a[first]=a[end];
 a[end]=ptr;*/
 return end;
}


int main()
{
   int a[10],b[10],n,i,first,last;
   printf("Enter the size of array:\n");
   scanf("%d",&n);
   printf("Enter array elements:\n");
   for(i=0;i<n;i++)
     scanf("%d",&a[i]);
   printf("Unsorted Array:\n");
   for(i=0;i<n;i++)
     printf("%d ",a[i]);
   first=0;
   last=n-1;
   quick_sort(a,first,last);
   printf("\nSorted Array:\n");
   for(i=0;i<n;i++)
     printf("%d ",a[i]);
 return 0;
}
