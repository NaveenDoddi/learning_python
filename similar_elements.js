arr1 = [1,2,3,4,5,6,6]
arr2 = [1,0,3,8,9,6,6]
res = []
for(let i = 0; i < arr1.length; i++){
    var bool = false
    for (let j = 0; j < arr2.length; j++){
        if (arr1[i] == arr2[j]) bool = true
    }
    if (bool){
        res.push(arr1[i])
    }
}
// var result = new Set(res)

console.log(res)
