import { useState } from "react";
import { toast } from "react-toastify";
import { BASE_URL } from "../../const";

function LoginPage(props) {

    const { goToMainPage, onSetUser } = props;

    const [isLoginFormActive, setIsLoginFormActive] = useState(true);

    //login
    const [loginName, setLoginName] = useState('');
    const [loginPassword, setLoginPassword] = useState('');

    //registration
    const [regName, setRegName] = useState('');
    const [regPassword, setRegPassword] = useState('');

    const handleRegistrationClick = async () => {
        if (!regName || !regPassword) {
           toast.error('Имя и пароль не должны быть пустыми!');
           return
        } 
        const formdata = new FormData();
        formdata.append('username', regName);
        formdata.append('password', regPassword);
        try {
            const result = await fetch(`${BASE_URL}api/auth/users/`, {
                method: 'POST',
                body: formdata
            })
            console.log(result, 'result')
            const parsedResult = await result.json();
            console.log(parsedResult, 'parsedResult')
            if (parsedResult?.password) {
                toast.error(parsedResult?.password.join(' '));
            } else {
                toast.success('Пользователь успешно создан!');
                setIsLoginFormActive(true);
                setLoginName(regName);
                setRegName('');
                setRegPassword('');
                setLoginPassword('');
            }
        } catch (error) {
            toast.error(`Ошибка: ${error}`)
        }
    }

    const handleLoginClick = async () => {
        if (!loginName || !loginPassword) {
            toast.error('Имя и пароль не должны быть пустыми!');
            return;
        }
        const formdata = new FormData();
        formdata.append('username', loginName);
        formdata.append('password', loginPassword);
        try {
            const result = await fetch(`${BASE_URL}api/auth/token/login/`, {
                method: 'POST',
                body: formdata
            })
            const parsedResult = await result.json();
            if (parsedResult?.non_field_errors) {
                toast.error(parsedResult?.non_field_errors.join(' '));
            } else {
                toast.success(`Добро пожаловать, ${loginName}!`);
                localStorage.setItem('token', parsedResult.auth_token);
                setLoginName('');
                setLoginPassword('');
                onSetUser({username: loginName});
                goToMainPage();
            }
        } catch (error) {
            toast.error(`Ошибка: ${error}`)
        }
    }

    return (

        <section className="login">
            <div className="login__content">
                <button
                    onClick={() => goToMainPage()}
                    className="login__back back-button"
                >
                    <svg width="24" height="24" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" fillRule="evenodd" clipRule="evenodd"><path d="M2.117 12l7.527 6.235-.644.765-9-7.521 9-7.479.645.764-7.529 6.236h21.884v1h-21.883z" /></svg>
                </button>
                {isLoginFormActive ? (
                    <>
                        <h1 className="login__title">Введите логин и пароль</h1>
                        <div className="login__form">
                            <input value={loginName} onChange={(e) => setLoginName(e.target.value)} type="text" placeholder="логин" />
                            <input value={loginPassword} onChange={(e) => setLoginPassword(e.target.value)} type="password" placeholder="пароль" />
                            <button onClick={handleLoginClick} className="common-button" type="submit">Войти</button>
                        </div>
                        <button
                            onClick={() => setIsLoginFormActive(false)}
                            className="login__toReg"
                        >
                            или Зарегистрироваться
                        </button>
                    </>
                ) : (
                    <>
                        <h1 className="login__title">Регистрация</h1>
                        <div className="login__form">
                            <input value={regName || ''} onChange={(e) => setRegName(e.target.value)} type="text" placeholder="логин" />
                            <input value={regPassword || ''} onChange={(e) => setRegPassword(e.target.value)} type="password" placeholder="пароль" />
                            <button onClick={handleRegistrationClick} className="common-button" type="submit">Зарегестрироваться</button>
                        </div>
                        <div className="login__infoText">
                            <svg xmlns="http://www.w3.org/2000/svg" width="24" height="24" viewBox="0 0 24 24"><path d="M12 2c5.514 0 10 4.486 10 10s-4.486 10-10 10-10-4.486-10-10 4.486-10 10-10zm0-2c-6.627 0-12 5.373-12 12s5.373 12 12 12 12-5.373 12-12-5.373-12-12-12zm-2.033 16.01c.564-1.789 1.632-3.932 1.821-4.474.273-.787-.211-1.136-1.74.209l-.34-.64c1.744-1.897 5.335-2.326 4.113.613-.763 1.835-1.309 3.074-1.621 4.03-.455 1.393.694.828 1.819-.211.153.25.203.331.356.619-2.498 2.378-5.271 2.588-4.408-.146zm4.742-8.169c-.532.453-1.32.443-1.761-.022-.441-.465-.367-1.208.164-1.661.532-.453 1.32-.442 1.761.022.439.466.367 1.209-.164 1.661z"/></svg>
                            <p>Длинна логина и пароля должна быть не менее 8 символов. Пароль должен состоять из букв и цифр.</p>
                        </div>
                        <button
                            onClick={() => setIsLoginFormActive(true)}
                            className="login__toReg"
                        >
                            у меня уже есть Аккаунт
                        </button>
                    </>
                )}
            </div>
        </section>

    );
}

export default LoginPage;