import React from "react";
import './navigation.css';


class Navigation extends React.Component
{

    fontAwesomeCdn() {
        let script = document.createElement('script');
        script.src = "https://kit.fontawesome.com/f2647e425b.js";
        script.crossOrigin = 'anonymous';
        document.body.appendChild(script);
    }


   render() {
        this.fontAwesomeCdn();
        return (
            <nav className="nav">
                <ul className="nav-ul">
                    <li className="nav-item">
                        <a className="nav-link" href="/">
                            &nbsp;
                            &nbsp;
                            <i className="fas fa-hamburger fa-2x"></i>
                            <span className="nav-text">
                           &nbsp; Homepage
                        </span>
                        </a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href={'/submit'}>
                            &nbsp;
                            &nbsp;
                            <i className="fas fa-pizza-slice  fa-2x"></i>
                            <span className="nav-text">
                         &nbsp; Submit Recipe
                        </span>
                        </a>
                    </li>
                    <li className="nav-item">
                        <a className="nav-link" href="#">
                            &nbsp;
                            &nbsp;
                            <i className="fas fa-carrot  fa-2x"></i>
                            <span className="nav-text">
                         &nbsp; Nothing yet
                        </span>
                        </a>
                    </li>
                </ul>
            </nav>
        )
    }
}
export default Navigation;