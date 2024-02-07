//try it yourself in c or c++

#include <iostream>
using namespace std;
int i=0;
void bsort(int arr[], int j,int n){
    if(j==0){
        return;
    }
    
    bsort(arr,j-1,n);
    if(j%n!=0){
         int temp;
         if(arr[i]>arr[i+1]){
             temp=arr[i];
             arr[i]=arr[i+1];
             arr[i+1]=temp;
             i++;
         }
    }else{
        i=0;
    }
}
int main() {
    // Write C++ code here
    int arr1[5]{5,4,3,2,1};
    bsort(arr1,25,5);
    
    for(int i=0; i<5; i++){
        cout<<arr1[i]<<"\t";
    }
     return 0;
}
