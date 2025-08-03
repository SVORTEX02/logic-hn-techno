// let flag = false;
// let count = 0;

// // for (var i = -12, j = 2; i / 2 < 3 || j < 20; i = i + 1, j = j + 4, l = l + 1) {
// //   console.log("vijay");
// //   flag = true;
// // }

// // if (flag === true) {
// //   console.log("Total times printed:", l);
// // } else {
// //   console.log("not true");
// // }

// // var k = 0;

// // for (var i = 0; i < 3; i++) {
// //   console.log("hello<br/>");

// //   for (; k < 2; k++) {
// //     console.log("virin<br/>");
// //   }

// //   console.log("raam<br/>");
// // }

// // for (var i = 100, l = 0; i > 20; i = i - 30) {
// //   for (var j = 50; j > 10; j = j - 5) {
// //     console.log("hello<br/>");
// //     l++;
// //   }
// // }
// // console.log("your answer=" + l);

// var j = 50;

// for (var i = 100, l = 0; i > 20; i = i - 30) {
//   for (; j > 10; j = j - 5) {
//     console.log("hello<br/>");
//     l++;
//   }
//   console.log("radhe radhe<br/>");
// }
// console.log("your answer=" + l);

  var m = 100;
  for (var i = 0, he = 0, ra = 0, ka = 0; i < 200; i++) { //i=0
    for (var j = 0; j < 5; j++) {  //j=0
      for (var k = 1; k <= j; k++) {  //k=1 j=0  k<j false 
        i = i + 20;  
        he++;  //0 
        console.log("hello<br/>"); 
      }
      for (var k = 2; k <= 9; k = k * 1.5) {  //k=2 k=3 k=4.5  k=6.5 k=9.75
        i = i + 20;//i=20 i=40 i=60 i=80 i=100
        ra++; //
        console.log("radhe<br/>"); //radhe 
      }
    }
    for (var l = 0; l < m; l++) {
      i = i + 10;
      ka++;
      m = m - 20;
      console.log("krishna<br/>");
    }
  }
  console.log("hellocounter=" + he + "<br/>");
  console.log("radhecounter=" + ra + "<br/>");
  console.log("krishnacounter=" + ka + "<br/>");