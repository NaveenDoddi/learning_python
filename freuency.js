string = 'HeLlo world 123 @#$#'
let filteredString = string.toLowerCase().split(' ').join("");
let frequency = {}

// Count frequencies
for (let char of filteredString) {
    // Object.keys(frequency).find((i) => i == filteredString[char]) ? frequency[filteredString[char]] += 1 : frequency[filteredString[char]] = 1
    frequency[char] == undefined ? frequency[char] = 1 : frequency[char] += 1 
}
console.log(frequency);

// { h: 1, e: 1, l: 3, o: 2, w: 1, r: 1, d: 1 }

