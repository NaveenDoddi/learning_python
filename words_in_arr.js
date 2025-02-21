arr = ['apple', 'hello', 'pen', 'help']

letters = "elpoh".split("")

for(let i of arr){
      bool = true
      let dup = [...letters]
      for(let j of i){
            if(dup.includes(j)){
                  dup.splice(dup.indexOf(j),1)
            }else{
                  bool = false
                  break
            }
      }      
      if(bool){
            console.log(i)
      }
      
}