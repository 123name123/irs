import { useEffect, useState } from "react";
import Header from "../components/header";
import Loader from "../components/loader";
import { toast } from "react-toastify";
import { BASE_URL } from "../../const";

const MainPage = (props) => {

    const { goToLoginPage, search, currentUser, onExit, products, getProducts, prodLoader, isFavoritsActive, setIsFavoritsActive } = props;

    const [searchValue, setSearchValue] = useState('');

    const handleLikeClick = async (evt, id) => {
        evt.stopPropagation();
        if (evt.target.classList.contains('active')) {
            //dislike
            try {
                const response = await fetch(`${BASE_URL}api/v1/favorites/${id}/`, {
                    method: 'DELETE',
                    headers: {
                        Authorization: `Token ${localStorage.getItem('token')}`
                      }
                })
                if (response.ok) {
                    evt.target.classList.remove('active');
                    toast.success('Товар удален из избранного');
                } else {
                    toast.error('Ошибка, что-то пошло не так :(');
                }
            } catch (error) {
                toast.error(`Ошибка: ${error}`);
            }
        } else {
            //like
            try {
                const formData = new FormData();
                formData.append('product_id', id)
                const response = await fetch(`${BASE_URL}api/v1/favorites/`, {
                    method: 'POST',
                    body: formData,
                    headers: {
                        Authorization: `Token ${localStorage.getItem('token')}`
                      }
                })
                if (response.ok) {
                    evt.target.classList.add('active');
                    toast.success('Товар добавлен в избранное!');
                } else {
                    toast.error('Ошибка, что-то пошло не так :(');
                }
            } catch (error) {
                toast.error(`Ошибка: ${error}`);
            }
        }
    }

    return (
        <>
            <Header prodLoader={prodLoader} currentUser={currentUser} goToLoginPage={goToLoginPage} onExit={onExit} isFavoritsActive={isFavoritsActive} setIsFavoritsActive={setIsFavoritsActive} />
            {!isFavoritsActive && (
                <div className="search">
                    <input value={searchValue} onChange={(e) => setSearchValue(e.target.value)} type="text" />
                    <button onClick={() => search(searchValue)} disabled={!searchValue} className="common-button">Find</button>
                    <button onClick={() => {setSearchValue(''); getProducts(`${BASE_URL}api/v1/products/`)}} className="common-button">Clear</button>
                </div>
            )}
            <section className="mainPage">
                <h2>Всего товаров: {products?.count || 0}</h2>
                {prodLoader && <Loader />}
                {products?.results?.length > 0 && !prodLoader && (
                    <>
                        <ul className="mainPage__list">
                            {products?.results?.length > 0 && products.results.map((product) => (
                                <li className="mainPage__item" key={product?.id}>
                                    <h2>{product?.title}</h2>
                                    <p><b>Цена:</b> {product?.price} $</p>
                                    <p><b>Код товара:</b> {product?.item_id}</p>
                                    {(product?.description && product?.description !== 'NULL') && <p className="mainPage__desc custom-scroll">{product?.description}</p>}
                                    <p><b>Поставщик:</b> {product?.supplier?.name}</p>
                                    <button className={`mainPage__like`} onClick={(evt) => handleLikeClick(evt, product.id)} >
                                        <svg clipRule="evenodd" fillRule="evenodd" strokeLinejoin="round" strokeMiterlimit="2" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="m12 5.72c-2.624-4.517-10-3.198-10 2.461 0 3.725 4.345 7.727 9.303 12.54.194.189.446.283.697.283s.503-.094.697-.283c4.977-4.831 9.303-8.814 9.303-12.54 0-5.678-7.396-6.944-10-2.461z" fill-rule="nonzero" /></svg>
                                    </button>
                                </li>
                            ))}
                        </ul>
                        <div className="mainPage__btns">
                            <button onClick={() => getProducts(products?.previous)} className={`${products?.previous ? 'active' : ''}`}>PREV</button>
                            <button onClick={() => getProducts(products?.next)} className={`${products?.next ? 'active' : ''}`}>NEXT</button>
                        </div>
                    </>
                )}
            </section>
        </>
    )
}

export default MainPage;