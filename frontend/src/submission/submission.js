import React from "react";
import './submission.css';

class Submission extends React.Component
{
    constructor(props) {
        super(props);
        this.state = {inputs: ['input-0']};
    }

    appendInput() {
        let newInput = `input-${this.state.inputs.length}`;
        this.setState(prevState => ({ inputs: prevState.inputs.concat([newInput])}));
    }

    render() {

        return  <div id="submission-container">
                    <form>
                        <input type='text' id='name-input' />
                        <input type='text' className='ingredients-input' id='ingredients-input-1'/>
                        <div>
                            {this.state.inputs.map(input => <input type='text' key={input}/>)}
                        </div>
                        <button onClick={ () => this.appendInput() }> Need another line? </button>
                        <input type='text' className='directions-input' id='directions-input-1'/>
                    </form>
                </div>
    }
}
export default Submission;