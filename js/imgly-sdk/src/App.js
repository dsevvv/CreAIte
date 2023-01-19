import './App.css';
import { PhotoEditorSDK } from './Editor';

function App() {
  return (
    <div className="App">
      <PhotoEditorSDK 
        templateImage={'https://i.imgur.com/sKV54PO.jpeg'} 
        editableImage={'https://i.imgur.com/IimRBXs.jpeg'}        
      />
    </div>
  );
}

export default App;
