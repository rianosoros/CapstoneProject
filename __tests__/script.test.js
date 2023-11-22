// __tests__/script.test.js
const { createIngredientsList, displayResults, performSearch } = require('../script');

// Mock global functions or objects used in your tests
global.fetch = jest.fn(() =>
  Promise.resolve({
    ok: true,
    json: () => Promise.resolve({ drinks: [{ strDrink: 'MockDrink', idDrink: '123' }] }),
  })
);

describe('My App Tests', () => {
  // Test for the createIngredientsList function
  describe('createIngredientsList function', () => {
    it('should create an ingredients list', () => {
      const drink = {
        strIngredient1: 'Ingredient1',
        strMeasure1: '1 oz',
        strIngredient2: 'Ingredient2',
        strMeasure2: '2 oz',
      };

      const result = createIngredientsList(drink);

      expect(result).toContain('<li>1 oz Ingredient1</li>');
      expect(result).toContain('<li>2 oz Ingredient2</li>');
    });
  });

  // Test for the performSearch function
  describe('performSearch function', () => {
    it('should perform a search and display results', async () => {
      const filterBy = 'drink-name';
      const searchValue = 'MockDrink';

      const drinkResults = document.createElement('div');
      document.body.appendChild(drinkResults);

      await performSearch(filterBy, searchValue);

      expect(drinkResults.innerHTML).toContain('<div class="drink-card" data-id="123">');
    });

    it('should handle a failed search', async () => {
      const filterBy = 'drink-name';
      const searchValue = 'MockDrink';

      global.fetch = jest.fn(() =>
        Promise.resolve({
          ok: false,
          json: () => Promise.resolve({ drinks: [] }),
        })
      );

      const drinkResults = document.createElement('div');
      document.body.appendChild(drinkResults);

      await performSearch(filterBy, searchValue);

      expect(drinkResults.innerHTML).toContain('<p>No results found</p>');
    });

    it('should handle a search with no results', async () => {
      const filterBy = 'drink-name';
      const searchValue = 'MockDrink';

      global.fetch = jest.fn(() =>
        Promise.resolve({
          ok: true,
          json: () => Promise.resolve({ drinks: [] }),
        })
      );

      const drinkResults = document.createElement('div');
      document.body.appendChild(drinkResults);

      await performSearch(filterBy, searchValue);

      expect(drinkResults.innerHTML).toContain('<p>No results found</p>');
    });

    it('should handle an error', async () => {
      const filterBy = 'drink-name';
      const searchValue = 'MockDrink';

      global.fetch = jest.fn(() => Promise.reject('API is down'));

      const drinkResults = document.createElement('div');
      document.body.appendChild(drinkResults);

      await performSearch(filterBy, searchValue);

      expect(drinkResults.innerHTML).toContain('<p>Something went wrong</p>');
    });

    it('should handle a search with no value', async () => {
      const filterBy = 'drink-name';
      const searchValue = '';

      const drinkResults = document.createElement('div');
      document.body.appendChild(drinkResults);

      await performSearch(filterBy, searchValue);

      expect(drinkResults.innerHTML).toContain('<p>Please enter a search value</p>');
    });

    it('should handle a search with no filter', async () => {
      const filterBy = '';
      const searchValue = 'MockDrink';

      const drinkResults = document.createElement('div');
      document.body.appendChild(drinkResults);

      await performSearch(filterBy, searchValue);

      expect(drinkResults.innerHTML).toContain('<p>Please select a filter</p>');
    });

  });
});
