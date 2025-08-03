class looop{
  public static void main(String args[]){
        // for (int  i = 0; i <= 5; i++) {
        //     for (int  j = 0; j <= 5; j++) {
        //       System.out.print("* ");
        //     }
        //   System.out.println(" ");
        //   }
        
        // simple method1 
        for(int i=0;i<=5;i++) {
          for(int j=1;j<=i;j++){
            System.out.print("*");
          }
          System.out.println(" ");
        }
        
        // for(int a=120;a<=440;a+=64){
        //   System.out.println("@");
        // }

        // for(int a=120;a<=440;a*=){
        //   System.out.print("&");
        // }
        //method 2

        for(int a=120;a<=440;a+=64){
          for(int b=20;b<=a;b+=60){
            System.out.print("$");
          }
          System.out.println(" ");
        }


        for(int k=12;k<=50;k*=){
          System.out.println("&");
        }

        // method 3  
        // for(int k=12;k<=50;k*=0.68){
        //   for(int l=24;l<=60;l++){
        //     System.out.print("#");
        //   }
        //   System.out.println(" ");
        // }


  }
}
