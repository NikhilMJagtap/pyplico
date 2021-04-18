import './App.scss';
import {Component} from 'react';
import Sidebar from './components/Sidebar/Sidebar';
import Workspace from './components/Workspace/Workspace';
import {BrowserRouter} from 'react-router-dom';

class App extends Component {


  render() {
    return (
      <BrowserRouter>
      <div className='App'>
        <Sidebar/>
        <Workspace/>
      </div>
      </BrowserRouter>
    )
  }

}

export default App;
