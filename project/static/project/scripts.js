document.addEventListener('DOMContentLoaded', function() {
    const apiChoice = document.getElementById('api_choice');
    const recommendationsContainer = document.getElementById('recommendations-container');

    // Function to fetch Myntra data
    function fetchMyntraData() {
        const myntraUrl = "https://www.myntra.com/formal-shoes/killer/killer-men-round-toe-lace-ups-formal-derby-shoes/31602544/buy";
        
        fetch(myntraUrl)
            .then(response => response.text())
            .then(html => {
                // Parsing the HTML and extracting recommendations or relevant data
                const parser = new DOMParser();
                const doc = parser.parseFromString(html, 'text/html');
                
                // Find and process recommendations - you may need to adjust based on Myntra's HTML structure
                const recommendations = doc.querySelectorAll('.recommendation-class'); // Example: Adjust this selector
                
                recommendations.forEach(item => {
                    const itemTitle = item.querySelector('.product-title').innerText; // Example: Adjust as needed
                    const itemPrice = item.querySelector('.product-price').innerText; // Example: Adjust as needed
                    const itemImage = item.querySelector('img').src; // Example: Adjust as needed
                    
                    const listItem = document.createElement('li');
                    listItem.innerHTML = `
                        <img src="${itemImage}" alt="${itemTitle}" width="100">
                        <p>${itemTitle}</p>
                        <p>Price: ${itemPrice}</p>
                    `;
                    recommendationsContainer.appendChild(listItem);
                });
            })
            .catch(error => console.log("Error fetching Myntra recommendations: ", error));
    }

    // Event listener for API choice change
    apiChoice.addEventListener('change', function() {
        const selectedApi = apiChoice.value;

        recommendationsContainer.innerHTML = ''; // Clear existing content

        if (selectedApi === 'myntra') {
            fetchMyntraData();
        }
        // Add similar fetch functions for Meesho if you have an API
    });
});
