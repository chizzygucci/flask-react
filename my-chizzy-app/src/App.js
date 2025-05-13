import React, { useEffect, useState } from 'react';

function App() {
  const [items, setItems] = useState([]);

  useEffect(() => {
    fetch('http://localhost:5000/api/items')
      .then((response) => response.json())
      .then((data) => setItems(data));
  }, []);  // Empty dependency array

  return (
    <div className="App">
      <h1>Items List</h1>
      <ul>
        {items.map((item) => (
          <li key={item.id}>{item.name}</li>
        ))}
      </ul>
    </div>
  );
}

export default App;

