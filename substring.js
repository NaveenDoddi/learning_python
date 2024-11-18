var str = "eceba";
k = 2;
var arr = [];

for(let i = 0; i < str.length; i++){

      var new_ele = str[i];
      arr.push(new_ele)

      var dummy = (arr.filter((j) => j == new_ele))

      if(dummy.length == k){
            break;
      }


}
console.log(arr.length)

