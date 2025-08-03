public class ARR02 {
    public static  void main(String args[]){
        // set difference 
        // int a[]={1,2,3,4,5};
        // int b[]={2,3,4,5,6};
        // int lenA=a.length;
        // int lenB=b.length;
        // int[] same = new int[5];  
        // int samei=0;       
        // int[] not_same = new int[5];
        // int not_samei=0;      
        // for(int i=0;i<lenA;i++){
        //     boolean flag=false;
        //     for(int j=0;j<lenB;j++){
        //         if(a[i]==b[j]){
        //             same[samei]=b[j];
        //             samei++;
        //             flag=true;
        //             break;
        //         }
                
        //     }
        //     if(!flag){
        //         not_same[not_samei]=a[i];
        //         not_samei++;
        //     }
        // }

        // for(int x=0;x<samei;x++){
        //     System.out.println("Same elements which is present in both a and b "+same[x]);
        // }
        
        // for(int y=0;y<not_samei;y++){
        //     System.out.println(" elements which are not  present in  a  not in  b "+not_same[y]);
        // }


        // Sorting 

        // int a[]={5,4,3,2,1};
        // int len=a.length;

        // for(int i=0;i<len;i++){
        //     for(int j=0;j<len-1;j++){
        //         if(a[j]>a[j+1]){
        //             int temp=a[j];
        //             a[j]=a[j+1];
        //             a[j+1]=temp;
        //         }
        //     }
        // }

        // for(int i=0;i<len;i++){
        //      System.out.println(a[i]);
        // }
       
        // given value 5
        int d[]={12,3,120,45,5,3,60,5,23,43,5};
        int len_D=d.length;

        int countr=0;
        int ind=0;
       
        for(int i=0;i<len_D;i++){
            if (d[i]==5){
                countr++;
            }
            if(countr==2){
                ind=i;
                break;
            }
        }
        
        
        
            for(int z=0;z<ind;z++){
                System.out.print(" "+d[z]);
            }
        
       
    }
    }

