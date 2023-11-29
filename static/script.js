
document.addEventListener('DOMContentLoaded', function () {
  console.log('Document is ready.');
  const featuredCategories = document.getElementById('featured-categories');
  console.log(featuredCategories);
  const form = document.getElementById('drink-search-form');
  const drinkModal = document.querySelector('.drink-modal');
  const closeDrinkModal = document.querySelector('.close');
  const drinkResults = document.getElementById('drink-results')

  form.addEventListener('submit', function (event) {
    console.log('Form submitted.');
    event.preventDefault();
  });

  // Function to create an ingredients list
  function createIngredientsList(drink) {
    let ingredientsList = '';
    for (let i = 1; i <= 15; i++) {
      const ingredient = drink[`strIngredient${i}`];
      if (ingredient) {
        const measure = drink[`strMeasure${i}`] || '';
        ingredientsList += `<li>${measure} ${ingredient}</li>`;
      }
    }
    return ingredientsList;
  }

// Function to display the search results
function displayResults(results) {
  const drinkResults = document.getElementById('drink-results');
  drinkResults.innerHTML = ''; // Clear previous results

  if (results) {
    results.forEach(drink => {
      const drinkCard = document.createElement('div');
      drinkCard.classList.add('drink-card');
      drinkCard.setAttribute('data-id', drink.idDrink);

      let cardContent = `
        <img src="${drink.strDrinkThumb}" alt="${drink.strDrink}" class="drink-image">
        <h3>${drink.strDrink}</h3>
      `;

      if (isAuthenticated) {
        console.log('User is logged in.');
        if (drinkId in likedDrinks) {
          cardContent += `
            <button class="add-to-liked" disabled>Added to Liked Drinks</button>
          `;
        } else {
          cardContent += `
            <button class="add-to-liked">Add to Liked Drinks</button>
          `;
        }
      } else {
        console.log('User is not logged in.');
      }


      drinkCard.innerHTML = cardContent;

      drinkResults.appendChild(drinkCard);

      drinkCard.addEventListener('click', function () {
        const drinkId = this.getAttribute('data-id');
        console.log('Clicked on drink ID:', drinkId);
      });
    });
  } else {
    drinkResults.textContent = 'No drinks found.';
  }
}

  // Event listener for the "Search" button click
  document.getElementById('search-btn').addEventListener('click', function () {
    // Get the selected "Filter By" option
    const filterBy = document.getElementById('filter-by').value;

    // Get user input based on the selected filter
    let searchValue = '';
    if (filterBy === 'drink-name') {
      searchValue = document.getElementById('drink').value;
    } else if (filterBy === 'ingredients') {
      const ingredientSelect = document.getElementById('ingredient');
      searchValue = Array.from(ingredientSelect.selectedOptions).map(option => option.value).join(',');
    } else if (filterBy === 'glass-type') {
      searchValue = document.getElementById('glass').value;
    } else if (filterBy === 'category') {
      searchValue = document.getElementById('category').value;
    }

    // Use the search value to perform the search
    performSearch(filterBy, searchValue);
  });

  // Function to perform the search
  function performSearch(filterBy, searchValue, category = null) {
    // Define the API URL based on the filter and search value
    let apiUrl = 'https://thecocktaildb.com/api/json/v1/1/';

    if (filterBy === 'drink-name') {
      apiUrl += `search.php?s=${searchValue}`;
    } else if (filterBy === 'ingredients') {
      apiUrl += `filter.php?i=${searchValue}`;
    } else if (filterBy === 'glass-type') {
      apiUrl += `filter.php?g=${searchValue}`;
    } else if (filterBy === 'category') {
      apiUrl += `filter.php?c=${searchValue}`;
    }

    // Make an API request to TheCocktailDB
    fetch(apiUrl)
      .then(response => {
        if (!response.ok) {
          throw new Error(`Network response was not ok: ${response.status} - ${response.statusText}`);
        }
        return response.json();
      })
      .then(data => {
        console.log(data);
        if (data && data.drinks) {
          // Process the API response and display the results
          displayResults(data.drinks);
        } else {
          // Handle the case where the API response doesn't contain drinks
          displayResults(null);
        }
      })
      .catch(error => {
        console.error('Error fetching data:', error);
      });
  }

  // Initial call to set the default filter
  document.getElementById('filter-by').dispatchEvent(new Event('change'));

 // Event listener for clicking on a drink image
  if (drinkResults) {
    drinkResults.addEventListener('click', function (event) {
      const clickedElement = event.target.closest('.drink-card');

      if (clickedElement) {
        // Check if the clicked element is the "Add to Liked Drinks" button
        if (!event.target.classList.contains('add-to-liked')) {
          const drinkId = clickedElement.getAttribute('data-id');

          if (drinkId) {
            console.log('Fetching details for drink ID:', drinkId);

            // Fetch additional details for the clicked drink by its ID
            fetch(`https://thecocktaildb.com/api/json/v1/1/lookup.php?i=${drinkId}`)
              .then(response => response.json())
              .then(data => {
                // Handle the API response data and construct the modal content
                if (data.drinks && data.drinks.length > 0) {
                  const drink = data.drinks[0];
                  const drinkDetailsHTML = `
                    <h3>${drink.strDrink}</h3>
                    <img src="${drink.strDrinkThumb}" alt="${drink.strDrink}" class="drink-image-modal">
                    <p>${drink.strInstructions}</p>
                    <ul class="ingredients-modal">
                      ${createIngredientsList(drink)}
                    </ul>
                  `;
                  document.getElementById('drink-modal-details').innerHTML = drinkDetailsHTML;

                  // Show the drink modal
                  drinkModal.style.display = 'block';
                  console.log("Displaying modal");
                } else {
                  console.error('No drinks found for the given ID.');
                }
              })
              .catch(error => {
                console.error('Error fetching additional drink details:', error);
              });
          }
        }
      }
    });
  }


  // Event listener for closing the drink modal
  closeDrinkModal.addEventListener('click', function () {
    drinkModal.style.display = 'none';
  });

  
  // Event listener for clicking on the "Add to Liked Drinks" button
  drinkResults.addEventListener('click', function (event) {
    
    const clickedElement = event.target.closest('.drink-card');

    if (clickedElement && event.target.classList.contains('add-to-liked')) {
      const drinkId = clickedElement.getAttribute('data-id');
      console.log(`Adding drink ID ${drinkId} to liked drinks...`);
      
      fetch(`/add-to-liked/${drinkId}`, {
        method: 'POST',
      })
        .then(response => {
          if (!response.ok) {
            throw new Error(`Network response was not ok: ${response.status} - ${response.statusText}`);
          }
          return response.json();
        })
        .then(data => {
          console.log('Drink added to liked drinks:', data.message);
        })
        .catch(error => {
          console.error('Error adding drink to liked drinks:', error);
        });
    }
  });


  // Event listener for clicking on featured drinks
  if (featuredCategories) {
    featuredCategories.addEventListener('click', function (event) {
    const clickedElement = event.target.closest('.featured-category');
      if (clickedElement) {
        event.preventDefault();
        const selectedCategory = clickedElement.getAttribute('data-category');
        const featuredFilterBy = 'category'; 
        const featuredDrink = selectedCategory; 

        // Update the hidden form inputs with the filter and search value
        document.getElementById('featured-filter-by').value = featuredFilterBy;
        document.getElementById('featured-drink').value = featuredDrink;

        // Trigger the form submission
        document.getElementById('featured-drink-form').submit();
      }
    });

  }else{
    console.log("featuredCategories is null");
  }



module.exports = {
  createIngredientsList,
  displayResults,
  performSearch
};

});