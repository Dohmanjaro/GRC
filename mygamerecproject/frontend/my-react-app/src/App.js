// my-react-app/src/App.js
import React from 'react';
import SearchBar from './SearchBar';

const App = () => {
  const handleSearch = (searchTerm) => {
    // You can perform actions related to searching (e.g., make API request) here
    console.log(`Searching for: ${searchTerm}`);
  };

  return (
    <div>
      <h1>Game Search App</h1>
      <SearchBar onSearch={handleSearch} />
      {/* Other React components or content */}
    </div>
  );
};

export default App;
