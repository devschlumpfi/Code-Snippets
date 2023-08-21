function outerFunction() {
    const outerVar = "I am from outer function";
    
    function innerFunction() {
        console.log(outerVar);
    }

    return innerFunction;
}

const closure = outerFunction();
closure(); // Outputs: "I am from outer function"
