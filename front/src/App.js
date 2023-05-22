import { useEffect, useState } from 'react';
import LoginPage from './ui/screens/LoginPage';
import MainPage from './ui/screens/MainPage';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { BASE_URL } from './const';

function App() {

  const [currentPage, setCurrentPage] = useState('main');
  const [currentUser, setCurrentUser] = useState(null);

  const goToLoginPage = () => setCurrentPage('login');
  const goToMainPage = () => setCurrentPage('main');

  useEffect(() => {
    const token = localStorage.getItem('token');
    if (token) {

      const getUser = async () => {
        try {
          const response = await fetch(`${BASE_URL}api/auth/users/me/`, {
            method: 'GET',
            headers: {
              Authorization: `Token ${token}`
            }
          })
          const parsedResult = await response.json();
          setCurrentUser(parsedResult);
          toast.success(`Добро пожаловать, ${parsedResult.username}!`);
        } catch (error) {
          toast.error(`Ошибка: ${error}`);
        }
      }
      
      getUser();
    }
  }, [])

  const handleExitClick = async () => {
    const token = localStorage.getItem('token');
    try {
      const response = await fetch(`${BASE_URL}api/auth/token/logout/`, {
          method: 'POST',
          headers: {
            Authorization: `Token ${token}`
          }
        })
      if (response.ok) {
        toast.success('Ждём вашего возвращения!');
        setCurrentUser(null);
        localStorage.removeItem('token');
      } else {
        toast.error('Ошибка, что-то пошло не так :(');
      }
    } catch (error) {
      toast.error(`Ошибка: ${error}`);
    }
  }

  return (
    <div className="App">
      {currentPage === 'main' && <MainPage goToLoginPage={goToLoginPage} currentUser={currentUser} onExit={handleExitClick} />}
      {currentPage === 'login' && <LoginPage goToMainPage={goToMainPage} onSetUser={setCurrentUser} />}
      <ToastContainer />
    </div>
  );
}

export default App;
