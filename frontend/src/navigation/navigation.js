import React from "react";
import './navigation.css';

function fontAwesomeCdn() {
    let script = document.createElement('script');
    script.src = "https://kit.fontawesome.com/f2647e425b.js";
    script.crossOrigin = 'anonymous';
    document.body.appendChild(script);
}

function Navigation() {
    fontAwesomeCdn();
    return (
        <nav className="nav">
            <ul className="nav-ul">
                <li className="nav-item">
                    <a className="nav-link" href="/">
                        <i className="fas fa-hamburger fa-3x"></i>
                        <span className="nav-text">
                         Homepage
                        </span>
                    </a>
                </li>
                <li className="nav-item">
                    <a className="nav-link" href="/submit">
                        <i className="fas fa-pizza-slice  fa-3x"></i>
                        <span className="nav-text">
                         Submit Recipe
                        </span>
                    </a>
                </li>
                <li className="nav-item">
                    <a className="nav-link" href="#">
                        <i className="fas fa-carrot  fa-3x"></i>
                        <span className="nav-text">
                         Nothing yet
                        </span>
                    </a>
                </li>
            </ul>
        </nav>
    )}

export default Navigation;