arr = ['apple', 'hello', 'pen', 'help']

letters = "elpoh".split("")

for(let i of arr){
      bool = true
      dup = [...letters]
      for(let j of i){
            if(dup.includes(j)){
                  dup.slice(1,j)

            }else{
                  bool = false
                  break
            }
      }
      
      if(bool){
            console.log(i)
      }
      
}