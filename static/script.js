
// Function to fetch data from the API
async function fetchData() {
    const requestOptions = {
        method: 'GET', // Specify the type of request (GET, POST, etc.)
        mode: 'no-cors' // Use 'no-cors' mode
    };

    try {
        // Replace 'https://api.example.com/view' with your API endpoint
        const response = await fetch('http://localhost:8000/auth/csrf', requestOptions);

        if (!response.ok) {
            throw new Error('Network response was not ok');
        }

        const data = await response.json();
        displayData(data);
    } catch (error) {
        console.error('There was a problem with the fetch operation:', error);
    }
}


// Function to display data on the webpage
async function displayData(data) {
    const outputDiv = document.getElementById('output');
    outputDiv.innerHTML = ''; // Clear previous content

    // Process data and display on the webpage
    data.forEach(item => {
        const itemElement = document.createElement('div');
        itemElement.textContent = `${item.name}: ${item.value}`;
        outputDiv.appendChild(itemElement);
    });
}

// Call the loadData function when the page loads
(async () => {
    await fetchData();
})();

// Call the fetchData function when the page loads