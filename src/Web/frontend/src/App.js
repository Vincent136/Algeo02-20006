import { useEffect, useState } from 'react';
import './App.css';
import Button from './components/Button';
import UploadImage from './components/UploadImage';

function App() {
  const onClick = () => {
    alert('Click');
  };

  const [currentTime, setCurrentTime] = useState(0);

  // useEffect(() => {
  //   fetch('time').then((res) =>
  //     res.json().then((data) => {
  //       setCurrentTime(data.time);
  //     })
  //   );
  // });

  return (
    <div className="App">
      <header>
        <h1>Smol Image</h1>
      </header>
      <UploadImage />
      <Button color="red" text="Compress" onClick={onClick} />
      <p>The current time is {currentTime}</p>
    </div>
  );
}

export default App;
