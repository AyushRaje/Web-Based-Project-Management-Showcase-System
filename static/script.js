
// Function to fetch data from the API
async function fetchData() {
    const requestOptions = {
        method: 'GET', // Specify the type of request (GET, POST, etc.)
        // mode: 'no-cors' // Use 'no-cors' mode
    };

    try {
        // Replace 'https://api.example.com/view' with your API endpoint
        const response = await fetch('http://localhost:8000/auth/test', requestOptions);

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        console.log(data)
        displayData(data);
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
    }
}


// Function to display data on the webpage
function displayData(data) {
    const outputDiv = document.getElementById('output');
    outputDiv.innerHTML = ''; // Clear previous content
    outputDiv.innerHTML+=JSON.stringify(data)
    // Process data and display on the webpage
    
}

// Call the loadData function when the page loads
(async () => {
    await fetchData();
})();

// Call the fetchData function when the page loads