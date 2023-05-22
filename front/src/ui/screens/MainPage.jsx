import { useState } from "react";
import Header from "../components/header";

const MainPage = (props) => {

    const { goToLoginPage, currentUser, onExit } = props;

    return(
        <Header currentUser={currentUser} goToLoginPage={goToLoginPage} onExit={onExit}/>
    )
}

export default MainPage;