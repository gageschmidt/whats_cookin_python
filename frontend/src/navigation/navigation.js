import React from "react";
import './navigation.css';

function fontAwesomeCdn() {
    let script = document.createElement('script');
    script.src = "https://kit.fontawesome.com/f2647e425b.js";
    script.crossOrigin = 'anonymous';
    document.body.appendChild(script);
}

function moveRecipeOfTheDay() {
    console.log('hello?');
    let recipeElement = document.getElementById('recipe-otd');
    let navigationElement = document.getElementsByClassName('nav');
    navigationElement.onmouseover = function () {
        recipeElement.setAttribute('style', 'left: 55%;')
    }
}

function Navigation() {
    fontAwesomeCdn();
    return (
        <nav className="nav" onMouseOver={moveRecipeOfTheDay()}>
            <ul className="nav-ul">
                <li className="nav-item">
                    <a className="nav-link" href="/">
                          &nbsp;
                        <i className="fas fa-hamburger fa-3x"></i>
                        <span className="nav-text">
                           &nbsp; Homepage
                        </span>
                    </a>
                </li>
                <li className="nav-item">
                    <a className="nav-link" href="/submit">
                        &nbsp;
                        <i className="fas fa-pizza-slice  fa-3x"></i>
                        <span className="nav-text">
                         &nbsp; Submit Recipe
                        </span>
                    </a>
                </li>
                <li className="nav-item">
                    <a className="nav-link" href="#">
                          &nbsp;
                        <i className="fas fa-carrot  fa-3x"></i>
                        <span className="nav-text">
                         &nbsp; Nothing yet
                        </span>
                    </a>
                </li>
            </ul>
        </nav>
    )}

export default Navigation;