let person = {
    firstName: "John",
    lastName: "Doe",
    age: 30,
    greet: function() {
        console.log(`Hello, my name is ${this.firstName} ${this.lastName}.`);
    }
};

console.log(person.firstName); // John
person.greet(); // Hello, my name is John Doe.
