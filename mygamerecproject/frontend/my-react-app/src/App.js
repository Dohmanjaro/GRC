// const App = () => {
//   const [searchResult, setSearchResult] = useState(null);

//   const handleSearch = async (searchTerm) => {
//     try {
//       const response = await fetch(`?search=${searchTerm}`);
//       const data = await response.json();

//       // Update state with the search result
//       setSearchResult(data.result);
//     } catch (error) {
//       console.error('Error during search:', error);
//     }
//   };
import React, { useState } from 'react';
import SearchBar from './SearchBar';

const App = () => {
  const [searchTerm, setSearchTerm] = useState('');

  const handleSearch = (searchTerm) => {
    // Update state with the search term
    setSearchTerm(searchTerm);

    // You can perform additional actions with the search term if needed
    // For example, you can make an API request here or trigger other functionality
  };

  const containerStyle = {
    maxWidth: '600px',
    margin: 'auto',
    padding: '20px',
    textAlign: 'center',
    boxShadow: '0 0 10px rgba(0, 0, 0, 0.1)',
    borderRadius: '8px',
  };

  const headerStyle = {
    color: '#333',
  };

  const resultStyle = {
    marginTop: '20px',
    fontSize: '18px',
    color: '#007BFF',
  };

  return (
    <div>
      <h1 style={headerStyle}>Game Search App</h1>
      <SearchBar onSearch={handleSearch} />
      {/* Omitted other React components or content */}
    </div>
  );
};

export default App;