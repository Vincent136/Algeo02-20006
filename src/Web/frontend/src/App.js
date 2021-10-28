import './App.css';
import Button from './components/Button';
import UploadImage from './components/UploadImage';

function App() {
  const onClick = () => {
    alert('Click');
  };

  return (
    <div className="App">
      <header>
        <h1>Smol Image</h1>
      </header>
      <UploadImage />

      <Button color="red" text="Compress" onClick={onClick} />
    </div>
  );
}

export default App;
