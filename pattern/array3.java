class array3{
    public static void main(String[] args) {
        // SHIFTING FRONT TO BACK 
        // int a[]={1,2,3,4,5,6};
        // int len=a.length;
        // int shift=2;

        // for(int k=0;k<shift;k++){
        //     int v=a[0];
        //     for (int i = 0; i < len; i++) {
        //         if (i + 1 < len) {
        //             a[i] = a[i + 1];
        //             if ((i + 1) == len - 1) {
        //                 a[len - 1] = v;
        //             }
        //         }
        //     }
        // }
        
        
        // for(int k=0;k<len;k++){
        //     System.out.print(" "+a[k]);
        // }

        // 2.Maximum consecutive one’s (or zeros) in a binary array
        // int a[]={0,1, 0, 1, 0,1,1,1,1,1};
        // int size=a.length;
        // System.out.println("The length of the array is :"+size);
        // int counter=0;
        // int value=0;
        // int max=0;
        // for(int i=0;i<size;i++){
            
        //    if ((i > 0 && a[i] == a[i - 1]) || (i+1 < size && a[i] == a[i + 1])){
        //                 counter++;
        //                 value=a[i];
        //                 System.out.println(a[i]);
        //     }
        // }
        // System.out.println("The number of times "+value+" is occured  consucutively is this "+counter);

        // 3.Move all zeros to end of array
        // task is to move all the zeros to the end of the array while maintaining the relative order of all non-zero elements
        int a[]={0, 0,4,5,0,7, 4, 3, 0, 5, 0};
        int size=a.length;
        int counter=0;
        boolean flag=false;
        int next=0;
        for(int i=0;i<size;i++){
            if(a[i]==0 ){
                if(((i+1<size && a[i+1]!=0) && (i-1>=0 && a[i-1]!=0)) ||( (i+1<size && a[i+1]!=0)&& (i-1>=0 && a[i-1]==0))){
                    next=a[i+1];
                    flag=true;
                    a[i+1]=a[i];
                }
                if(flag){
                    a[i]=next;
                }
                flag=false;
                counter++;
                
            }
        }
        
        // System.out.println(counter);
        for(int k=0;k<size;k++){
            System.out.print("  "+a[k]);
        }


        // 4.Reverse an Array in groups of given size
        // int a[]={1,2,3,4,5,6,7,8};
        // int size=a.length;
        // int k=2;
        // boolean flag=false;
        // int start=0;
        

        // while(k<size){
        
        //         for(int i=k;i>=start;i--){
        //                 System.out.print("   "+a[i]);
        //                 if(i==start){
        //                     flag=true;
        //                 }
        //             }
        //             if(flag){
        //                 start=k+1;
        //                 k=k+3;
        //                 flag = false;
        //             }
        //             if(k==8){
        //                 k=k-1;
        //             }
        //         }
        //             }
                       
                
    //   Sort an array in wave form
    // int a[]={12,13,14,15,17};
    // int size=a.length;
    // for(int i=0;i<=size-1;i+=2){
    //     if(i+1<size-1){
    //         int temp=a[i];
    //         a[i]=a[i+1];
    //         a[i+1]=temp;
    //     }
    // }
    
    // for(int k=0;k<size;k++){
    //     System.out.print(" "+a[k]);

    // }

    // Adding one to number represented as array of digits
    // int a[]={9,9,9};
    // int size=a.length;
    // String k="";
    // boolean flag=false;
    // for(int i=0;i<size;i++){
    //     k+=a[i];
    //     flag=true;
    // }

    // if(flag){
    //     int num = Integer.parseInt(k);
    //     num+=1;
    //     System.out.println(num);
    // }

   
    

   


    }}