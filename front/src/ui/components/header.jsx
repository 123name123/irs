function Header(props) {

    const { currentUser } = props;
    const { goToLoginPage } = props;
    const { onExit } = props;

    return ( 
        <header className="header">
            <svg className="header__svg" clipRule="evenodd" fillRule="evenodd" strokeLinejoin="round" strokeMiterlimit="2" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg"><path d="m21 4c0-.478-.379-1-1-1h-16c-.62 0-1 .519-1 1v16c0 .621.52 1 1 1h16c.478 0 1-.379 1-1zm-3 9.5v4c0 .276-.224.5-.5.5h-4c-.276 0-.5-.224-.5-.5v-4c0-.276.224-.5.5-.5h4c.276 0 .5.224.5.5zm-10.061 1.99-1.218-1.218c-.281-.281-.282-.779 0-1.061s.78-.281 1.061 0l1.218 1.218 1.218-1.218c.281-.281.779-.282 1.061 0s.281.78 0 1.061l-1.218 1.218 1.218 1.218c.281.281.282.779 0 1.061s-.78.281-1.061 0l-1.218-1.218-1.218 1.218c-.281.281-.779.282-1.061 0s-.281-.78 0-1.061zm8.561-.99h-2v2h2zm-7.5-8.5c1.656 0 3 1.344 3 3s-1.344 3-3 3-3-1.344-3-3 1.344-3 3-3zm9 5.25c0 .399-.353.75-.75.75-1.153 0-2.347 0-3.5 0-.397 0-.75-.351-.75-.75s.353-.75.75-.75h3.5c.397 0 .75.351.75.75zm-9-3.75c.828 0 1.5.672 1.5 1.5s-.672 1.5-1.5 1.5-1.5-.672-1.5-1.5.672-1.5 1.5-1.5zm9 1.5c0 .399-.353.75-.75.75-1.153 0-2.347 0-3.5 0-.397 0-.75-.351-.75-.75s.353-.75.75-.75h3.5c.397 0 .75.351.75.75zm0-2.25c0 .399-.353.75-.75.75-1.153 0-2.347 0-3.5 0-.397 0-.75-.351-.75-.75s.353-.75.75-.75h3.5c.397 0 .75.351.75.75z" fillRule="nonzero"/></svg>
            <h1>Recomendation</h1>
            <div className="header__buttons">
                { currentUser ? (
                    <>
                        <button className="header__button common-button">My favorits ♥</button>
                        <span>{currentUser.username}</span>
                        <button className="header__exit" onClick={onExit}>
                            <svg width="24" height="24" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 24 24" fill-rule="evenodd" clip-rule="evenodd"><path d="M11 21h8v-2l1-1v4h-9v2l-10-3v-18l10-3v2h9v5l-1-1v-3h-8v18zm10.053-9l-3.293-3.293.707-.707 4.5 4.5-4.5 4.5-.707-.707 3.293-3.293h-9.053v-1h9.053z"/></svg>
                        </button>
                    </>
                    ) : (
                    <>
                        <button
                        className="header__button common-button"
                        onClick={() => goToLoginPage()}
                        >
                            Login
                        </button>
                    </>
                ) }
            </div>
        </header>
    );
}

export default Header;