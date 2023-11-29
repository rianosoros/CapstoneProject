const { createIngredientsList, displayResults, performSearch } = require('../static/script.js');

const { JSDOM } = require('jsdom');
const dom = new JSDOM('<!doctype html><html><body></body></html>');

const script = require('../static/script.js');




describe('My App Tests', () => {

  describe('createIngredientsList function', () => {
    it('should create an ingredients list', () => {
      const drink = {
        strIngredient1: 'Tequila',
        strMeasure1: '2 oz',
        strIngredient2: 'Triple sec',
        strMeasure2: '1 oz',
        strIngredient3: 'Lime juice',
        strMeasure3: '1 oz',
        strIngredient4: 'Salt',
        strMeasure4: '1 dash',
      };

      const result = createIngredientsList(drink);

      expect(result.includes('<li>2 oz Tequila</li>')).toBeTruthy();
      expect(result.includes('<li>1 oz Triple sec</li>')).toBeTruthy();
    });
  });

  describe('performSearch function', () => {
    it('should perform a search and display results', async () => {
      const filterBy = 'drink-name';
      const searchValue = 'MockDrink';

      const drinkResults = document.createElement('div');
      document.body.appendChild(drinkResults);

      await performSearch(filterBy, searchValue);

      expect(drinkResults.innerHTML.includes('<div class="drink-card" data-id="123">')).toBeTruthy();
    });

    it('should handle a failed search', async () => {
      const filterBy = 'drink-name';
      const searchValue = 'MockDrink';

      spyOn(global, 'fetch').and.returnValue(Promise.resolve({
        ok: false,
        json: () => Promise.resolve({ drinks: [] }),
      }));

      const drinkResults = document.createElement('div');
      document.body.appendChild(drinkResults);

      await performSearch(filterBy, searchValue);

      expect(drinkResults.innerHTML.includes('<p>No results found</p>')).toBeTruthy();
    });

    it('should handle a search with no results', async () => {
      const filterBy = 'drink-name';
      const searchValue = 'MockDrink';

      spyOn(global, 'fetch').and.returnValue(Promise.resolve({
        ok: true,
        json: () => Promise.resolve({ drinks: [] }),
      }));

      const drinkResults = document.createElement('div');
      document.body.appendChild(drinkResults);

      await performSearch(filterBy, searchValue);

      expect(drinkResults.innerHTML.includes('<p>No results found</p>')).toBeTruthy();
    });

    it('should handle an error', async () => {
      const filterBy = 'drink-name';
      const searchValue = 'MockDrink';

      spyOn(global, 'fetch').and.returnValue(Promise.reject('API is down'));

      const drinkResults = document.createElement('div');
      document.body.appendChild(drinkResults);

      await performSearch(filterBy, searchValue);

      expect(drinkResults.innerHTML.includes('<p>Something went wrong</p>')).toBeTruthy();
    });

    it('should handle a search with no value', async () => {
      const filterBy = 'drink-name';
      const searchValue = '';

      const drinkResults = document.createElement('div');
      document.body.appendChild(drinkResults);

      await performSearch(filterBy, searchValue);

      expect(drinkResults.innerHTML.includes('<p>Please enter a search value</p>')).toBeTruthy();
    });

    it('should handle a search with no filter', async () => {
      const filterBy = '';
      const searchValue = 'MockDrink';

      const drinkResults = document.createElement('div');
      document.body.appendChild(drinkResults);

      await performSearch(filterBy, searchValue);

      expect(drinkResults.innerHTML.includes('<p>Please select a filter</p>')).toBeTruthy();
    });

  });
});
