arr = [1, 3, -1, -3, 5, 3, 6, 7]
target = 3
res = []
for (let i = 0; i <= arr.length-target; i++){
    max = arr[i]
    for (let j = i; j < i+target; j++){
        if(max < arr[j]){
            max = arr[j]
        }
    }
    res.push(max)
}
console.log(res)
