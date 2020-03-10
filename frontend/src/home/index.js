import React from 'react';
import ReactDOM from 'react-dom';
import * as serviceWorker from '/serviceWorker';
import homepage from "../home/homepage";

ReactDOM.render(<homepage />, document.getElementById('root'));

serviceWorker.unregister();