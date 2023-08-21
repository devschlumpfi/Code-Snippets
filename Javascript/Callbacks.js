function fetchData(callback) {
    setTimeout(() => {
        const data = { message: "Data fetched using callback" };
        callback(data);
    }, 2000);
}

function processData(data) {
    console.log(data.message);
}

fetchData(processData);
