import React from 'react';
import ReactDOM from 'react-dom';
import * as serviceWorker from './serviceWorker';
import Homepage from "./home/homepage";
import Navigation from "./navigation/navigation";
import Submission from "./submission/submission"
import {BrowserRouter, Switch, withRouter} from 'react-router-dom';
import { Router, Route } from "react-router";

ReactDOM.render(<BrowserRouter>
                    <Navigation />
                    <Switch>
                        <Route path='/' component={ Homepage } exact/>
                        <Route path='/submit' component={ withRouter( Submission ) } exact/>
                    </Switch>
                </BrowserRouter>, document.getElementById('root')
);


// If you want your app to work offline and load faster, you can change
// unregister() to register() below. Note this comes with some pitfalls.
// Learn more about service workers: https://bit.ly/CRA-PWA
serviceWorker.unregister();
