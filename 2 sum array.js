arr = [3, 2, 4, 5, 5, 7]
target = 10
// for (let i = 0; i < arr.length; i++){
//     for (let j = i+1; j < arr.length; j++){
//         if(arr[i] + arr[j] == target){
//             console.log(i, j)
//         }
//     }
// }
for (let i = 0; i < arr.length; i++){
    rem = target - arr[i]
    if (arr.includes(rem)){
        console.log(i, arr.indexOf(rem))
    }
}

// s = 0
// end = arr.length
