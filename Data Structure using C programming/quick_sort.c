#include<stdio.h>
void swap(int a,int b)
{
   int temp;
     temp=a;
      a=b;
      b=temp;
}
void quick_sort(int a[],int n,int first,int last)
{
   int location,i;
   if(first<last)
   {
     location=partition(a,first,last);
     quick_sort(a,n,first,location-1);
     quick_sort(a,n,location+1,last);
   }
   printf("\nSorted Array:\n");
   for(i=0;i<n;i++)
     printf("%d ",a[i]);
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
    swap(a[start],a[end]);
  }	
 } 
 swap(a[first],a[end]);
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
   quick_sort(a,n,first,last);
 return 0;
}
