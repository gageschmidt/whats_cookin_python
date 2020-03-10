import React from 'react';
import './homepage.css'

function getDjangoHomeApi() {
    try {
        fetch("http://127.0.0.1:8000"
        )
          .then(response => response.json())
            .then( response => {
            console.log(response);
          });
    } catch (e) {
        console.log(e);
    }
}

function Homepage() {
    getDjangoHomeApi();
    return (
        <div id="recipe-otd">
            <div className="recipe-title">
               <span className="recipe-otd-title">
                   Recipe of the day
               </span>
            </div>
            <div className="recipe-name">
                <span className="recipe-name-text">
                    Recipe Name:
                </span>
            </div>
            <div className="recipe-ingredients">
                <span className="recipe-ingredients-text">
                    Recipe Ingredients:
                </span>
            </div>
            <div className="recipe-directions">
                <span className="recipe-directions-text">
                    Recipe Directions:
                </span>
            </div>
        </div>)}

export default Homepage;
