import { BrowserRouter, Route, Routes } from 'react-router-dom';
import Login from './components/Login';
import Profile from './components/Profile';
import Header from './components/Header';
import useToken from './components/useToken';
import './App.css';
import React from 'react';

function App() {
  const { token, removeToken, setToken } = useToken();
  return(
    <BrowserRouter>
      <div className='App'>
        <Header token={removeToken}/>
        {!token && token!=="" &&token !== undefined?
          <Login setToken={setToken} />
          :(
            <>
              <Routes>
                asd
                <Route path="/profile" element={<Profile token={token} setToken={setToken} />} />
                <Route path="/" element={<Home />} />
              </Routes>
            </>
          )
        }
      </div>
    </BrowserRouter>
  );

  function Home(){
    return (
      <a href='/profile'>Profile</a>
      )
  }
}

export default App;