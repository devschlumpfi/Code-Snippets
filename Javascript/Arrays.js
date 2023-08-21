let numbers = [1, 2, 3, 4, 5];
console.log(numbers.length); // 5

numbers.push(6); // Add element at the end
numbers.pop();   // Remove last element
console.log(numbers); // [1, 2, 3, 4, 5]

let slicedArray = numbers.slice(1, 3);
console.log(slicedArray); // [2, 3]
