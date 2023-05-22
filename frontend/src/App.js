import { useEffect, useState } from 'react';
import LoginPage from './ui/screens/LoginPage';
import MainPage from './ui/screens/MainPage';
import { toast, ToastContainer } from 'react-toastify';
import 'react-toastify/dist/ReactToastify.css';
import { BASE_URL } from './const';

function App() {

  const [currentPage, setCurrentPage] = useState('main');
  const [currentUser, setCurrentUser] = useState(null);
  const [products, setProducts] = useState([]);
  const [prodLoader, setProdLoader] = useState(false);
  const [isFavoritsActive, setIsFavoritsActive] = useState(false);

  console.log(products, 'products');

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
        } catch (error) {
          toast.error(`Ошибка: ${error}`);
        }
      }

      getUser();
    }

  }, []);

  const getProducts = async (url) => {
    setProdLoader(true);
    try {
      const response = await fetch(url, {
        method: 'GET',
      })
      const parsedResult = await response.json();
      setProducts(parsedResult);
    } catch (error) {
      toast.error(`Ошибка: ${error}`);
    } finally {
      setProdLoader(false);
    }
  }

  const getFavorits = async () => {
    setProdLoader(true);
    try {
      const response = await fetch(`${BASE_URL}api/v1/favorites/`, {
        method: 'GET',
        headers: {
          Authorization: `Token ${localStorage.getItem('token')}`
        }
      })
      const parsedResult = await response.json();
      const newArr = parsedResult.results.map((item) => item.product[0]);
      console.log(parsedResult, 'fav');
      setProducts({...parsedResult, results: newArr});
    } catch (error) {
      toast.error(`Ошибка: ${error}`);
    } finally {
      setProdLoader(false);
    }
  }

  const search = async (word) => {
    setProdLoader(true);
    try {
      const response = await fetch(`${BASE_URL}api/v1/products/?supplier_name=${word}`, {
        method: 'GET',
        headers: {
          Authorization: `Token ${localStorage.getItem('token')}`
        }
      })
      const parsedResult = await response.json();
      setProducts(parsedResult);
    } catch (error) {
      toast.error(`Ошибка: ${error}`);
    } finally {
      setProdLoader(false);
    }
  }

  useEffect(() => {
    if (currentUser) {
      if (isFavoritsActive) {
        getFavorits();
      } else {
        getProducts(`${BASE_URL}api/v1/products/`);
      }
    }
  }, [currentUser, isFavoritsActive]);

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
      {currentPage === 'main' &&
        <MainPage
          goToLoginPage={goToLoginPage}
          currentUser={currentUser}
          onExit={handleExitClick}
          products={products}
          getProducts={getProducts}
          prodLoader={prodLoader}
          isFavoritsActive={isFavoritsActive}
          setIsFavoritsActive={setIsFavoritsActive}
          search={search}
        />
      }
      {currentPage === 'login' && <LoginPage goToMainPage={goToMainPage} onSetUser={setCurrentUser} />}
      <ToastContainer />
    </div>
  );
}

export default App;
