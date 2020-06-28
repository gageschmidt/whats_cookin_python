import React from 'react';
import './homepage.css'

class Homepage extends React.Component {
    directions;
    ingredients;
    constructor(props) {
        super(props);
        this.state = {
            error: null,
            isLoaded: false,
            recipe: []
        };
    }

    componentDidMount() {
        fetch("http://127.0.0.1:8000")
            .then(response => response.json())
            .then(response => {
                this.setState({
                    isLoaded: true,
                    recipe: response
                })
            },
            (error) => {
                this.setState({
                    isLoaded: true,
                    error
                })
            }
        )
    }

    render() {
        const {error, isLoaded, recipe} = this.state;
        if (error) {
            return <div>Error: {error.message}</div>;
        } else if (!isLoaded) {
            return <div>Loading...</div>;
        } else {
            const ingredients = recipe.ingredients.map(
                (ingredient, i) => <li key={i}>{ingredient}</li>
            );
            const directions = recipe.directions.map(
                (direction, i) => <li key={i}>{direction}</li>
            );
            return (
                <div id="recipe-otd">
                    <div className="recipe-title">
                       <span className="recipe-otd-title">
                           Recipe of the day
                       </span>
                    </div>
                    <div className="recipe-name">
                        <h3>
                            {recipe.name}
                        </h3>
                    </div>
                    <div className="recipe-ingredients">
                        <span className="recipe-ingredients-text">
                            Ingredients:
                        </span>
                        <h3>
                            {ingredients}
                        </h3>
                    </div>
                    <div className="recipe-directions">
                        <span className="recipe-directions-text">
                            Directions:
                        </span>
                         <h3>
                            {directions}
                        </h3>
                    </div>
                </div>)
        }
    }
}
export default Homepage;
